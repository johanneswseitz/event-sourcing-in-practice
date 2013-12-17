import os
import datetime
import logging
import re

from markdown import markdown
from markdown.preprocessors import Preprocessor
from markdown.extensions import Extension


# TODO: extract this into a module of its own
class CodeSnippets(Extension):
    def __init__(self, seek_directory):
        self.seek_directory = seek_directory

    def extendMarkdown(self, md, md_globals):
        preproc = CodeSnippetIncludingPreProcessor(self.seek_directory)
        md.preprocessors.add('code_snippets', preproc, '_begin')
 
class CodeSnippetIncludingPreProcessor(Preprocessor):
    def __init__(self, seek_directory):
        self.satement_replacers = [CodeIncludeSatementReplacer(seek_directory)]

    def run(self, lines):
        new_lines = []
        for line in lines:
            for replacer in self.satement_replacers:
                if (replacer.replaces(line)):
                    new_lines.append(replacer.replacement_for(line))
                else: 
                    new_lines.append(line)
        return new_lines



class CodeIncludeSatementReplacer(object):
    def __init__(self, seek_directory):
        self.include_statement = re.compile(r"@(\(([^\)]*)\))?\[([^\]]*)\]")
        self.seek_directory = seek_directory

    def replaces(self, line):
        return self.include_statement.match(line) != None
 
    def replacement_for(self, line):
        parameters = self.include_statement.search(line)
        include_file = parameters.group(3)
        if not os.path.isabs(include_file):
            include_file = os.path.join(self.seek_directory, include_file)
        snippet_maker = parameters.group(2)
        with open(include_file) as file_content:
            if not snippet_maker:
                included = file_content.read()
            else:
                included = self.truncate_to_part_between_maker(snippet_maker, file_content)
                # TODO: factor this out as a parameter
            return "~~~ {.scala}\n" + included + "\n~~~"

    def truncate_to_part_between_maker(self, marker, file_content):
        included = []
        including = False
        for line in file_content:
            if marker in line and including:
                return "\n".join(included)
            if including:
                included.append(line)
            if marker in line and not including:
                including = True
        return "\n".join(included)


SLIDES_PATH = 'slides' + os.sep
MARKDOWN_EXTRAS = ['extra', 'codehilite', CodeSnippets(os.getcwd())]
SLIDES = []

def preBuild(site):
    global SLIDES

    # Build all the slides
    for page in site.pages():
        if page.path.startswith(SLIDES_PATH):

            # TODO: Skip non html slides for obious reasons

            # Build a context for each slide
            slide_meta_data = {}
            slide_meta_data["title"] = "-".join(page.path.split("-")[1:])
            slide_meta_data["path"] = page.path
            page_content = open(page.paths['full']).read()
            page_directory = os.path.dirname(page.paths['full'])
            if page.path.endswith(".md"):
                slide_meta_data["markdown_content"] = markdown(page_content, ['extra', 'codehilite', CodeSnippets(page_directory)])

            SLIDES.append(slide_meta_data)

    # Sort the slides by pathname
    SLIDES = sorted(SLIDES, key=lambda x: x['path'])


def preBuildPage(site, page, context, data):
    """
    Add the list of slides to every page context so we can
    access them from wherever on the site.
    """
    context['slides'] = SLIDES

    return context, data
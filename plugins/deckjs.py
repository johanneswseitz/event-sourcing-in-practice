import os
import datetime
import logging
from markdown import markdown
import re

SLIDES_PATH = 'slides' + os.sep
SLIDES = []

from markdown.preprocessors import Preprocessor
from markdown.extensions import Extension
import re

class CodeSnippets(Extension):
    def extendMarkdown(self, md, md_globals):
        md.preprocessors.add('code_snippets', CodeSnippetIncludingPreProcessor(), '_begin')

class CodeSnippetIncludingPreProcessor(Preprocessor):
    def __init__(self):
        self.satement_replacers = [CodeIncludeSatementReplacer()]

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

    def __init__(self):
        self.include_statement = re.compile(r"@(\(([^\)]*)\))?\[([^\]]*)\]")

    def replaces(self, line):
        return self.include_statement.match(line) != None

    def replacement_for(self, line):
        parameters = self.include_statement.search(line)
        include_file = parameters.group(3)
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
            if page.path.endswith(".md"):
                slide_meta_data["markdown_content"] = markdown(page_content, ['extra', 'codehilite', CodeSnippets()])

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
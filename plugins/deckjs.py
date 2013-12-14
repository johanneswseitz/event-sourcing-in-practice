import os
import datetime
import logging
from markdown import markdown
import re

SLIDES_PATH = 'slides' + os.sep
SLIDES = []

from markdown.preprocessors import Preprocessor
from markdown.extensions import Extension

class CodeSampleIncludeExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        # Insert instance of 'mypattern' before 'references' pattern
        md.preprocessors.add('codesampleInclude', CodeSampleIncludingPreProcessor(), '_begin')

class CodeSampleIncludingPreProcessor(Preprocessor):
    def __init__(self):
        self.pattern = re.compile(r'\#include\(([^\)]*)\)')
        assert self.pattern.match("#include(foobar.txt)")

    def run(self, lines):
        new_lines = []
        for line in lines:
            m = self.pattern.search(line)
            if m:
                filename = m.group(1)
                new_lines.append("OMG FILE INCLUDE!!! " + filename)
            else:
                new_lines.append(line)
        return new_lines

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
                slide_meta_data["markdown_content"] = markdown(page_content, ['extra', CodeSampleIncludeExtension()])

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
import os
import datetime
import logging
from markdown import markdown
import re

SLIDES_PATH = 'slides' + os.sep
SLIDES = []

from markdown.preprocessors import Preprocessor
from markdown.extensions import Extension


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
                slide_meta_data["markdown_content"] = markdown(page_content, ['extra', 'codehilite', CodeSampleIncludeExtension()])

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
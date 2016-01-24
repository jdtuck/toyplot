# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from behave import *

import os
import sys

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

copyright_notice = """# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

"""

@given(u'the Toyplot sources.')
def step_impl(context):
    context.sources = []
    for directory, subdirectories, filenames in os.walk(root_dir):
        for filename in filenames:
            if os.path.splitext(filename)[1] not in [".py"]:
                continue
            if os.path.basename(directory) == "design" and filename == "decodegraphics.py":
                continue
            if os.path.basename(directory) == "_test":
                continue

            context.sources.append(os.path.join(directory, filename))
    context.sources = sorted(context.sources)

@then(u'all sources must contain a copyright notice.')
def step_impl(context):
    for source in context.sources:
        with open(source, "r") as stream:
            if not stream.read().startswith(copyright_notice):
                raise AssertionError("%s missing copyright notice." % source)


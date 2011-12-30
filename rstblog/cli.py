# -*- coding: utf-8 -*-
"""
    rstblog.cli
    ~~~~~~~~~~~

    The command line interface

    :copyright: (c) 2010 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""
from __future__ import with_statement
import sys
import os
from rstblog.config import Config
from rstblog.builder import Builder


def get_builder(project_folder):
    """Runs the builder for the given project folder."""
    config_filename = os.path.join(project_folder, 'config.yml')
    config = Config()
    if not os.path.isfile(config_filename):
        raise ValueError('root config file "%s" is required' % config_filename)
    with open(config_filename) as data:
        config = config.add_from_file(data)
    return Builder(project_folder, config)

def _check_args(expected_args, usage):
    """Check if the number of arguments falls within given interval.

    Print usage otherwise.
    """
    if len(sys.argv) not in range(1, expected_args+1):
        print >> sys.stderr, 'usage: %s' % usage
        sys.exit(1)

def build():
    """build the blog"""

    _check_args(2, 'rstblog-build [<folder>]')

    if len(sys.argv) == 2:
        folder = sys.argv[1]
    else:
        folder = os.getcwd()

    get_builder(folder).run()

def serve():
    """serve the blog locally"""

    _check_args(2, 'rstblog-serve [<folder>]')

    if len(sys.argv) == 2:
        folder = sys.argv[1]
    else:
        folder = os.getcwd()

    get_builder(folder).debug_serve()

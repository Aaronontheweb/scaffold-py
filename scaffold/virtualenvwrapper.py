#!/usr/bin/env python
# encoding: utf-8
#

"""
Hook to call pyscaffold automatically though virtualenvwrapper_.
when create a new project using the template `base`::

    $ mkproject -t base

.. _virtualenvwrapper: http://virtualenvwrapper.readthedocs.org
"""

import logging
import subprocess

log = logging.getLogger('scaffold')


def template(args):
    project = args[0]
    log.info('Running "pyscaffold -p %s"', project)
    subprocess.check_call(['pyscaffold', '-p', project, '-d', '..'])

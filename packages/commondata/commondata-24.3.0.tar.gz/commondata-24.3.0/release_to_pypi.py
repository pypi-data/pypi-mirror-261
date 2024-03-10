#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Copyright 2024 Rumma & Ko Ltd
# License: GNU Affero General Public License v3 (see file COPYING for details)

import build

python -m build
twine upload dist/*

@click.command()
@click.option("--batch", "-b", default=False, help="Whether to suppress any interactive questions.")
def main(batch):

if __name__ == '__main__':
    main()

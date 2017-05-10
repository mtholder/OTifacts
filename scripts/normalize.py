#!/usr/bin/env python
"""Pre-commit hook to normalize formatting of resources under version
control.
"""
from __future__ import print_function
import codecs
import json
import sys
import os

def normalize_json(fp):
    with codecs.open(fp, 'rU', encoding='utf-8') as inp:
        obj = json.load(inp)
    with codecs.open(fp, 'w', encoding='utf-8') as outp:
        json.dump(obj, outp,
                  indent=2,
                  separators=(',', ': '),
                  sort_keys=True)

if __name__ == '__main__':
    scripts_dir, script_name = os.path.split(sys.argv[0])
    top_dir = os.path.split(os.path.abspath(scripts_dir))[0]
    os.chdir(top_dir)
    is_first = True
    for dirpath, dirname, filenames in os.walk(top_dir):
        if is_first:
            is_first = False
            for skip in ['.git', 'references', 'scripts']:
                try:
                    dirname.remove(skip)
                except:
                    pass
        else:
            for filename in filenames:
                if filename.endswith('.json'):
                    path = os.path.join(dirpath, filename)
                    normalize_json(path)
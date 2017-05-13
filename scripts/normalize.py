#!/usr/bin/env python
"""Pre-commit hook to normalize formatting of resources under version
control.
"""
from __future__ import print_function
from peyotl import find_otifacts_json_filepaths, write_as_json
import codecs
import json
import sys
import os


def normalize_bibtex(fp):
    import bibtexparser
    from bibtexparser.bibdatabase import BibDatabase
    from bibtexparser.bwriter import BibTexWriter
    with codecs.open(fp, 'rU', encoding='utf-8') as inp:
        lib_as_str = inp.read()
    library = bibtexparser.loads(lib_as_str)
    d = {}
    for el in library.entries:
        bibtex_key = el['ID']
        if bibtex_key in d:
            raise RuntimeError('BibTeX key "{}" repeated'.format(bibtex_key))
        d[bibtex_key] = el
    sorted_ids = d.keys()
    sorted_ids.sort()
    sdb = BibDatabase()
    sdb.entries = [d[i] for i in sorted_ids]
    writer = BibTexWriter()
    with codecs.open(fp, 'w', encoding='utf-8') as out:
        out.write(writer.write(sdb))
    # finally we obliterate fields related to when we wrote this record
    with codecs.open(fp, 'rU', encoding='utf-8') as inp:
        lines = inp.readlines()
    with codecs.open(fp, 'w', encoding='utf-8') as out:
        for line in lines:
            ls = line.strip()
            if ls.startswith('owner =') or ls.startswith('timestamp ='):
                continue
            out.write(line)
    return d


def normalize_json(fp, refs):
    with codecs.open(fp, 'rU', encoding='utf-8') as inp:
        try:
            obj = json.load(inp)
        except:
            sys.stderr.write('Could not read "{}"'.format(fp))
            raise
    for v in obj.values():
        ref_list = v.get('references', [])
        for r in ref_list:
            if r not in refs:
                raise RuntimeError('Unknown reference key "{}"'.format(r))
    write_as_json(obj, fp, indent=2, separators=(',', ': '), sort_keys=True)


def main(top_dir):
    os.chdir(top_dir)
    bib_tex_fp = os.path.join(top_dir, 'references', 'OTifacts.bib')
    references_dict = normalize_bibtex(bib_tex_fp)
    for path in find_otifacts_json_filepaths(top_dir):
        normalize_json(path, references_dict)

if __name__ == '__main__':
    scripts_dir, script_name = os.path.split(sys.argv[0])
    top_directory = os.path.split(os.path.abspath(scripts_dir))[0]
    main(top_directory)

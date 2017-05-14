#!/usr/bin/env python
"""Pre-commit hook to normalize formatting of resources under version
control.
"""
from __future__ import print_function
from peyotl import read_all_otifacts, partition_otifacts_by_root_element
import codecs
import json
import sys
import os

def summarize_otifact_schema(res_dict, out):
    by_root = partition_otifacts_by_root_element(res_dict)
    by_rt = {}
    for k, root_obj in by_root.items():
        o = root_obj[k]
        by_rt.setdefault(o['resource_type'], []).append(k)
    rtk = list(by_rt.keys())
    rtk.sort()
    # known_to_have_uniq_vals = frozenset(['url', 'version', 'latest_download_url', 'maintainer'])
    common = frozenset(['date', 'url', 'version', 'format', 'schema'])
    out.write('resource_type: {}}}\n'.format('|'. join(rtk)))
    out.write("Keys that are possible to any resource type include:\n" \
              "  date: YYYY or YYYY-MM-DD\n" \
              "  version: string\n" \
              "  url: \n" \
              "  format or package_convention: for describing the archive format\n" \
              "    format: gzip|zip|tar+gzip|text\n" \
              "  schema: to describe the data representation form of the unpacked artifact.\n" \
              "    schema: IRMNG DwC|NCBI taxonomy|OTT|http://rs.tdwg.org/dwc/|newick|silva fasta|propinquity tree|OTT ID CSV\n" \
              "The following is a list of other keys found in different resource types:\n"
              )

    for rt in rtk:
        res_obj_keys_to_valset = {}
        res_obj_keys_to_num = {}
        keys_of_this_type = by_rt[rt]
        for res_id in keys_of_this_type:
            res_obj_dict = by_root[res_id]
            for k, v in res_obj_dict.items():
                # print('v = {}'.format(v))
                for vk, vv in v.items():
                    if vk == 'stats':
                        res_obj_keys_to_valset.setdefault(vk, set()).update(vv.keys())
                    else:
                        res_obj_keys_to_valset.setdefault(vk, set()).add(str(vv))
                    res_obj_keys_to_num[vk] = 1 + res_obj_keys_to_num.get(vk, 0)
        res_obj_keys = list(res_obj_keys_to_valset.keys())
        res_obj_keys.sort()
        out.write('resource_type: {}\n'.format(rt))
        for k in res_obj_keys:
            if k in common:
                continue
            if k in ['inherits_from', 'resource_type']:
                continue
            n_usages = res_obj_keys_to_num.get(k, 0)
            value_set = res_obj_keys_to_valset.get(k, set())
            if k == 'stats':
                lv = list(value_set)
                lv.sort()
                vm = ' => dict with keys: "{}"'.format('", "'.join(lv))
            elif n_usages > len(value_set):
                lv = list(value_set)
                lv.sort()
                vm = ' => "{}"'.format('", "'.join(lv))
            else:
                vm = " key with unique values"
            out.write('  {}{}\n'.format(k, vm))


def main(top_dir):
    res_dict = read_all_otifacts(top_dir)
    summarize_otifact_schema(res_dict, sys.stdout)

if __name__ == '__main__':
    scripts_dir, script_name = os.path.split(sys.argv[0])
    top_directory = os.path.split(os.path.abspath(scripts_dir))[0]
    main(top_directory)

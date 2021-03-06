# OTifacts
Repository of references to data artifacts created by or used by the 
  [Open Tree of Life project](https://tree.opentreeoflife.org).

The subdirectories contain JSON files that describe different resource.
The schema for these docs is under development, but the intent is to describe
    the resource in sufficient detail for a savvy app or user to know how to
    interact with it, and to store a few summary statistics as needed.

The repository is motivated by the fact that both 
    the work-in-progress [taxalotl](https://github.com/mtholder/taxalotl) repository and
    the current web app repository (see
   [synthesis.json](https://github.com/OpenTreeOfLife/opentree/blob/master/webapp/static/statistics/synthesis.json))
   need to manage basic data about Open Tree artifacts.
Mixing these stores of data with code clutters code changes with data changes.

Data to be stored here is intended to be slowly changing, and probably changed by 
    additions only (after the schema gets solidified).
So we don't need a fully editing interface for these files (like the git shards managed by phylesystem
    code in peyotl).
We can rely on GitHub APIs or pushes from privileged users/apps.

The scripts directory here is intended to only relate to scripts that validate or reformat
    data stored in this repository.

## License
Note that the [License.txt](./License.txt) and [CONTRIBUTORS.txt](./CONTRIBUTORS.txt)
only refer to the content of the repo - not the linked data. Check the linked cites for
further information about Licensing and authorship, if you are going to download data
from those sites.

The `references` field has keys that refer to the BibTeX keys of entries in the 
[references/OTifacts.bib](./references/OTifacts.bib) file to assist in citations.

The `license_url` and `license_of_tou_info` fields are intended to store a link (former)
or text (latter) pertaining to the license info URLs or terms of use statements.
Certainly check those links, if you are going to download information from those cites,
but do due diligence regardless as the info in these files may not be up-to-date.


## Scripts

    virtualenv env
    source env/bin/activate
    pip install bibtexparser

## References
BibTex


## Schema


  * `package_convention` of `propinquity pipeline v1` means: look for the 
    tar+gz archive of the full output at:
    https://files.opentreeoflife.org/synthesis/opentree{#}/opentree{#}_output.tgz
    and the tree slice of that output at:
    https://files.opentreeoflife.org/synthesis/opentree{#}/opentree{#}_tree.tgz
    where `{#}` is a placeholder for the version string.
    
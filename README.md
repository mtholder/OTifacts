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



## Scripts

    virtualenv env
    source env/bin/activate
    pip install bibtexparser

## References
BibTex


## Schema


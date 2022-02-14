"""
script to upload to conda :)
Should be run from root of directory
Requirements: 
- Install anaconda
- Run `conda install anaconda`
- `anaconda login`
- `conda build . channel`
Then from the output, use this:
- conda convert /Users/jacky.wong/opt/anaconda3/conda-bld/osx-64/relevanceai-0.28.0-py39_0.tar.bz2 -p all -o channel

"""

import os
from pathlib import Path

# os.system("conda build .")

# from observing the outputs, these seem to be the main file formats
for fn in (
    list(Path("channel").rglob("*.whl"))
    + list(Path("channel").rglob("*tar.gz"))
    + list(Path("channel").rglob("*.bz2"))
):
    print(fn)
    cmd = f"anaconda upload -u relevance {fn}"
    print(cmd)
    os.system(cmd)


Source code for the Skin and Bone project
-----------------------------------------

More information about this project can be found here: https://skin-and-bone-in-london-1760-1901.github.io/

The code in this repository is intended to run inside a python virtual environment. To create this environment, run the following commands in a UNIX-like shell:

python3 -m venv .venv
source .venv/bin/activate
pip install -U openpyxl
pip install -U tqdm

# Enter the python virtual environment (if not already in it, see above).
source ../dhids/.venv/bin/activate

# Generate data/outputs/dp_injury.xlsx and data/outputs/dp_person.xlsx
# This script uses json files created by the digital panopticon project.
# It uses the files in data/lookups to identify and classify the injuries described in the records.
python python/dp_injury.py

# Generate data/outputs/hp_injury.xlsx and data/outputs/hp_person.xlsx
# This script uses xlsx files of hospital data.
# It also uses the files in data/lookups to identify and classify the injuries described in the records.
python python/hp_injury.py

# Generate data/outputs/os_injury.xlsx and data/outputs/os_person.xlsx
# This script uses xlsx files of osteology data.
# It also uses the files in data/lookups to identify and classify the injuries described in the records.
python python/os_injury.py


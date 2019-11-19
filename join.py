import csv


def strip_name(bacteria):
    """Remove the double underscores from each part of the given bacteria name"""
    return ";".join([part[part.index("__") + 2:].strip() for part in bacteria.split(";")])


# Open metadata file and add contents to a list of rows of values
bacteria_data = []
with open("metadata/level-6 (2).csv") as f:
    for row in csv.reader(f, quotechar='|'):
        bacteria_data.append(row)

# Open inhibitory file and add contents to a list of rows of values
inhibitory_data = []
with open("code/anti-db-bacterial-metadata.txt") as f:
    for row in csv.reader(f, delimiter='\t', quotechar='|'):
        inhibitory_data.append(row)

bacteria_header = bacteria_data[0]  # First row is header info (column names)
# Remove rows which are not specific to skin
bacteria_data = [row for row in bacteria_data if row[bacteria_header.index("body_site")] == "Skin"]
# Find the numbers for columns which contain bacteria counts
bacteria_indices = [i for i, bacteria in enumerate(bacteria_header) if bacteria.startswith("D_")]

inhibitory_header = inhibitory_data[0]  # First row is header info


inhibitory_bacteria = set()
for row in inhibitory_data[1:]:  # skip header row
    bacteria = row[inhibitory_header.index("Uclust_taxonomy")]  # get the bacteria name (at the index of the Uclust_taxonomy in the header row) in the current row 
    if bacteria == "Unassigned":
        continue  # skip to next bacteria
    inhibitory = row[inhibitory_header.index("Bd_inhibition")] == "inhibitory"  # determine whether bacteria is listed as "inhibitory" in "Bd_inhibition" column
    if not inhibitory:
        continue  # skip if not
    inhibitory_bacteria.add(strip_name(bacteria))  # strip the bacteria's name and add to the set

frog_bacteria = {}
for i in bacteria_indices:
    bacteria = strip_name(bacteria_header[i])
    if bacteria in inhibitory_bacteria:  # add all bacteria in the frog file if inhibitory
        frog_bacteria[bacteria] = i  # set the corresponding value to the row index of the bacteria in the file

# For each row in the bacteria file, assign the row num to the corresponding species name
frog_species = {row[bacteria_header.index("species name")]: num for num, row in enumerate(bacteria_data)}

# for each frog, create a dict of each bacteria and the amount present for the frog
# i.e. {frog1: {bact1: amount, bact2: amount}, frog2: {bact1: amount, bact2:amount}}
present_bacteria = {}
for frog in frog_species:
    current_bacteria = {}
    bacteria_amounts = bacteria_data[frog_species[frog]]
    for bacteria in frog_bacteria:
        bacteria_num = frog_bacteria[bacteria]
        current_bacteria[bacteria] = float(bacteria_amounts[bacteria_num])

    present_bacteria[frog] = current_bacteria


# Create list of rows for output
output = []
# add header row
output.append(["bacteria"] + list(present_bacteria.keys()))

for bacteria in frog_bacteria:
    # Create row of bacteria amounts for each bacteria
    row = [bacteria]
    for frog in present_bacteria:
        row.append(present_bacteria[frog][bacteria])
    output.append(row)

print(output)

# output to tsvs
with open("joined.tsv", "w") as f:
    ofile = csv.writer(f, delimiter='\t')
    ofile.writerows(output)
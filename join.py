import csv


def strip_name(bacteria):
    return ";".join([part[part.index("__") + 2:].strip() for part in bacteria.split(";")])


bacteria_data = []
with open("metadata/level-6 (2).csv") as f:
    for row in csv.reader(f, quotechar='|'):
        bacteria_data.append(row)

inhibitory_data = []
with open("code/anti-db-bacterial-metadata.txt") as f:
    for row in csv.reader(f, delimiter='\t', quotechar='|'):
        inhibitory_data.append(row)

bacteria_header = bacteria_data[0]
bacteria_data = [row for row in bacteria_data if row[bacteria_header.index("body_site")] == "Skin"]
bacteria_indices = [i for i, bacteria in enumerate(bacteria_header) if bacteria.startswith("D_")]

inhibitory_header = inhibitory_data[0]


inhibitory_bacteria = set()
for row in inhibitory_data[1:]:
    bacteria = row[inhibitory_header.index("Uclust_taxonomy")]
    if bacteria == "Unassigned":
        continue
    inhibitory = row[inhibitory_header.index("Bd_inhibition")] == "inhibitory"
    if not inhibitory:
        continue
    inhibitory_bacteria.add(strip_name(bacteria))

frog_bacteria = {}
for i in bacteria_indices:
    bacteria = strip_name(bacteria_header[i])
    if bacteria in inhibitory_bacteria:
        frog_bacteria[bacteria] = i

frog_species = {row[bacteria_header.index("species name")]: num for num, row in enumerate(bacteria_data)}
present_bacteria = {}
for frog in frog_species:
    current_bacteria = {}
    bacteria_amounts = bacteria_data[frog_species[frog]]
    for bacteria in frog_bacteria:
        bacteria_num = frog_bacteria[bacteria]
        current_bacteria[bacteria] = float(bacteria_amounts[bacteria_num])

    present_bacteria[frog] = current_bacteria


output = []
output.append(["bacteria"] + list(present_bacteria.keys()))
for bacteria in frog_bacteria:
    row = [bacteria]
    for frog in present_bacteria:
        row.append(present_bacteria[frog][bacteria])
    output.append(row)

print(output)

with open("joined.csv", "w") as f:
    ofile = csv.writer(f)
    ofile.writerows(output)
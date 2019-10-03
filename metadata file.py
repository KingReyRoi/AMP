#!/usr/bin/python
import os

names = {}

with open("code/Sequencing samples  - All samples.tsv") as f:
    for line in f.read().split("\n")[10:]:
        num, name = line.split("\t")[:2]
        names[num] = name

os.chdir("/Users/King/Desktop/Sikes_research/test/Sequences")

with open("/Users/King/Desktop/Sikes_research/qiime/code/output.tsv", "a") as f_output:
    for file_name in filter(lambda f: f.endswith(".gz") and "R1" in f, os.listdir()):
        num = file_name.split("-")[0]
        prefix = file_name.split("_")[0]
        name = names[num]
        f_output.write(f"{prefix}\t{name}\n")

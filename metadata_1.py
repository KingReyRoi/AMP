#!/usr/bin/python
import os

names = {}

with open("/Users/King/Desktop/Sikes_research/test/Caramoan collections July-Aug2018.RMB 25072–.25786.22Aug2018.txt") as f:
    for line in f.read().split("\n"):
        num, name = line.split("\t")[:1][4:]
        names[num] = name

os.chdir("/Users/King/Desktop/Sikes_research/test/Sequences")

with open("/Users/King/Desktop/Sikes_research/qiime/code/output.tsv", "a") as f_output1:
    for file_name in filter(lambda f: f.endswith(".gz") and "R1" in f, os.listdir()):
        num = file_name.split("-")[0]
        prefix = file_name.split("_")[0]
        name = names[num]
        f_output1.write(f"{prefix}\t{name}\n")
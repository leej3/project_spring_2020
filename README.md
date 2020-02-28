# project_spring_2020

[![CircleCI](https://circleci.com/gh/biof309/project_spring_2020/tree/master.svg?style=shield)](https://circleci.com/gh/biof309/project_spring_2020/tree/master)

For my final project, I plan to create a script that will find overlapping copy number variants (CNV) across multiple individuals’ genomes. The script will scan large comma delineated files to compare chromosome number (the chromosome on which the CNV is located), CNV start position, CNV stop location, and CNV type (deletion vs duplication). The script must also accept a value for the minimum length for regions of interest (i.e. 1 kb) and a value defining the minimum length of an overlap (i.e. a CNV found in two separate genomes having a start and stop position within 25 basepairs of the other). It then will create an output file containing the chromosome number, start position, stop position, and CNV type of each shared CNV.

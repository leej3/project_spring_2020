#!/usr/bin/env python
import sys, getopt
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

##To call this program "python Annotate.py <locus_file> <annotation_paths_file> <output_file_name>
##Make sure the locus file has a header of "Chr" and "pos"
##Make sure the annotation file doesn't have any empty lines (especially at the end)


def main(locus_file, ann_paths_file, output, xlab):
    locus = open(locus_file, "r") # open locus file
    header = locus.readline() #save the header line
    header = header.strip().split()
    chr_i = header.index("Chr")  #Saves the index of chr and pos
    pos_i = header.index("pos")
    rsid_i = header.index("RSID")
    chr = [] #keep track of chr for each snp
    pos = [] #keep track of position of each snp
    rsid = [] #keep track of rsid of each snp
    for line in locus.readlines(): # gather the position of all snps in the locus
        cols = line.split()
        chr.append(str(cols[chr_i])) #keep the chr numbers as strings
        pos.append(int(cols[pos_i])) # keep the positions as ints
        rsid.append(str(cols[rsid_i]))
    locus.close()
    out_header = [] # create header for the output file, which will be the names of the annotation files
    snps = np.zeros((len(chr), len(open(ann_paths_file).readlines())), dtype=np.int16) #Initialize matrix with zeros (#snps x #annotations)
    paths = open(ann_paths_file, "r") # open annotation paths file
    ann_i = 0 #annotation file index
    for line in paths.readlines():  #iterate through annotation files, storing each line in the file as a separate element of a new list
        ann = open(line.strip(),"r")
        filename = os.path.basename(line.strip()) #get the filename for the header of output
        filename = filename[:-4] #remove the extension of the filename. It removes the last 4 chars, which are .bed
        out_header.append(filename)
        for line in ann.readlines(): #check every line in annotation file
            line = line.split()
            line[0] =line[0][3:] #remove the 'chr' from the chr column
                #lets iterate through snps at each line in annotation file
            for i in range(len(chr)):
                if(line[0] == chr[i] and int(line[1]) <= pos[i] <= int(line[2])):
                    snps[i,ann_i] = 1 #if the snp is within an annotation peak, change that snp matrix entry to 1
        ann_i += 1
        ann.close()

    snps_header = pd.DataFrame(snps,columns = out_header)
    rsid_arr = np.asarray(rsid)
    snps_header.insert(0,'SNP',rsid_arr)
    np.savetxt(output, snps_header, fmt = "%s", comments ='')
    paths.close()

    id_labels = snps_header.columns[1:]

    id_matrix = np.array(snps_header[id_labels].values, dtype=float).T 

    SNP = (snps_header['SNP']) 

    fig, ax = plt.subplots() 
    mat = ax.imshow(id_matrix, cmap='GnBu', interpolation='nearest') 
    plt.yticks(range(id_matrix.shape[0]), id_labels) 
    plt.xticks(range(id_matrix.shape[1]), SNP)
    plt.xticks(rotation=45)
    plt.xlabel(xlab)
    plt.savefig(fname = output + '.pdf', format = 'pdf', bbox_inches='tight')

    return header	
	
if __name__=="__main__":
	main(sys.argv[1], sys.argv[2], sys.argv[3],sys.argv[4])

	


def main():

    import os
    import pandas as pd
    from matplotlib import pyplot as plt
    import seaborn as sns
    from bk_packages.basic_methods import *
    
    DATA_FOLDER="/Users/kangb3/github/project_spring_2020_dup/data/import/"
    EXP_FNAME = os.path.join(DATA_FOLDER, "exprs_mtx.txt")
    META_FNAME = os.path.join(DATA_FOLDER, "metatable.txt")
    
    #### Read Meta Files - read as list of lists
    meta = []
    with open(META_FNAME) as f_obj:
        for line in f_obj:
            res = line.replace('"','').strip('\n').split('\t')
            meta.append(res)
    
    ### Insert one element in the 1th list of the meta data
    meta[0].insert(0,'rowname')
    
    ### Read matrix file - read as list of lists
    mtx = []
    with open(EXP_FNAME) as f_obj:
        for line in f_obj:
            res = line.replace('"','').strip('\n').split('\t')
            mtx.append(res)
    
    ### Insert one element in the 1th list of the mtx
    mtx[0].insert(0,'gene')

if __name__ == '__main__':
    main()

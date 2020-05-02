
def clusTocell_dic_generator(meta):
    """Return {cluster:cell.ids} dictionary """
    temp = [meta[i][2] for i in range(0,len(meta))] # extract cell cluster info
    unique_cluster = unique(temp[1:])         # take unique cluster info
    unique_cluster = sorted(unique_cluster)
    
    meta_by_cluster = []
    meta_dic = {}
    
    ## group cell.ids based on their cluster
    for cluster in unique_cluster:
        index = [i for i, n in enumerate(temp) if n == cluster] # extract the indices of rows in a given cluster
        a = [meta[i][1:3] for i in index] # using the indices, extract cell.id and assigned cluster info.
        meta_by_cluster.append(a)
    
    # convert the list acquired above to dictionary with the cluster as keys
    for j in range(0, len(unique_cluster)):
        meta_dic[ meta_by_cluster[j][0][1] ] = [meta_by_cluster[j][i][0] for i in range(0, len(meta_by_cluster[j]))]
    
    return(meta_dic)

def cellTogene_dic_generator(x):
    """Apply T-transformation and convert the list of lists to Dictionary"""
    """with cell.id as keys and gene expression as value"""
    mtx_t = t(x)
    mtx_dic = {}
    
    for line in mtx_t:
        mtx_dic[line[0]] = line[1:]
    
    return(mtx_dic)

def random_selector(meta_dic, num_to_select = 20):
    
    """Random selection of cell.ids from each cluster"""
    
    import random
    import math
        
    dic_random_items = {}
    num_to_select = num_to_select  # this will be determined by user.
    
    for key in meta_dic.keys():
        
        clust_cell_ids = meta_dic[key].copy()
        
        # determine the number of cycle to run in the following loop.
        if len(meta_dic[key]) < num_to_select:
            print("Number of items to select exceeds the number of items in the list.")
            print("Remember this is random selection without replacement.")
            cycle_to_run = math.floor(len(meta_dic[key])/num_to_select)
        elif len(meta_dic[key])%num_to_select == 0:
            cycle_to_run = int(len(meta_dic[key])/num_to_select)
        else:
            cycle_to_run = math.ceil(len(meta_dic[key])/num_to_select)
    
        for i in range(0, cycle_to_run): # random sampling from the given list without replacement
            if len(clust_cell_ids) > num_to_select:
                a = random.sample(clust_cell_ids, num_to_select)
                dic_random_items[ a[0] ] = a  # takes the first cell.id among selected ones as a key.
                [clust_cell_ids.remove(a[i]) for i in range(0,len(a))] # selected cell.ids are removed from the dic.
            elif len(clust_cell_ids) < num_to_select: # the remaining cells are taken 
                a = clust_cell_ids
                dic_random_items[ a[0] ] = a
    
    return(dic_random_items)

def geneAverage(mtx_dic, dic_random_items):
    mtx_small = {}
    a = mtx_dic['gene'].copy()
    mtx_small['gene'] = a
    
    for key, values in dic_random_items.items():
        temp = []
        a = []
        for value in values:
            a = mtx_dic[ value ].copy()
            temp.append(convert_to_float(a))
        mtx_small[ key ] = rowMean(temp)
    
    [v.insert(0,k) for k, v in mtx_small.items()]
    temp_2 = [x for x in mtx_small.values()]
    
    final_mtx = []
    temp = t(temp_2)
    final_mtx = temp.copy()
    
    return(final_mtx)

def t(mtx):
    """T-transform the Input Matrix"""
    try:
        if type(mtx) is str: #if the input is str, raise exception.
            raise Exception('Error: the input should be a list of lists.')
        
        for i in range(0, len(mtx)):
            assert len(mtx[i]) == len(mtx[i-1]) # check whether each list has the same length.
        
        ## Execution code
        mtx_t = []
        for j in range(0, len(mtx[0])):
            mtx_t.append( [mtx[i][j] for i in range(0,len(mtx))] )
        return(mtx_t)
    
    except TypeError as detail: # Control TypeEorror.
        return ('Error: the input should be a list of lists.')
    except AssertionError as detail:
        return ('Error: length of the lists should be the same')

def convert_to_float(input_list):
    """Convert list of str to list of float"""
    try:
        list_float = [float(i) for i in input_list]
        return(list_float)
    except ValueError as detail:
        return ("input is not convertible to float.")

def unique(input_list):
    """Return unique value of the input list"""  
    try:
        # intilize a null list 
        unique_list = [] 
        # traverse for all elements 
        for x in input_list: 
            # check if exists in unique_list or not 
            if x not in unique_list: 
                unique_list.append(x)
        return(unique_list)
    except TypeError as detail:
        return ("int object is not iterable")

def rowSum(mtx):
    """Return all row-sums as a list"""
    try:
        for i in range(0, len(mtx)):
            assert len(mtx[i]) == len(mtx[i-1]) # check whether each list has the same length.
        
        res = list()
        for j in range(0, len(mtx[0])): 
            tmp = 0
            for i in range(0, len(mtx)): 
                tmp = tmp + mtx[i][j]
            res.append(tmp)
        return(res)
    
    except AssertionError as detail:
        return ('Length of lists is irregular or input format is wrong.')
    except TypeError as detail:
        return ('Undefined operand type')

def rowMean(mtx):
    """Return all row-sums as a list"""
    try:
        for i in range(0, len(mtx)):
            assert len(mtx[i]) == len(mtx[i-1]) # check whether each list has the same length.
        
        res = list()
        for j in range(0, len(mtx[0])): 
            tmp = 0
            for i in range(0, len(mtx)): 
                tmp = tmp + mtx[i][j]
            res.append(tmp/len(mtx))
        return(res)
    
    except AssertionError as detail:
        return ('Length of lists is irregular or input format is wrong.')
    except TypeError as detail:
        return ('Undefined operand type')

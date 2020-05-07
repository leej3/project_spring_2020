from project_code.annotation_plot import main

# read in test data
locus_file = 'chr5.cs.snps.txt'
ann_paths_file = 'peak.paths.txt'
output = 'test_output'
xlab = 'test_xlab'

def test_read_of_locus_file(): # Check that locus file has been formatted properly
    header = main(locus_file, ann_paths_file, output, xlab)
    assert header[0] == 'Chr'
    assert header[1] == 'pos'
    assert header[2] == 'RSID'
    
def test_read_of_ann_paths_file():
    ann = main(locus_file, ann_paths_file, output, xlab)
    assert ann[0] == 'Chr' #First element of header will be Chr as bedfiles are standardised format

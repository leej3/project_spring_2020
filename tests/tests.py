from project_code.annotation_plot import main

# read in test data
locus_file = 'chr5.cs.snps.txt'
ann_paths_file = 'peak.paths.txt'
output = 'test_output'
xlab = 'test_xlab'

def test_read_of_locus_file():
    header = main(locus_file, ann_paths_file, output, xlab)
    assert header[0] == 'Chr'
    
def test_read_of_ann_paths_file():
    ann = main(locus_file, ann_paths_file, output, xlab)
    assert ann[0] == 'Chr'

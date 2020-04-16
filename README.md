# Single Cell Random Drawing

This small python package will enable for users to randomly draw the indicated number of cells from individual cluster of scRNAseq data and average the gene expression value of the chosen cells.

# Input
  1. Expression matrix of scRNAseq (gene by cells)
  2. Metadata (cell ids and cluster or cell type info)

# The benefit of downsizing cells with averaging the exprssion levels of gene?
  1. downsizing itself reduce the calculation burden --> reducing calculation time
  2. Increase the resolution of differential gene expressin.

(e.g. assume that you have 400 cells in cluster 1 of your scRNAseq data, and if you set the number of cells to be chosen as 20, then 20 cells from cluster 1 of your data will be randomly and repeatedly selected with no replacement. This process will downsize the cluster 1 from 400 cells to 20 cells with better gene expression resolution.)

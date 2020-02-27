
**I work with tetrads and I work on scoring them for drug markers.

-	I want to be able to upload an excel file consisting of sample numbers and 1s and 0s and have the package put this excel in a folder of its own
-	Want the package to re-arrange my data within the excel according to the parameters of 1s and 0s that I give it
-	I want the package to be able to choose the sample names that have the correct 1/0 combination that I am looking for
-	For example if I have a sample that grows on Kan and Hyg but not Nat, it would be 1,1,0 respectively
-	I want the package to create a second document that contains a list of the sample names that correspond to the parameters I want
-	This list should be organized based on the sample number (ex. 1,2,3,4,5,6,etc.)
-	I want the package to name this document “samples with correct markers”

**An example of this would be:

-	Let’s say that I wanted spores that grow on URA, KAN, and ARG, but not on HYG or NAT
-	I have an excel document that has spores listed as rows, and the markers listed as the columns
-	It would take my excel file and put it in a new folder labeled “tetrad dissection 1”
-	Then, within the excel document, if I were to type in the program like “Ura, 1, Kan, 1, Arg, 1, Hyg, 0, Nat, 0”, then it would sort through the file and find the rows that correspond to the samples that have this.  
-	Then it would take these sample names and put them in a separate document as a list
-	It would then label this new list as “samples with correct markers” and keep this list in the folder “tetrad dissection 1”

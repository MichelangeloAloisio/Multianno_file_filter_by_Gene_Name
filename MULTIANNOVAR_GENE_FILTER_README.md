# Multianno_file_filter_by_Gene_Name

INTRODUCTION

Today, in Genetic clinical diagnostic, Annovar is the most used tool to annotate exome or whole genome Variant Caller NGS output files. 
The Annovar output file is called Multianno.txt. Usually it is open with softwares as Microsof Excel and OpenOffice that permit to visualize 
the annotation file as TABLE and to apply filter to columns in order to facilitate Genetists in the discovery of the patient mutation.
While, despite their userfriendly approach, these software could not work with large files. Since both the Whole Genome and the Exome sequencing 
files usually are too large (about 400 Mb), we developed a filter with python3 programming language that permit to: 

1) Filter the GENE COLUMN of the muliannovar file by the GENE LIST file present in the folder (gene_list.csv).
Is possible to edit the gene list in gene_list.csv file based on the target gene panel desired. 

2) Edit the Order the column position 


GENE LIST to facilitate the clinical user to filter the Annovar output by a List of 
TARGET genes that could be change and choose 

DOWNLOAD  
Download the MULTIANNOVAR_FILTER_FOLDER and save it on Personal Computer.

MULTIANNOVAR_FILTER_FOLDER contents: 
1) MULTIANNOVAR.txt annovar output file, the user upload the file in the MULTIANNOVAR_GENE_FILTER_folder;
2) gene_list.cvs file that contains a LIST of the TARGET GENE PANEL to analyze; 
3) Column

DOWNLOAD  
Download the MULTIANNOVAR_GENE_FILTER folder and save on Personal Computer.




the Multiannovar.txt file could be too large expecially (also 400 Mb) in whole Genome or Exome one sequencig.
The Multianno_file_filter_by_Gene_Name is able to filter by GENE NAME the multianno files in order to:
1) Pass from Whole or Exome sequencing multiannovar file to a FILTERED TARGET Gene File 
Filter to extract a panel of target Genes from a Large Annovar annotation output file ('multianno.txt'). Moreover the   

#!/usr/bin/env python

#Developer contact mail: michelangelo.aloisio@burlo.trieste.it

####cose da fare 1) print file log 


#############################################################################################################
###################                                                                          ################
###################                       MULTIANNOVAR_GENE_FILTER.py                               ####################
###################                                                                          ################
#############################################################################################################


#############################################################################################################
################### SECTION 1:       START program:  IMPORT and PRINT DATE                     ################
#############################################################################################################
import datetime
import pandas as pd
Log_file_error=open('Log_file_ERROR.txt', 'wt')

BOLD = '\033[1m'
END = '\033[0m'

print( BOLD+'MULTIANNOVAR_GENE_FILTER pipeline'+END)
print('')
Log_file_error.write('MULTIANNOVAR_GENE_FILTER pipeline'+'\n')
Log_file_error.write('')

datetime_object = str(datetime.datetime.now()).split(' ') #DATE string added in the name of the OUTPUT FILES
date= str(datetime_object[0])
time=str(datetime_object[1]).split(':')[0]+':'+str(datetime_object[1]).split(':')[1]

print (BOLD+'START_TIME: ', date+' '+time+ END)
print('')
Log_file_error.write('START_TIME_'+ date+'\n')
Log_file_error.write('')

#############################################################################################################
################### SECTION 2:     UPLOAD COLUMN and GENE FILES                               ################
#############################################################################################################

Gene_filter_file='genes_list.csv' ###If you want to change the name of the Gene list file change the name here
Column_filter_file='lista_colonna_ordine.csv'###If you want to change the name of theCOLUMN list file change the name here

Log_file_error.write('UPLOADED FILES '+'\n')
Log_file_error.write(Gene_filter_file+'\n')
Log_file_error.write(Column_filter_file+'\n')

#############################################################################################################
################### SECTION 3:    Ask the name and UPLOAD the MULTIANNO FILE                     ################
#############################################################################################################

CONTROL_input_1=input(BOLD+'1) Add the ANNOVAR out File in the current folder and press Enter '+END)
CTRL=False
while CTRL==False:
	try:
		nome_file_annotazioni= input(BOLD+'''Insert the Name of the Annovar output file (ex. patient1_multianno.txt) and Press Enter '''+END)
		CTRL_right_file_name=open(nome_file_annotazioni)
	except FileNotFoundError:
		CTRL=False
		print(BOLD+'Name Error'+END)
		print(BOLD+'The file does not exist in the folder'+END)
		print(BOLD+'Try Again'+END)
		error_stp=input(BOLD+'press enter to go on'+END)
		print('')
	else:
		CTRL=True
		print(BOLD+'OK'+END)
		print('')
Log_file_error.write('nome_file_annotazioni')
Log_file_error.write('')

#############################################################################################################
################### SECTION 4:  3 CONTROLS TO CHECK THE RIGHT FILE NAMES in the FOLDER       ################
#############################################################################################################

###CONTROL_1
if nome_file_annotazioni==Gene_filter_file:
	print (BOLD+'Error: Annotation_file and Gene_List_file have the same name'+END)
	print (BOLD+'Restart Again'+END)
	exit()
###CONTROL_2
if nome_file_annotazioni==Column_filter_file:
	print (BOLD+'Error: Annotation_file and Column_List_file have the same name'+END)
	print (BOLD+'Restart Again'+END)
	exit()
###CONTROL_3
if Gene_filter_file==Column_filter_file:
	print (BOLD+'Error: Gene_List_file and Column_List_file have the same name'+END)
	print (BOLD+'Restart Again'+END)
	exit()

#############################################################################################################
#################   SECTION 5:   CHECK IF GENE and COLUMN FILE NAMEs are in the FOLDER         ################
#############################################################################################################

CONTROL_input_2= input(BOLD+'2) Check if the file genes_list.csv is in the folder and press Enter'+END)
try:
	Gene_filter_file_open=open(Gene_filter_file, 'r')
except FileNotFoundError:
	print(BOLD+'File: genes_list.csv is NOT in the Folder. Please add it in folder and start again.'+END)
	print (BOLD+'Restart Again'+END)
	exit()
print (BOLD+'OK'+END)
print('')

CONTROL_input_3= input(BOLD+'3) Check if the file lista_colonna_ordine.csv is in the folder and press Enter'+END)
try:
	Column_filter_file_open=open(Column_filter_file, 'r')
except FileNotFoundError:
	print(BOLD+'File: lista_colonna_ordine.csv is NOT in the Folder. Please add it in folder and start again.'+END)
	print (BOLD+'Restart Again'+END)
	exit()
print (BOLD+'OK'+END)
print('')

#############################################################################################################
#################   SECTION 6:             FILTER COMPUTATIONAL CORE                         ################
#############################################################################################################


#####import column ordered list
tuple_t=()
diz_print=list(tuple_t)
for x in Column_filter_file_open:
	diz_print.append(int(x.strip())-1)

#####import Gene ordered list
Gene_filter_lista=[]
for x in Gene_filter_file_open:
	Gene_filter_lista.append(x.strip())
try:
	data=pd.read_csv(nome_file_annotazioni, sep='\t', header=0,)### Original Multiannovar file pandas dataframe
except ValueError:
	print(BOLD+'Error: Check the Multianno file name'+END)
	print (BOLD+'Restart Again'+END)
	exit()
data=data[data['Gene.refGene'].isin(Gene_filter_lista)] ### FILTERED by GENE Original Multiannovar dataframe
data_1=data.iloc[:,diz_print]                          ### Column POSITION MODIFIED  Multiannovar dataframe
data_1.to_csv('FILTERED_OUTPUT_'+nome_file_annotazioni+'.csv', sep='\t', na_rep=0, index=False)## PRINT TO FILE 

print(BOLD+'The file FILTERED_OUPUT.csv  is READY in the folder'+END)
print('')
print(BOLD+'''IMPORTANT
The FILTERED_OUPUT.csv is a TAB DELIMTED CSV file.
If You open it on Excel program:
 1) ENSURE to split columns ONLY by TAB (tabulation); 
 2) ENSURE that other split symbols are deactivated! '''+END)
print('')
print('')
print (BOLD+'Thank you!!!'+END)

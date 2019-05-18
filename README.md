# gene_list_extractor
Extract gene expression data which matches to custom gene list.

It is python codes and use "python gene_list_extractor.py -i input_gene_file -l gene_list_file -o output_file -c1 1 -c2 1" to run!

# File format
Example of input_gene_file is provided as gene_expression_data.txt. 

		sample1	sample2	sample3	sample4	sample5
	geneA	1	3	5.5	7	2
	geneB	100	267	55	79	62
	geneC	0.3	0.65	9.5	0.87	2.1
	geneD	205	356	78	67	2900
	geneE	1001	3001	5500	7001	2001
	geneF	2	2	2	2	2
	geneG	0.01	0.03	0.5	0.07	0.02

Example of gene_list_file is provided as gene_list.txt.

	geneA
	geneG
	geneI
	geneP
	geneW
	geneX

# Description of file format
 -h, --help            show this help message and exit
 
 -i INPUT, --input INPUT		input gene expression file name
 
 -l LIST, --list LIST		input gene list file name
 
 -o OUTPUT, --output OUTPUT		output file name
 
 -c1 COLUMN_INPUT, --column_input COLUMN_INPUT		column number; gene ID location in input gene expression file
 
 -c2 COLUMN_LIST, --column_list COLUMN_LIST		column number; gene ID location in gene list file

# Outcome

	NAME1	id1 250	B #from 2nd_line(students total scores and grade)
	NAME2	id2 231	C #from 2nd_line(students total scores and grade)

Setting of grades are A>=92%, 92%>A->88%, 88%>B+>=84%, 84%>B>=80%, 80%>B->=76%, 76%>C+>=72%, 72%>C>=68%, 68%>C->=64%, 64%>D+>=60, 60%>D>=56%, 56%>D->=52%, and F<52%.


# gene_list_extractor
Extract gene expression data which matches to custom gene list.

python gene_list_extractor.py -i input_gene_file -l gene_list_file -o output_file -c1 1 -c2 1

# File format
Example of input_file is provided as grades.txt. 

	Name	ID	quiz1	quiz2	quiz3	quiz4	exam1	exam2	journal_club	attendance	assignment	
	Points	total	10	10	10	10	100	100	20	20	20	
	NAME1	id1	5	6	7	8	99	80	20	20	10	
	NAME2	id2	5	7	7	9	96	78	12	17	5	

# Description of file format
Quizzes should locate first part of scores.

# Outcome

	NAME1	id1 250	B #from 2nd_line(students total scores and grade)
	NAME2	id2 231	C #from 2nd_line(students total scores and grade)

Setting of grades are A>=92%, 92%>A->88%, 88%>B+>=84%, 84%>B>=80%, 80%>B->=76%, 76%>C+>=72%, 72%>C>=68%, 68%>C->=64%, 64%>D+>=60, 60%>D>=56%, 56%>D->=52%, and F<52%.


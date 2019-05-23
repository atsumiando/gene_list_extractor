import argparse



parser = argparse.ArgumentParser(usage='python gene_list_extractor.py -i input_gene_file -l gene_list_file -o output_file', add_help=True,formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('-i','--input',help = 'input gene expression file name', required=True)
parser.add_argument('-l','--list',help = 'input gene list file name', required=True)
parser.add_argument('-o', '--output', help = 'output file name',default = "output")
parser.add_argument('-c1', '--column_input',help = 'default 1; column number in gene ID location in input gene expression file', type=int,default = 1)
parser.add_argument('-c2', '--column_list',help = 'default 1; column number in gene ID location in gene list file', type=int,default = 1)

args = parser.parse_args()


input_file_name = args.input 
list_file_name = args.list
output_file_name = args.output 
column_input = args.column_input 
column_list = args.column_list

def filename():
        with open(input_file_name, 'r') as sourcefile:#add your file name and separate data in lines
                list = sourcefile.read().splitlines()
                inputs, record = [], []
                for index in range(len(list)):
                        record = list[index].split('\t')
                        inputs.append(record)
	with open(list_file_name, 'r') as sourcefile2:#add your file name and separate data in lines
                list2 = sourcefile2.read().splitlines()
                inputs2, record2 = [], []
                for index2 in range(len(list2)):
                        record2 = list2[index2].split('\t')
                        inputs2.append(record2)
        with open(output_file_name, 'w' ) as sinkfile: #make new file
                for index in range(len(list)):
                	for index2 in range(len(list2)):
				if inputs[index][column_input-1] == inputs2[index2][column_list-1]:
                        		data = inputs[index]
                        		data_str= [str(x) for x in data]
                        		data_final ='\t'.join(str(e) for e in data_str)
                        		sinkfile.write(data_final +"\n")

filename()


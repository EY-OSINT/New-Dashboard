#FUNCTION THAT MERGES ANY NUMBER OF FILES INTO output_file concatinates them in queue.
def merge_files(file1,file2,file3,output_file):
    
    filenames = [file1, file2,file3,output_file ]
    with open(output_file, 'w') as outfile:
        for fname in filenames:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)
    return
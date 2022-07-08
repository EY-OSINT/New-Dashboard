#FUNCTION THAT MERGES ANY NUMBER OF FILES INTO output_file concatinates them in queue.
def merge_files(file1,file2,file3,output_file):
    
    filenames = [file1, file2,file3,output_file ]
    with open(output_file, 'w') as outfile:
        for fname in filenames:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)
    return
#Function that removes duplicate LINES from file to output_file
import os
def remove_duplicates(file,output_file):
    openFile = open(file, "r")
    writeFile = open(output_file, "w") 
    #Store traversed lines
    tmp = set() 
    for txtLine in openFile: 
    #Check new line
        if txtLine not in tmp: 
            writeFile.write(txtLine) 
    #Add new traversed line to tmp 
            tmp.add(txtLine)         
    openFile.close() 
    writeFile.close()  
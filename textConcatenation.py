# Combine all the text documents
import sys
import os

def textConcat(input_folder):
    files = os.listdir(input_folder)
    result = open("Reports_final_doc.txt", "w")
    for file in files:
        f = open(file, "r")
        for line in f:
            result.write(line)
        result.write("\n")
        f.close()
    result.close()
    print("Done.")
    
# Main
inp_folder = sys.argv[1]
textConcat(inp_folder)

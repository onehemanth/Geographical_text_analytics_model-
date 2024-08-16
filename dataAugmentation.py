# This is used to augment the data from all the annotation files
import json
import sys

def augmentData(file1, file2):
    result = open(file1)
    result_data = json.load(result)
    result.close()
    
    inFile = open(file2)
    inFile_data = json.load(inFile)
    inFile.close()
    
    for item in inFile_data["annotations"]:
        result_data["annotations"].append(item)
    
    # Save json
    save_file = open(file1, "w")  
    json.dump(result_data, save_file, indent = 0)  
    save_file.close() 
    print("Done.")


# Main 
file1 = sys.argv[1]
file2 = sys.argv[2]
print("Data gets augmented into {0}".format(file1))

augmentData(file1, file2)
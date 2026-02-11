from os import walk
from verify import validate_string, response_valid, VALID_BIN_RESPONSES, VALID_PRINT_OPTIONS, VALID_SEPARATORS
from save_to_file import save_to_file


def main():

    path = input("PLEASE INPUT THE PATH TO THE DESIRED DIRECTORY\n")
    type = ""
    console = True

    while(True):
        type = input("PLEASE INPUT THE DESIRED FILE TYPE\n")
        if(len(type) == 0 or type.lower() == "all"):
            type = "True"
            break
        if(type[0] == '.'):
            break
        print("ERROR: PROVIDED FILE TYPE IS INVALID.")

    remove_root = validate_string("DO YOU WITH TO INCLUDE THE ROOT? (Y/N)", VALID_BIN_RESPONSES, 'n', False, True)

    separator = validate_string("SEPARATE WITH A SPACE OR A NEW LINE?", VALID_SEPARATORS, 'n', " ", "\n")

    while(True):
        temp = input("DO YOU WISH TO PRINT TO THE CONSOLE OR A FILE? ").lower()
        if(not(response_valid(temp, VALID_PRINT_OPTIONS))):
            print("ERROR: INVALID RESPONSE INPUT")
            continue
        if(temp == "file"):
            console = False
        break

    print_progress = validate_string("DO YOU WISH TO PRINT OUT DIRECTORIES AND THEIR FILES AS THEY ARE FOUND? (Y/N)", VALID_BIN_RESPONSES, 'n', True, False)

    directoryPaths = []
    fileNames = []
    current_files = 0
    for (root,dirs,files) in walk(path,topdown=True):
        fileNames.append([x for x in files if (x.endswith(type) or type == "True")])
        if(len(fileNames[current_files]) > 0):
            directoryPaths.append(root)
            current_files+=1
        else:
            fileNames.pop()
            

            

    if(remove_root):
        for i in range(len(directoryPaths)):
            directoryPaths[i] = directoryPaths[i].replace(path, "", 1)
    out = ""
    for i in range(len(directoryPaths)):
        if(print_progress):
            print(directoryPaths[i]+":")
            print(fileNames[i])
            print()
        for j in range(len(fileNames[i])):
            out+=(directoryPaths[i]+"\\"+fileNames[i][j])
            if(j < (len(fileNames[i])-1) or i < (len(directoryPaths)-1)):
                out+=separator
    out = out.replace("\\", "/")
    if(console):
        print(out)
        return
    
    save_to_file(out)

    return



main()
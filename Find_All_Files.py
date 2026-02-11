from os import walk
import os.path


def response_valid(response, valid_responses):
    if(type(response) != str or (type(valid_responses) != tuple and type(valid_responses) != list)):
        return False
    for string in valid_responses:
        if(response == string):
            return True
    return False

def validate_string(msg, valid_responses, alternative_response, default_state, alternative_state):
    while(True):
        temp = input(msg+" ").lower()
        if(not(response_valid(temp, valid_responses))):
            print("ERROR: INVALID RESPONSE INPUT")
            continue
        if(temp[0] == alternative_response):
            return alternative_state
        return default_state

def main():
    VALID_BIN_RESPONSES = ("y", "n", "yes", "no")
    VALID_PRINT_OPTIONS = ("console", "file")
    VALID_SEPARATORS = ("space", "newline", "new line")
    path = input("PLEASE INPUT THE PATH TO THE DESIRED DIRECTORY\n").replace("/", "\\")
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

    separator = validate_string("SEPARATE WITH A SPACE OR A NEW LINE", VALID_SEPARATORS, 'n', " ", "\n")

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
        
    for i in range(len(directoryPaths)):
        if(print_progress):
            print(directoryPaths[i]+":")
            print(fileNames[i])
            print()

    if(console):
        print()
        return
    
    modify = False
    while(not(modify)):
        out_file = input("PLEASE INPUT THE NAME OF THE OUTPUT FILE: ")
        if(os.path.isfile(out_file)):
            print("FILE ALREADY EXISTS", " ")
            modify = validate_string("DO YOU WISH TO OVERWRITE IT? (Y/N)", VALID_BIN_RESPONSES, 'n', True, False)
        else:
            modify = True
    return



main()
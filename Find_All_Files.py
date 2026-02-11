from os import walk


def response_valid(response, valid_responses):
    if(type(response) != str or (type(valid_responses) != tuple and type(valid_responses) != list)):
        return False
    for string in valid_responses:
        if(response == string):
            return True
    return False

def main():
    VALID_BIN_RESPONSES = ("y", "n", "yes", "no")
    path = input("PLEASE INPUT THE PATH TO THE DESIRED DIRECTORY\n").replace("/", "\\")
    type = ""
    remove_root = False

    while(True):
        type = input("PLEASE INPUT THE DESIRED FILE TYPE\n")
        if(len(type) == 0 or type.lower() == "all"):
            type = "True"
            break
        if(type[0] == '.'):
            break
        print("ERROR: PROVIDED FILE TYPE IS INVALID.")

    while(True):
        temp = input("DO YOU WISH TO INCLUDE THE ROOT? (Y/N) ").lower()
        if(not(response_valid(temp, VALID_BIN_RESPONSES))):
            print("ERROR: INVALID RESPONSE INPUT")
            continue
        if(temp[0] == 'n'):
            remove_root = True
        break

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
        print(directoryPaths[i]+":")
        print(fileNames[i])
        print()

main()
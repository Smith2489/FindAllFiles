import os
from verify import validate_string, VALID_SEPARATORS, VALID_BIN_RESPONSES
from save_to_file import save_to_file

INDICES = ("FIRST", "SECOND", "THIRD")

def main():
    files = ["", "", ""]
    file_text = ["", "", ""]

    for i in range(len(files)):
        while(True):
            files[i] = input("PLEASE TYPE IN THE NAME OF THE "+INDICES[i]+" FILE TO STITCH\n")
            if(not(os.path.isfile(files[i]))):
                print("ERROR: FILE NOT FOUND")
                continue
            break
                

    for i in range(len(files)):
        with open(files[i], "r") as file:
            file_text[i] = file.read()


    separator = validate_string("STITCH WITH A SPACE OR A NEW LINE?", VALID_SEPARATORS, 'n', " ", "\n")
    print_to_console = validate_string("WOULD YOU LIKE TO PRINT OUT TO THE CONSOLE? (Y/N)", VALID_BIN_RESPONSES, 'y', False, True)
    out = ""
    for i in range(len(file_text)):
        out+=file_text[i]
        if(i < len(file_text)-1):
            out+=separator

    if(print_to_console):
        print(out)
    
    save_to_file(out)

    return

    


main()
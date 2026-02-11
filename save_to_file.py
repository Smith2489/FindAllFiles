from verify import validate_string, VALID_BIN_RESPONSES
import os

def save_to_file(out):
    modify = False
    while(not(modify)):
        out_file = input("PLEASE INPUT THE NAME OF THE OUTPUT FILE: ")
        if(os.path.isfile(out_file)):
            print("FILE ALREADY EXISTS", " ")
            modify = validate_string("DO YOU WISH TO OVERWRITE IT? (Y/N)", VALID_BIN_RESPONSES, 'n', True, False)
        else:
            modify = True
    
    with open(out_file, "w") as file:
        file.write(out)
    return
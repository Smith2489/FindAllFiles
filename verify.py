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
    
VALID_BIN_RESPONSES = ("y", "n", "yes", "no")
VALID_PRINT_OPTIONS = ("console", "file")
VALID_SEPARATORS = ("space", "newline", "new line")
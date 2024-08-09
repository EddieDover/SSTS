
#variables: name, durname, id, email, password, confirm_pass, valid(boolean),  

def check_email(email):
    valid=False
    for i in range (0,len(email)):
        if email[i]=="@":
            for j in range (i,len(email)):
                if email[i]==".":
                    valid=True      
        if valid==True:
            break

def check_password_symbol(password):
    valid=False
    for i in range (0, len(password)):
        for symbol in range(33,48):
            if password[i]==chr(symbol):
                valid=True
        for symbol in range(58,65):
            if password[i]==chr(symbol):
                valid=True
        for symbol in range(91,97):
            if password[i]==chr(symbol):
                valid=True
        for isymbol in range(123,127):
            if password[i]==chr(symbol):
                valid=True
#checks if there is a symbol

def check_password_number(password):
    valid=False
    for i in range (0,len(password)):
        for number in range(0,10):
            if password[i]==str(number):
                valid=True
#checks if there is a number

def check_confirm_password(password,confirm_pass):
    valid_pass=False
    if password>=8:
        check_password_number(password)
        check_password_symbol(password)
        if password==confirm_pass:
            valid_pass=True
#checks teh length and if is same as confirm

def valid_name_surname(name, surname):
    valid_name=True
    temp_name=""
    for different_names in range (0,2):
        if different_names==0:
            temp_name=name
        if different_names==1:
            temp_name=surname
        #changes between surname and name so that they are both checked
        for i in range (0,len(temp_name)):
            for invalid in range(33,65):
                if temp_name[i]==chr(invalid):
                    valid_name=False
                    #checks if there are any numbers in the name
            for invalid in range(91,97):
                if temp_name[i]==chr(invalid):
                    valid_name=False
            for invalid in range(123,127):
                if temp_name[i]==chr(invalid):
                    valid_name=False


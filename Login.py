details=[["Alex","Irwin","178884","27/06/2007","alex07.irwin@btinternet.com","alexirwin07","P4s5w0rD"]]

def login():
    success=False
    username=input("")
    password=input("")
    for i in range (0,(len(details))):
        print (details[i][5],details[i][6])
        if details [i][5]==username:
            if details[i][6]==password:
                success=True
    if success!=True:
        success=False
    print (success)
#login()
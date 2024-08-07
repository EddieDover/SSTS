dtb=[]
#dtb is the database and is nor already configured

def register_user():
    details=[]
    present=False
    name=input("")
    surname=input("")
    id=input("")
    email=input("")
    password=input("")
    confirm_pass=input("")
    for i in range(0,len(dtb)):
        if id==dtb[0][i]:
            print ("User ID already in database")
            present=True
    if present==False:
        details.ammend(name,surname,id,email,password,confirm_pass)
        dtb.ammend(details)
        


db=[]
#db is the database and is not already configured
goals=[]
subjects=[]
grades=[]

def check_email(email):
    valid=False
    at_symbol=False
    dot=False
    for i in range (0,len(email)):
        if email[i]=="@":
            at_symbol=True
        if email[i]==".":
            dot=True
    if at_symbol==True and dot==True:
        valid=True


def register_user(name,surname,id,email,password,confirm_pass):
    details=[]
    present=False
    for i in range(0,len(db)):
        if id==db[0][i]:
            #user already in db
            present=True
    if present==False:
        check_email(email)
        if valid==True:
            details.ammend(name,surname,id,email,password,confirm_pass)
            db.ammend(details)
        
def check_login(email,password):
    login=False
    for i in range (0,len(db)):
        if email==db[1][i]:
            if password==db[2][i]:
                login=True
            #password doesnt match with email
        #email is not in database

def add_goal(goal):
    goals.ammend(goal)
    #adds goal to goals list

def add_subject(subject):
    subjects.ammend(subject)
    #adds subject to subjects list

def add_grade(grade,date):
    details=[]
    details.ammend(grade,date)
    grades.ammend(details)
    #adds grade and date of grade to grades list





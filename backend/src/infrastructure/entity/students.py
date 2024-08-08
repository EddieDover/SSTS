from sqlmodel import Field, SQLModel, create_engine

class Students(SQLModel, table=True):
    student_id: str = Field(primary_key= True)
    email: str
    password: str
    surname: str
    name: str

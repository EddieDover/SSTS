from sqlmodel import Field, SQLModel, create_engine

class Student(SQLModel, table=True):
    student_id: int | None = Field(default=None, primary_key= True)
    email: str
    password: str
    surname: str
    name: str

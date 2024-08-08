from sqlmodel import Field, SQLModel, create_engine

class Subjects(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    student_id: str = Field(foreign_key = True)
    subject: str
    grade: str
from datetime import date

from pydantic import BaseModel
from enum import Enum

class PersonType(Enum):
     STUDENT = "STUDENT"
     TEACHER = "TEACHER"

class Mark(Enum):
    F = 0
    E = 1
    D = 2
    C = 3
    B = 4
    A = 5

class Student(BaseModel):
    name: str


class Teacher(BaseModel):
    name: str

class Homework(BaseModel):
    name: str
    publish_date: date
    description: str
    deadline: date

class AttemptResult(BaseModel):
    comment: str
    mark: Mark

class HomeworkAttempt(BaseModel):
    homework: Homework
    submit_date: date
    result: AttemptResult


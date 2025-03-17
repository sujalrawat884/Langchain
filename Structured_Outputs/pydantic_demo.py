from pydantic import BaseModel

class Student(BaseModel):
    name: str

new_student = {'name' : Sujal}


student = Student(**new_student)

print(student)
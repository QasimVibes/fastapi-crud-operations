from fastapi import FastAPI
import uvicorn

app = FastAPI()

students: list = [
    {"Student_ID": 1, "Name": "John", "Age": 17, "Class": "VI", "Grade": "A"},
    {"Student_ID": 2, "Name": "Peter", "Age": 18, "Class": "IV", "Grade": "B"},
    {"Student_ID": 3, "Name": "Amy", "Age": 16, "Class": "V", "Grade": "C"},
    {"Student_ID": 4, "Name": "Hannah", "Age": 18, "Class": "VII", "Grade": "A+"},
]


@app.get("/students")
def student_list():
    return students


@app.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student["Student_ID"] == student_id:
            return student
    return {"message": "Student not found"}


@app.post("/students")
def add_student(student_id: int, name: str, age: int, class_: str, grade: str):
    students.append(
        {
            "Student_ID": student_id,
            "Name": name,
            "Age": age,
            "Class": class_,
            "Grade": grade,
        }
    )
    return students


@app.put("/students/{student_id}")
def update_student(student_id: int, name: str, age: int, class_: str, grade: str):
    for student in students:
        if student["Student_ID"] == student_id:
            student["Name"] = name
            student["Age"] = age
            student["Class"] = class_
            student["Grade"] = grade
            return students
    return {"message": "Student not found"}


@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for student in students:
        if student["Student_ID"] == student_id:
            students.remove(student)
            return students
    return {"message": "Student not found"}


def start():
    uvicorn.run("student.main:app", host="127.0.0.1", port=8080, reload=True)
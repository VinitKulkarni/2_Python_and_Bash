results = {
    "student1":"D",
    "student2":"C",
    "student3":"B",
    "student4":"A",
    "student5":"F",
    }

#adding new student and grade to the dictionary
results["student6"] = "A"

#result after adding new student
print("RESULTS OF STUDENTS:\n",results)

#update the existing student grade
nameOfStudent = input("Enter the student name, whose grade you want to update:")
newGrade = input("Enter the Grade:")

#finding existing student name
flag=False
for key in results:
    if (key == nameOfStudent):
        results[key] = newGrade
        flag=False
        break
    else:
        flag=True

if flag == True: 
    print ("Student not found")

#result after changing the grade
print("RESULTS OF STUDENTS:\n",results)

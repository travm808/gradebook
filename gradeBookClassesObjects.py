def studentChecker(studentName, studentList):
    if (studentName in studentList):
        return True
    else: 
        print("Student Not Found Please Try Again")
        print("\n")
def classChecker(className, gradebook):
    if (className in gradebook):
        return True
    else:
        print("Class Not Found. Please Try Again")
        print("\n")
def testChecker(testName, gradebook):
    if (testName in gradebook):
        return True
    else:
        print("Test Not Found. Please Try Again")
        print("\n")

class Student:
    def __init__(self, name, schoolClass, grades):
        self.name = name
        self.schoolClass = schoolClass
        self.grades = grades
print("Welcome to My Gradebook")

students = {}
while True:
    print("Add Student")
    print("Add Class")
    print("Add Test with Grade")
    print("Remove Student")
    print("Remove Class")
    print("Remove Test with Grade")
    print("Test Average")
    print("Show All Students")
    print("Show Student's Classes")
    print("Quit")
    userInput = input("Please Select an Option: ")

    if (userInput == "Add Student"):
        newStudent = input("What is the Student's Name? ")
        students[newStudent] = {}
    elif (userInput == "Add Class"):
        newClassStudent = input("What Student are We Adding a Class to? ")
        if (studentChecker(newClassStudent,students)):
            newClass = input("What Class are We Adding? ")
            students[newClassStudent][newClass] = {}
    elif (userInput == "Add Test with Grade"):
        newGradeStudent = input("What Student are We Adding a Test and Grade to? ")
        if (studentChecker(newGradeStudent, students)):
            newGradeClass = input("What Class is this Test in? ")
            if (classChecker(newGradeClass,students[newGradeStudent])):
                newTestName = input("What is the Name of the Test? ")
                newTestGrade = input("What is the Grade for that Test? ")
                students[newGradeStudent][newGradeClass][newTestName] =  newTestGrade
    elif (userInput == "Remove Student"):
        removeStudent = input("What Student are We Removing? ")
        if (studentChecker(removeStudent, students)):
            del students[removeStudent]
    elif (userInput == "Remove Class"):
        removeClassStudent = input("What Student are We Removing a Class to? ")
        if (studentChecker(removeClassStudent, students)):
            removeClass = input("What Class are We Removing? ")
            if (classChecker(removeClass, students[removeClassStudent])):
                del students[removeClassStudent][removeClass]          
    elif (userInput == "Remove Test with Grade"):
        removeGradeStudent = input("What Student are We Removing a Test from? ")
        if (studentChecker(removeGradeStudent, students)):
            removeGradeClass = input("What Class are We Removing a Test from? ")
            if (classChecker(removeGradeClass, students[removeGradeStudent])):
                removeTest = input("What Test are We Removing? ")
                if (testChecker(removeTest, students[removeGradeStudent][removeGradeClass])):
                    del students[removeGradeStudent][removeGradeClass][removeTest]
    elif (userInput == "Show All Students"):
        print(students)
        print("\n")
    elif (userInput == "Test Average"):
        testAvgStudent = input("What Student are We Getting a Test Average For? ")
        if (studentChecker(testAvgStudent,students)):
            testAvgClass = input("What Class are We Getting a Test Average For? ")
            if (classChecker(testAvgClass, students[testAvgStudent])):
                sum = 0
                avgScore = 0
                testAmount = 0
                for test, grade in students[testAvgStudent][testAvgClass].items():
                    sum += int(grade)
                    testAmount += 1
                avgScore = float(sum) / float(testAmount)
                print("The test average for " + testAvgStudent + " is " + str(avgScore) + " for " + testAvgClass + "class")
                print("\n")
    elif (userInput == "Show Student's Classes"):
        studentName = input("What Student's Classes Would You Like to See? ")
        if (studentChecker(studentName, students)):
            print(studentName + " classes are printed below")
            if (students[studentName] != {}):
                for nameClass, tests in students[studentName].items():
                    print(nameClass)
            else:
                print("This Student has No Classes Assigned to Him or Her")
                print("\n")
    elif (userInput == "Quit"):
        break
    else:
        print("Invalid Option. Please Try Again")

print(students)



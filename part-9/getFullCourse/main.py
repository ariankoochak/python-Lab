
# courseList = {'riazi' : 3,'dini' : 2,'fizik' : 3,'arabi' : 2,'zaban' : 1}
courseList = {}

def getFullCourseData():
    return {'courseName':getCourseName(),'score':float(input('enter score : '))}

def getCourseName():
    exp = input('enter course name : ')
    while exp not in courseList.keys():
        print('your course name is invalid')
        exp = input('please try again : ')
    return exp

def getCourseList():
    exp = []
    isFinish = 'n'
    while isFinish == 'n':
        exp.append(getFullCourseData())
        isFinish = input('is finish? (y/n) : ').lower()
    return exp

def addStudent():
    print('\nadd student:')
    firstName = input('enter first name : ')
    lastName = input('enter last name : ')
    studentCode = input('enter student code : ')
    return [studentCode,{'firstName' : firstName,'lastName' : lastName,'grades' : getCourseList()}]
def showAll(inp):
    for studentCode in inp:
        student = inp[studentCode]
        print(f'\n\n\t{student["firstName"]} {student["lastName"]} | {studentCode}')
        print(100*'=')
        i = 1
        zaribSum = 0
        scoreWithZaribSum = 0
        for grade in student['grades']:
            zarib = courseList[grade["courseName"]]
            score = grade["score"];
            zaribSum += zarib
            scoreWithZaribSum += score * zarib
            print(f'{i} - {grade["courseName"]} \t\t{zarib} \t\t{score}')
            i += 1
        print(50 * '-')
        print(f'total => \t\t\t\t {scoreWithZaribSum / zaribSum}')
        print(100*'=')

def getClass():
    isFinish = 'n'
    exp = {}
    while isFinish == 'n':
        temp = addStudent()
        exp[temp[0]] = temp[1]
        isFinish = input('students is finish? (y/n) : ').lower()
    return exp

def readCourseList(path):
    db = open(path,'r').readlines()
    for i in range(len(db)):
        db[i] = db[i].split(',')
        courseList[db[i][0]] = int(db[i][1][0])

##############################################################
readCourseList('/Users/arian.koochakgmail.com/Desktop/Code/python-Lab/part-9/getFullCourse/courseList.txt')
# {'123': {'firstName': 'arian', 'lastName': 'koochak', 'grades': [{'courseName': 'riazi', 'score': 20.0}, {'courseName': 'dini', 'score': 20.0}, {'courseName': 'fizik', 'score': 17.0}]}, '7431': {'firstName': 'abbas', 'lastName': 'elhi', 'grades': [{'courseName': 'fizik', 'score': 20.0}, {'courseName': 'riazi', 'score': 20.0}, {'courseName': 'dini', 'score': 16.0}]}}

showAll({'123': {'firstName': 'arian', 'lastName': 'koochak', 'grades': [{'courseName': 'riazi', 'score': 20.0}, {'courseName': 'dini', 'score': 20.0}, {'courseName': 'fizik', 'score': 17.0}]}, '7431': {'firstName': 'abbas', 'lastName': 'elhi', 'grades': [{'courseName': 'fizik', 'score': 20.0}, {'courseName': 'riazi', 'score': 20.0}, {'courseName': 'dini', 'score': 16.0}]}})

# showAll(getClass())
    


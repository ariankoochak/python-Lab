
courseList = {'riazi' : 3,'dini' : 2,'fizik' : 3,'arabi' : 2,'zaban' : 1}

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
        print(f'total => \t\t\t {scoreWithZaribSum / zaribSum}')
        print(100*'=')

def getClass():
    isFinish = 'n'
    exp = {}
    while isFinish == 'n':
        temp = addStudent()
        exp[temp[0]] = temp[1]
        isFinish = input('students is finish? (y/n) : ').lower()
    return exp
##############################################################

showAll(getClass())
    


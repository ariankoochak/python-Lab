def showKarname(studentScore):
    unitSum = 0
    scoreInUnitSum = 0
    for course in studentScore:
        k = "%.2f"%(course[1]*course[2])
        print(f'{course[0]}\t\t{course[1]}\t\t{course[2]}\t\t{k}\n',end='')
        unitSum += course[1]
        scoreInUnitSum += float(k);
    print('______________________________________________________')
    print('Total\t\t'+str(unitSum),"%34.2f"%(scoreInUnitSum/unitSum))
print('\n\n')
showKarname([['riazi',2,16.50],['DiNi',6,11.25],['DikTe',3,13.75]])
print('\n\n')

import random
import csv
import os
import threading
import time
#0,3,LIBERAL;NDP;GREEN;CPC,1;1;3;2,NO;NO;YES;YES
def randomYesNo():
    num = random.randrange(0, 100)
    if num >= 50:
        return 'YES'
    return 'NO'
j = 0
template = []
def mainThread():
    global template
    global j
    for i in range(0,100000000):
        hezb = ['LIBERAL','NDP','GREEN','CPC']
        random.shuffle(hezb)
        hezb = ";".join(hezb)
        template.append( f'{j},{i},{hezb},{random.randrange(1, 5)};{random.randrange(1, 5)};{random.randrange(1, 5)};{random.randrange(1, 5)},{randomYesNo()};{randomYesNo()};{randomYesNo()};{randomYesNo()}')
        
    with open('bigData.csv', 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        for item in template:
            writer.writerow([item])
def loadThread():
    while(len(template) < 100000000):
        # os.system('clear')
        print(f'{int(100 * len(template) / 100000000)}%') 
        time.sleep(0.25)
        os.system('cls')
    

main = threading.Thread(target=mainThread)
timer = threading.Thread(target = loadThread)

main.start()
timer.start()



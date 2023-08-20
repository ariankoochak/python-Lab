def caclulator(a,b,action):    
    print('\t------------------------------------------')
    c = None
    match action:
        case '+':
            c = a + b
        case '-':
            c = a - b
        case '*':
            c = a * b  
        case '/':
            if b != 0:
                c = a / b
            else:
                print('\terror => Div/0')  
        case '//':
            if b != 0:
                c = a // b
            else:
                print('\terror => Div/0')  
        case '%':
            if b != 0:
                c = a % b
            else:
                print('\terror => Div/0')   
        case _ :
            print('\tinvalid operator!')
    if c != None:
        print('\tResult    ',a,' ',action,' ',b,' = ',c,'\n')


a = float(input('\n\tEnter First Number:\t'))
action = input('\tEnter Operator:\t\t')
b = float(input('\tEnter Second Number:\t'))

caclulator(a,b,action)
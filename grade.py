with open('./students.txt', 'r') as f:
    
    def line():
        a = '    Student            Name   Midterm   Final   Average   Grade'
        print(a)
        print('-'*65)
        
    def print_(x):
        for i in range(len(x)):
            print("{:>10} {:>16} {:>6} {:>8} {:>10} {:>6}".format(*x[i]))        
        
    def to_str(x):
        for i in range(len(x)):
            x[i][2] = str(x[i][2])
            x[i][3] = str(x[i][3])
            
    def grade(x):
        for i in range(len(x)):
            if x[i][4] >= 90:
                x[i].append('A')
            elif x[i][4] >= 80:
                x[i].append('B')
            elif x[i][4] >= 70:
                x[i].append('C')
            elif x[i][4] >= 60:
                x[i].append('D')
            else:
                x[i].append('F')
        to_str(x)
                
    def readstudent(x):
        s = [i for i in f]
        s = [s[i].strip().split('\t') for i in range(len(s))]
        for i in range(len(s)):
            s[i].append((float(s[i][2])+float(s[i][3]))/2)        
        grade(s)
        s.sort(key = lambda e : float(e[4]), reverse = True)
        return s
    
    def show(x):
        line()
        print_(x)
                
    def search(x): 
        a = input('Student ID: ')
        l =[x[i][0] for i in range(len(x))]
        if a not in l:
            return print('NO SUCH PERSON.')
        line()
        for i in range(len(x)):
            if a == l[i]:
                print("{:>10} {:>16} {:>6} {:>8} {:>10} {:>6}".format(*x[i]))  
            
    def changescore(x):
        a = input('Student ID: ')
        l =[x[i][0] for i in range(len(x))]
        if a not in l:
            return print('NO SUCH PERSON.')
        for v in range(len(x)):
            if a == s[v][0]:
                v1 = v
        b = input('Mid/Final? ')
        if b not in ['mid', 'final']:
            return 
        c = float(input('Input new score: '))
        if (c > 100) | (c < 0):
            return
        for i in range(len(x)):
            if (b == 'mid') & (i == v1):
                x[i][2] = float(c)
                x[i][4] = (c + float(x[i][3]))/2
            if (b == 'final') & (i == v1):
                x[i][3] = float(c)
                x[i][4] =  (float(x[i][2]) + c)/2
        if x[v1][4] >= 90:
            x[v1][5] = 'A'
        elif x[v1][4] >= 80:
            x[v1][5] = 'B'
        elif x[v1][4] >= 70:
            x[v1][5] = 'C'
        elif x[v1][4] >= 60:
            x[v1][5] = 'D'
        else:
            x[v1][5] = 'F'
        print('Score changed.')
        x.sort(key = lambda e : float(e[4]), reverse = True)
        to_str(x)


    def add(x):
        stid = input('Student ID: ')
        l =[x[i][0] for i in range(len(x))]
        if stid in l:
            return print('ALREADY EXISTS')
        name = input('Name: ')
        mid = int(input('Midterm Score: '))
        final = int(input('Final Score: '))
        if ((mid > 100)|(mid < 0))|((final > 100)|(final < 0)):
            return
        l = [stid, name, mid, final]
        l.append((l[2] + l[3]) / 2)
        if l[4] >= 90:
            l.append('A')
        elif l[4] >= 80:
            l.append('B')
        elif l[4] >= 70:
            l.append('C')
        elif l[4] >= 60:
            l.append('D')
        else:
            l.append('F')
        x.append(l)
        x.sort(key = lambda e : float(e[4]), reverse = True)
        to_str(x)
        if len(l) == 6:
            print('Student added.')
    
    def searchgrade(x):
        grade = input('Grade to search: ')
        l =[x[i][5] for i in range(len(x))]
        if grade not in l:
            return print('NO RESULTS.')
        for i in range(len(x)):
            if grade == l[i]:
                print("{:>10} {:>16} {:>6} {:>8} {:>10} {:>6}".format(*x[i]))  
    
    def remove(x):
        re = input('Student ID: ')
        l =[x[i][0] for i in range(len(x))]
        if re not in l:
            return print('NO SUCH PERSON.')
        for i in range(len(x)):
            if re == l[i]:
                x.remove(x[i])
                print('Student removed')
        if len(x) < 1:
            return print('List is empty.')
    
    def quit(x):
        a = input('Save data?[yes/no] ')
        if a == 'yes':
            for i in range(len(x)):
                x[i].remove(x[i][5])
                x[i].remove(x[i][4])
                x[i] = '\t'.join(x[i]) + '\n'
            f_n = input('File name: ')
            x = ''.join(x)
            with open('./'+f_n, 'w') as f:
                f.write(x)
            print('$')
        if a == 'no':
            return print('$')
               
    s = readstudent(f)
    show(s)
    
    while True:
        command = input("# ")
        n_command = command.upper()
        if n_command == "SHOW" :
            show(s)
        elif n_command == "SEARCH":
            search(s)
        elif n_command == "CHANGESCORE":
            changescore(s)
        elif n_command == 'ADD':
            add(s)
        elif n_command == 'SEARCHGRADE':
            searchgrade(s)
        elif n_command == 'REMOVE':
            remove(s)
        elif n_command == 'QUIT':
            quit(s)
            break
        else:
            print("wrong input!")
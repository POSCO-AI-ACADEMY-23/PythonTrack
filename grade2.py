f = open("students.txt", 'r')

def line():
    a = ' Student            Name   Midterm   Final   Average   Grade'
    print(a)
    print('-'*65)

    for i in range(len(x)):
        print("{:>10} {:>16} {:>6} {:>8} {:>10} {:>6}".format(*x[i]))

def show(x):
    line()

show()

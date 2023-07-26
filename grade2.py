with open('students.txt', 'r') as f:
     
    def line():
        a = 'Student        Name   Midterm   Final   Average   Grade'
        print(a)                            # 출력
        print('-'*62)                       # - 62개 추가

    def print_(x):
        for i in range(len(x)):
            print("{:>0} {:>12} {:>5} {:>7} {:>10} ".format(*x[i]))  # format(x[i][0],x[i][1],x[i][2],x[i][3],x[i][4]),x[i][5]) 
                   #학번  이름   중간  기말   평균  등급
    def read(x):
        f1 = f.readlines()
        l = [i for i in f1]
        l= [l[i].strip().split('\t') for i in range(len(l))]
        
        for i in range(len(l)):
            l[i].append((float(l[i][2])+float(l[i][3]))/2) 
        return l

    line()
    s = read(f)
    print_(s)
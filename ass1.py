def main():
    for i in range (2):
        
        n = []
        m = []
        a = []
        l = []
        p = []
        c = []
        cg = []
         
        print("\n")    
        name = input ('Please Enter Your Name: ')
        mat_no = input ('Enter Your Matric Number: ')
        age = input ('Enter your Age: ')
        level = input ('Enter your Current Level: ')
        program = input ('Enter your Program: ')
        college = input ('Enter your College: ')
        cgpa = input ('Enter your current CGPA: ')


        print ('Hello ' + name)
        print ('Your Matric Number is ' + mat_no)
        print ('You are ' + age + ' years old')
        print ('You are currently in ' + level + ' level ')
        print ('You are studying ' + program + ' in ' + college)
        print ('Your current CGPA is ' + cgpa)

        n.append (name)
        m.append (mat_no)
        a.append (age)
        l.append (level)
        p.append (program)
        c.append (college)
        cg.append (cgpa)
    
    print("Students Registered: \n")
    print(n)

main()

def Marks_Display():

    for i in range(2):
        print("------------------------------------------------")
        a = phy[i]
        b = math[i]
        c = eng[i]
        d = sci[i]
        e = mfl[i]
        avg_score = ((a+b+c+d+e) / 5)
        if (avg_score >= 85):
            print(Student_Names[i],": A* ")
        elif (avg_score >= 70 ):
            print(Student_Names[i], ": A ")
        elif (avg_score >= 60 ):
            print(Student_Names[i], ": B ")
        elif (avg_score >= 50):
            print(Student_Names[i], ": C ")
        elif (avg_score >= 25 ):
            print(Student_Names[i], ": D ")
        else :
            print(Student_Names[i], ": dont come to school ")



        print("Phy:" , phy[i],"\tMath:", math[i], "\tEnglish:", eng[i],"\tSci:",sci[i],"\t MFL:",mfl[i],"\naverage:", avg_score)













def Input_Phy():
    for u in Student_Names:
        print(u)
        y = int(input("enter phy marks : "))
        phy.append(y)

def Input_Math():
    for u in Student_Names:
        print(u)
        y = int(input("enter math marks : "))
        math.append(y)

def Input_Eng():
    for u in Student_Names:
        print(u)
        y = int(input("enter eng marks : "))
        eng.append(y)

def Input_Sci():
    for u in Student_Names:
        print(u)
        y = int(input("enter sci marks : "))
        sci.append(y)

def Input_mfl():
    for u in Student_Names:
        print(u)
        y = int(input("enter MFL marks : "))
        mfl.append(y)



def student_Names():
    for i in range(2):
        x = input("name: ")
        Student_Names.append(x)

    Input_Phy()
    Input_Eng()
    Input_mfl()
    Input_Sci()
    Input_Math()


def Password_Check():
    print(" welcome to the TISB MARK's server ")
    pass1 = input("enter password: \n ")
    if pass1 == "admin":
        print("succesful entry")
        student_Names()
    else:
        print("wrong password")




Student_Names=[]
phy = []
math= []
eng = []
sci = []
mfl = []
average_Score = []
per = []

Password_Check()
Marks_Display()


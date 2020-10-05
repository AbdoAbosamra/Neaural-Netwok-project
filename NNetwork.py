import numpy as np
from tkinter import *
from tkinter import ttk


P = np.array([[1, 1], [-1, 1], [1, -1], [-1, -1]])
print("This is P : \n", P)
Pt = P.transpose()
print("The transpose of P is : ", Pt)
# 1- Calculate The Wight By:
# w = p*pt
W = np.dot(P, Pt)
print("The Wight is[ w = p * pt] : \n", W)


# 2- Define The Activation function hardlims.
def hardlims(n):
    res = np.zeros((n.shape[0], n.shape[1]))
    for i in range(len(n)):
        for j in range(len(res)):
            if (i == j):
                if (n[i] < 0):
                    res[int(j)] -= 1
                else:
                    res[int(j)] += 1

    return res


#####################################

def EnterMatricies():


    R = int(input("Enter the number of rows:"))


    C = int(input("Enter the number of columns:"))

    print("Enter the entries in a single line (separated by space): ")

    # User input of entries in a
    # single line separated by space
    global entries
    entries = list(map(int, input().split()))

    # For printing the matrix
    matrix = np.array(entries).reshape(int(R), int(C))
    return matrix


p1 = EnterMatricies()
print("The first input you entered : ", p1)
p2 = EnterMatricies()
print("The second input you entered : ", p2)


# check if the two inputs are orthogonal
# 𝑝1𝑇*p2
def orthogonal_Test(p1, p2):
    p1t = p1.transpose()

    n = np.dot(p2, p1t)
    if (n == 0):
        return ("P1 And P2 Are Orthogonal")
    else:
        return ("P1 And P2 Are NoT Orthogonal")


print(orthogonal_Test(p1, p2))

b = 0  # We don't have bais here.

n1 = np.dot(W, p1.transpose()) + b
n2 = np.dot(W, p2.transpose()) + b

print("n if we will test p1 :  \n", n1)
print("n if we will test p2 :  \n", n2)

a1 = hardlims(n1)
a2 = hardlims(n2)
print("The outPut of P1 is : \n", a1)
print("The outPut of P2 is : \n", a2)


def test(a1, p1):
   Pt =p1.transpose()
   for m in a1:
       for l in Pt:
            if(m == l):
                return ("Successful Test a = P")
                break
            else:
                return ("Failed test a != P")
                break
       break
Final_Test1 = test(a1, p1)
Final_Test2= test(a2, p2)
press = int(input(("If you want test with p1 press 1 , \nIf you want test with p2 press 2:")))
if (press == 1):
    print(Final_Test1)
else:
    print(Final_Test2)



####################################################################
#GUI

root = Tk()
root.title("Auto Assiciator Hebbian Network")

Rp = ttk.Label(root, text="Please Enter  Input rows")
Rp.pack()
R = ttk.Entry(root, width=20)

R.pack()
R.focus_set()
Cp = ttk.Label(root, text="Please Enter  Input columns")
Cp.pack()
C = ttk.Entry(root, width=20)
C.pack()
C.focus_set()
btn1 = ttk.Button(root, text="Enter")
btn1.pack()
INPUT = ttk.Label(root, text="Enter the entries in a single line (separated by space): ")
INPUT.pack()
C_entry1 = ttk.Entry(root, width=20)
C_entry1.pack()





def T():
    IN1 = StringVar()
    IN1.set(str(p1))
    P1_GUI = ttk.Label(root, text="The  Firt Input You entered is :")
    P1_GUI.pack()
    P1_GUI = ttk.Label(root, text=IN1.get())
    P1_GUI.pack()


btn2 = ttk.Button(root, text="Enter", command=T)
btn2.pack()
INPUT2 = ttk.Label(root, text="Enter the entries in a single line (separated by space): ")
INPUT2.pack()
C_entry2 = ttk.Entry(root, width=20)
C_entry2.pack()


def T2():
    P2_GUI = ttk.Label(root, text="The  Second Input You entered is :")
    P2_GUI.pack()

    P2_GUI = ttk.Label(root, text=p2)
    P2_GUI.pack()



btn3 = ttk.Button(root, text="Enter", command=T2)
btn3.pack()

w =orthogonal_Test(p1, p2)
def onclik():
    master=Tk()
    master.title("Test orthogonality")
    v = StringVar()
    v.set(w)
    Label(master, text=v.get()).pack()

bu22 = ttk.Button(root, text="Test orthogonality", command=onclik)
bu22.pack(side=LEFT)

def Test():
    v2=StringVar()
    v2.set(test(a1, p1))
    Label(root, text=v2.get()).pack()
def Press_GUI():
    Test = ttk.Label(root, text="If you want test with p1 press 1 , \nIf you want test with p2 press 2:").pack()
    Test_entry = ttk.Entry(root ,width=20).pack()
Test_btn = ttk.Button(root, text="Test Inputs" ,command=Press_GUI ).pack(side=RIGHT)
Test_btn2 = ttk.Button(root, text="Test Now!" ,command=Test)
Test_btn2.pack(padx=5 , pady=5,anchor=CENTER )

root.mainloop()

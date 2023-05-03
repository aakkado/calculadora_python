from tkinter import *
import math
import tkinter.messagebox

root = Tk()

root.title("Scientifc Calculator")
root.configure(background="powder blue")
root.resizable(width=False, height=False)
root.geometry("496x568+0+0")

calc = Frame (root)
calc.grid()

class Calc():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.input_value = True
        self.check_sum = False
        self.operator = ""
        self.result = False
    
    def numberEnter(self, num):
        self.result = False
        firstNum = txtDisplay.get()
        secondNum = str(num)
        if self.input_value:
            self.current = secondNum
            self.input_value = False
        else:
            if secondNum == '.':
                if secondNum in firstNum:
                    return
            self.current = firstNum + secondNum
        self.display(self.current)
    
    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)
    
    def validFunction(self):
        if self.operator == "add":
            self.total += self.current
            self.current = self.total
        if self.operator == "sub":
            self.total -= self.current
            self.current = self.total
        if self.operator == "multi":
            self.total *= self.current
            self.current = self.total
        if self.operator == "divide":
            self.total /= self.current
            self.current = self.total
        if self.operator == "mod":
            self.total %= self.current
            self.current = self.total
        self.input_value = True
        self.check_sum = False
        self.display(self.total)
        
    def sumTotal(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.validFunction()
        else:
            self.total = float(txtDisplay.get())
    
    def operation(self, operator):
        self.current = float(self.current)
        if self.check_sum:
            self.validFunction()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.operator = operator
        self.result = False
    
    def clearEntry(self):
        self.result = False
        self.current = str(self.current)[:-1]
        if self.current == "":
            self.current = "0"
        self.display(self.current)

    def clearAll(self):
        self.result = False 
        self.current = "0" 
        self.display(0) 
        self.input_value = True
        self.total = 0
        
    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)
    
    def tau(self):
        self.result =  False
        self.current = math.tau
        self.display(self.current)
        
    def e(self):
        self.result =  False
        self.current = math.e
        self.display(self.current)
        
    def mathsPM(self):
        self.result = False
        self.current = -(float(txtDisplay.get()))
        self.display(self.current)
        
    def squared(self):
        self.result = False
        self.current = math.sqrt (float(txtDisplay.get()))
        self.display(self.current)
        
    def cos(self):
        self.result = False
        self.current = math.cos (float(txtDisplay.get()))
        self.display(self.current)
        
added_value = Calc()

txtDisplay = Entry(calc, font=('arial',20,'bold'), bg = "powder blue", bd=30, width=29, justify=RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0, "0")

numpad = "789456123"
i=0
btn = []
for j in range(2,5):
    for k in range(3):
        btn.append(Button(calc, width=6, height=2, font=('arial',20,'bold'), bd = 4, text = numpad[i]))
        btn[i].grid(row = j , column = k, pady = 1)
        btn[i]["command"] = lambda x = numpad[i]: added_value.numberEnter(x)
        i += 1
#std calc buttons
btnClear = Button(calc, text=chr(67), width=6, height=2, font=('arial',20,'bold'), bd = 4,
                  bg = "powder blue", command=added_value.clearEntry).grid(row= 1, column= 0, pady = 1)

btnClearAll = Button(calc, text=chr(67) + chr(69), width=6, height=2, font=('arial',20,'bold'), bd = 4,
                  bg = "powder blue", command=added_value.clearAll).grid(row= 1, column= 1, pady = 1)

btnSqr = Button(calc, text="√", width=6, height=2, font=('arial',20,'bold'), bd = 4,
                  bg = "powder blue", command=added_value.squared).grid(row= 1, column= 2, pady = 1)

btnAdd = Button(calc, text="+", width=6, height=2, font=('arial',20,'bold'), bd = 4,
                  bg = "powder blue", command = lambda: added_value.operation("add")).grid(row= 1, column= 3, pady = 1)

btnSub = Button(calc, text="-", width=6, height=2, font=('arial',20,'bold'), bd = 4,
                  bg = "powder blue", command = lambda: added_value.operation("sub")).grid(row= 2, column= 3, pady = 1)

btnMult = Button(calc, text="x", width=6, height=2, font=('arial',20,'bold'), bd = 4,
                  bg = "powder blue", command = lambda: added_value.operation("multi")).grid(row= 3 , column= 3, pady = 1)

btnDiv = Button(calc, text=chr(247), width=6, height=2, font=('arial',20,'bold'), bd = 4,
                  bg = "powder blue", command = lambda: added_value.operation("divide")).grid(row= 4 , column= 3, pady = 1)

btnZero = Button(calc, text="0", width=6, height=2, font=('arial',20,'bold'), bd = 4,
                  bg = "powder blue", command = lambda: added_value.numberEnter(0)).grid(row= 5 , column= 0, pady = 1)

btnDot = Button(calc, text=".", width=6, height=2, font=('arial',20,'bold'), bd = 4,
                  bg = "powder blue", command = lambda: added_value.numberEnter(".")).grid(row= 5, column= 1, pady = 1)

btnPM = Button(calc, text=chr(177), width=6, height=2, font=('arial',20,'bold'), bd = 4,
                  bg = "powder blue", command = added_value.mathsPM).grid(row= 5 , column= 2, pady = 1)

btnEquals = Button(calc, text="=", width=6, height=2, font=('arial',20,'bold'), bd = 4,
                  bg = "powder blue", command=added_value.sumTotal).grid(row= 5 , column= 3, pady = 1)

#sci calc buttons

#Row1
btnPI = Button(calc, text="π", width=6, height=2, font=('arial',20,'bold'), bd = 4,
                  bg = "powder blue", command = added_value.pi).grid(row= 1 , column= 4, pady = 1)

btnCos = Button(calc, text="cos", width=6, height=2, font=('arial',20,'bold'), bd = 4,
                  bg = "powder blue", command=added_value.cos).grid(row= 1, column= 5, pady = 1)

btnTan = Button(calc, text='tan', width=6, height=2, font=('arial',20,'bold'), bd = 4,
                  bg = "powder blue").grid(row= 1 , column= 6, pady = 1)

btnSin = Button(calc, text="sin", width=6, height=2, font=('arial',20,'bold'), bd = 4,
                  bg = "powder blue").grid(row= 1 , column= 7, pady = 1)

#Row2
btn2PI = Button(calc, text="2π", width=6, height=2, font=('arial',20,'bold'), bd = 4,
                  bg = "powder blue", command = added_value.tau).grid(row= 2 , column= 4, pady = 1)

btnCosh = Button(calc, text="cosh", width=6, height=2, font=('arial',20,'bold'), bd = 4,
                  bg = "powder blue").grid(row= 2, column= 5, pady = 1)

btnTanh = Button(calc, text='tanh', width=6, height=2, font=('arial',20,'bold'), bd = 4,
                  bg = "powder blue").grid(row= 2 , column= 6, pady = 1)

btnSinh = Button(calc, text="sinh", width=6, height=2, font=('arial',20,'bold'), bd = 4,
                  bg = "powder blue").grid(row= 2 , column= 7, pady = 1)

#Row3
btnLog = Button(calc, text="Log", width=6, height=2, font=('arial',20,'bold'), bd = 4,
                  bg = "powder blue").grid(row= 3 , column= 4, pady = 1)

btnExp = Button(calc, text="Exp", width=6, height=2, font=('arial',20,'bold'), bd = 4,
                  bg = "powder blue").grid(row= 3, column= 5, pady = 1)

btnMod = Button(calc, text='Mod', width=6, height=2, font=('arial',20,'bold'), bd = 4,
                  bg = "powder blue", command = lambda: added_value.operation("mod")).grid(row= 3 , column= 6, pady = 1)

btnE = Button(calc, text="e", width=6, height=2, font=('arial',20,'bold'), bd = 4,
                  bg = "powder blue", command = added_value.e).grid(row= 3 , column= 7, pady = 1)

#Row4
btnLog2 = Button(calc, text="log2", width=6, height=2, font=('arial',20,'bold'), bd = 4,
                  bg = "powder blue").grid(row= 4 , column= 4, pady = 1)

btnDeg = Button(calc, text="deg", width=6, height=2, font=('arial',20,'bold'), bd = 4,
                  bg = "powder blue").grid(row= 4, column= 5, pady = 1)

btnCosh = Button(calc, text='acosh', width=6, height=2, font=('arial',20,'bold'), bd = 4,
                  bg = "powder blue").grid(row= 4 , column= 6, pady = 1)

btnSinh = Button(calc, text="asinh", width=6, height=2, font=('arial',20,'bold'), bd = 4,
                  bg = "powder blue").grid(row= 4 , column= 7, pady = 1)

#Row5
btnLog10 = Button(calc, text="log10", width=6, height=2, font=('arial',20,'bold'), bd = 4,
                  bg = "powder blue").grid(row= 5 , column= 4, pady = 1)

btnLog1 = Button(calc, text="log1p", width=6, height=2, font=('arial',20,'bold'), bd = 4,
                  bg = "powder blue").grid(row= 5, column= 5, pady = 1)

btnExpm1 = Button(calc, text='exmp1', width=6, height=2, font=('arial',20,'bold'), bd = 4,
                  bg = "powder blue").grid(row= 5 , column= 6, pady = 1)

btnLgmma = Button(calc, text="lgmma", width=6, height=2, font=('arial',20,'bold'), bd = 4,
                  bg = "powder blue").grid(row= 5 , column= 7, pady = 1)

#Label
lblDisplay = Label(calc, text = "Scientific Calculator", font=('arial',20,'bold'), justify=CENTER)
lblDisplay.grid(row=0,column=4,columnspan=4)

#menus
def iExit():
    iExit = tkinter.messagebox.askyesno("Scientifc Calculator","Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return

def scientific():
    root.resizable(width=False, height=False)
    root.geometry("966x568+0+0")

def standart():
    root.resizable(width=False, height=False)
    root.geometry("496x568+0+0")

menubar = Menu(calc)

filemenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Standart", command=standart)
filemenu.add_command(label="Scientific", command=scientific)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=iExit)

editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_separator()
editmenu.add_command(label="Paste") 

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="View Help")   

root.configure(menu=menubar)
root.mainloop()
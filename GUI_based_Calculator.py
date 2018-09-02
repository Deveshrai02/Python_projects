from tkinter import *

class calculator:
    def __init__(self):
        self.root=Tk()
        self.result=Label(self.root,bg="white")
        self.result.grid(row=0,column=0)
        self.btn1=Button(self.root,text='1',bg="orange",width=6,height=4,command=lambda : self.get_num("1")).grid(row=1,column=0)
        self.btn2 = Button(self.root, text='2', bg="orange",width=6,height=4,command=lambda : self.get_num("2")).grid(row=1, column=1)
        self.btn3 = Button(self.root, text='3', bg="orange",width=6,height=4,command=lambda : self.get_num("3")).grid(row=1, column=2)
        self.btnAdd = Button(self.root, text='+', bg="orange",width=6,height=4,command=lambda : self.get_operator("+")).grid(row=1, column=3)
        self.btn4 = Button(self.root, text='4', bg="orange", width=6, height=4,command=lambda : self.get_num("4")).grid(row=2, column=0)
        self.btn5 = Button(self.root, text='5', bg="orange", width=6, height=4,command=lambda : self.get_num("5")).grid(row=2, column=1)
        self.btn6 = Button(self.root, text='6', bg="orange", width=6, height=4,command=lambda : self.get_num("6")).grid(row=2, column=2)
        self.btnSub = Button(self.root, text='-', bg="orange", width=6, height=4,command=lambda : self.get_operator("-")).grid(row=2, column=3)
        self.btn7 = Button(self.root, text='7', bg="orange", width=6, height=4,command=lambda : self.get_num("7")).grid(row=3, column=0)
        self.btn8 = Button(self.root, text='8', bg="orange", width=6, height=4,command=lambda : self.get_num("8")).grid(row=3, column=1)
        self.btn9 = Button(self.root, text='9', bg="orange", width=6, height=4,command=lambda : self.get_num("9")).grid(row=3, column=2)
        self.btnDiv = Button(self.root, text='/', bg="orange", width=6, height=4,command=lambda : self.get_operator("/")).grid(row=3, column=3)
        self.btn0 = Button(self.root, text='0', bg="orange", width=6, height=4,command=lambda : self.get_num("0")).grid(row=4, column=0)
        self.btnMul = Button(self.root, text='*', bg="orange", width=6, height=4,command=lambda : self.get_operator("*")).grid(row=4, column=1)
        self.btnClr = Button(self.root, text='C', bg="orange", width=6, height=4,command=lambda : self.get_clr()).grid(row=4, column=2)
        self.btnEquals = Button(self.root, text='=', bg="orange", width=6, height=4,command=lambda : self.print_result()).grid(row=4, column=3)

        self.root.mainloop()

    def get_num(self,num):
        new_num=self.result['text']+num
        self.result.configure(text=new_num)

    def get_clr(self):
        self.result.configure(text="")

    def get_operator(self,operator):
        self.first_num=int(self.result['text'])
        self.operator=operator
        self.result.configure(text="")

    def print_result(self):
        self.second_num=int(self.result['text'])
        if self.operator=="+":
            self.result.configure(text=str(self.first_num+self.second_num))
        elif self.operator=="-":
            self.result.configure(text=str(self.first_num - self.second_num))
        elif self.operator=="/":
            self.result.configure(text=str(self.first_num / self.second_num))
        else:
            self.result.configure(text=str(self.first_num * self.second_num))




obj1=calculator()

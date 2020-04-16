from tkinter import *
from PIL import *
#from tkinter import ImageTk
#calc = Tk()
#canvas = Canvas(calc, width = 200, height = 200, bg = 'blue')
#canvas.pack(expand = YES, fill = BOTH)
#self.image = ImageTk.PhotoImage(file = "C:\\Users\\location\\imageName.png")
#canvas.create_image(10, 10, image = self.image, anchor = NW)
expression = "" 
def press(num): 
    global expression 
    expression = expression + str(num) 
    equation.set(expression) 
def ravno(): 
    try: 
        global expression 
        total = str(eval(expression)) 
        equation.set(total) 
        expression = "" 
    except: 
  
        equation.set("Error") 
        expression = "" 
def clear(): 
    global expression 
    expression = "" 
    equation.set("") 
if __name__ == "__main__": 
    calc = Tk()
    calc.configure(background="light blue") 
    calc.title("Culculator")
    calc.geometry("265x125")
    equation = StringVar()
    expression_field = Entry(calc, textvariable=equation) 
    expression_field.grid(columnspan=4, ipadx=70) 
    equation.set('Vvedi cifri')
    button7 = Button(calc, text=' 7 ', fg='black', bg='light green', command=lambda: press(7), height=1, width=7) 
    button7.grid(row=2, column=0) 
    button8 = Button(calc, text=' 8 ', fg='black', bg='light green', command=lambda: press(8), height=1, width=7) 
    button8.grid(row=2, column=1) 
    button9 = Button(calc, text=' 9 ', fg='black', bg='light green', command=lambda: press(9), height=1, width=7) 
    button9.grid(row=2, column=2) 
    button4 = Button(calc, text=' 4 ', fg='black', bg='light green', command=lambda: press(4), height=1, width=7) 
    button4.grid(row=3, column=0) 
    button5 = Button(calc, text=' 5 ', fg='black', bg='light green', command=lambda: press(5), height=1, width=7) 
    button5.grid(row=3, column=1) 
    button6 = Button(calc, text=' 6 ', fg='black', bg='light green', command=lambda: press(6), height=1, width=7) 
    button6.grid(row=3, column=2) 
    button1 = Button(calc, text=' 1 ', fg='black', bg='light green', command=lambda: press(1), height=1, width=7) 
    button1.grid(row=4, column=0) 
    button2 = Button(calc, text=' 2 ', fg='black', bg='light green', command=lambda: press(2), height=1, width=7)
    button2.grid(row=4, column=1) 
    button3 = Button(calc, text=' 3 ', fg='black', bg='light green', command=lambda: press(3), height=1, width=7) 
    button3.grid(row=4, column=2) 
    button0 = Button(calc, text=' 0 ', fg='black', bg='light green', command=lambda: press(0), height=1, width=7) 
    button0.grid(row=5, column=0)
    clear = Button(calc, text='Clear', fg='black', bg='light green',command=clear, height=1, width=7) 
    clear.grid(row=5, column=1)
    plusik = Button(calc, text=' + ', fg='black', bg='light green', command=lambda: press("+"), height=1, width=7)
    plusik.grid(row=2, column=3) 
    minusik = Button(calc, text=' - ', fg='black', bg='light green', command=lambda: press("-"), height=1, width=7) 
    minusik.grid(row=3, column=3) 
    umnojit = Button(calc, text=' * ', fg='black', bg='light green', command=lambda: press("*"), height=1, width=7) 
    umnojit.grid(row=4, column=3) 
    podelit = Button(calc, text=' / ', fg='black', bg='light green', command=lambda: press("/"), height=1, width=7)
    podelit.grid(row=5, column=3) 
    ravno = Button(calc, text=' = ', fg='black', bg='light green', command=ravno, height=1, width=7) 
    ravno.grid(row=5, column=2) 
    calc.mainloop()

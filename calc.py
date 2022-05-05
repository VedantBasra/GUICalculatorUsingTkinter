import tkinter as tk

calc = ""

#function for input in calculator
def add_to_calc(symbol):
    global calc
    calc += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calc)

#evaluating the input
def eval_calc():
    global calc
    try:
        result= str(eval(calc))
        calc= ""
        text_result.delete(1.0,"end")
        text_result.insert(1.0, result)
    except:
        clear()
        text_result.insert(1.0, "Error")

#function for clearing the input field
def clear():
    global calc
    calc = ""
    text_result.delete(1.0,"end")

#defining the window and its geometry
win = tk.Tk()
win.geometry('294x275')
win.resizable(0,0)

#making the text input field
text_result = tk.Text(win, height=1.5,width=16,font=("Arial",24))
text_result.grid(columnspan=5)

#defining the buttons
#number buttons
bt1 = tk.Button(win,text="1",command=lambda: add_to_calc(1),width=5,font=("Arial",14))
bt1.grid(row=2,column=1)

bt2 = tk.Button(win,text="2",command=lambda: add_to_calc(2),width=5,font=("Arial",14))
bt2.grid(row=2,column=2)

bt3 = tk.Button(win,text="3",command=lambda: add_to_calc(3),width=5,font=("Arial",14))
bt3.grid(row=2,column=3)

bt4 = tk.Button(win,text="4",command=lambda: add_to_calc(4),width=5,font=("Arial",14))
bt4.grid(row=3,column=1)

bt5 = tk.Button(win,text="5",command=lambda: add_to_calc(5),width=5,font=("Arial",14))
bt5.grid(row=3,column=2)

bt6 = tk.Button(win,text="6",command=lambda: add_to_calc(6),width=5,font=("Arial",14))
bt6.grid(row=3,column=3)

bt7 = tk.Button(win,text="7",command=lambda: add_to_calc(7),width=5,font=("Arial",14))
bt7.grid(row=4,column=1)

bt8 = tk.Button(win,text="8",command=lambda: add_to_calc(8),width=5,font=("Arial",14))
bt8.grid(row=4,column=2)

bt9 = tk.Button(win,text="9",command=lambda: add_to_calc(9),width=5,font=("Arial",14))
bt9.grid(row=4,column=3)

bt0 = tk.Button(win,text="0",command=lambda: add_to_calc(0),width=5,font=("Arial",14))
bt0.grid(row=5,column=2)

#function buttons
bt_plus = tk.Button(win,text="+",command=lambda: add_to_calc("+"),width=5,font=("Arial",14))
bt_plus.grid(row=2,column=4)

bt_minus = tk.Button(win,text="-",command=lambda: add_to_calc("-"),width=5,font=("Arial",14))
bt_minus.grid(row=3,column=4)

bt_multi = tk.Button(win,text="*",command=lambda: add_to_calc("*"),width=5,font=("Arial",14))
bt_multi.grid(row=4,column=4)

bt_div = tk.Button(win,text="/",command=lambda: add_to_calc("/"),width=5,font=("Arial",14))
bt_div.grid(row=5,column=4)

bt_openp = tk.Button(win,text="(",command=lambda: add_to_calc("("),width=5,font=("Arial",14))
bt_openp.grid(row=5,column=1)

bt_closep = tk.Button(win,text=")",command=lambda: add_to_calc(")"),width=5,font=("Arial",14))
bt_closep.grid(row=5,column=3)

bt_eq = tk.Button(win,text="=",command=eval_calc,width=11,font=("Arial",14))
bt_eq.grid(row=6,column=1, columnspan=2)

bt_clr = tk.Button(win,text="Clear",command=clear,width=11,font=("Arial",14))
bt_clr.grid(row=6,column=3, columnspan=2)
win.mainloop()

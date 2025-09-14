from tkinter import *

root=Tk()
root.geometry("650x700")
root.title("Calculator")

def click(value):
    if value == "Delete":
        ent.delete(0, END)
    elif value == "=":
        try:
            res = eval(ent.get())
            ent.delete(0,END)
            ent.insert(END,(res))
        except Exception as e:
            ent.delete(0, END)
            ent.insert(END, 'Error')
    
    elif(value=='Backspace'):
        current_text = ent.get()
        ent.delete(0, END)
        ent.insert(0, current_text[:-1])
    else:
        ent.insert(END, value)
    
    



button=[
'9','8','7','Delete',
'6','5','4','/',
'3','2','1','+',
'0','-','*','=',
'Backspace'


]
row_val=1
col_val=0
ent=Entry(root,font=('ariel 27 '),justify='right',borderwidth=10,relief=SUNKEN)
ent.grid(row=0,column=0,ipadx=10,ipady=20,columnspan=6)
for btn in button:
    Button(root, text=btn,height=5,width=10,font=16,command=lambda value=btn: click(value),bg='orange').grid(row=row_val, column=col_val,pady=2,padx=2)
    col_val+=1
    if(col_val>=4):
        col_val=0
        row_val+=1




root.mainloop()
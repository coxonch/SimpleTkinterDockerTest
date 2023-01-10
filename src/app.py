from tkinter import *
import tkinter.ttk as ttk
import connection

db = "./sqlite.db" #container db location

root = Tk()
root.title("Python - Display SQLite3 Data In TreeView")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 1000
height = 800
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(1,1)

#==================================FRAME==============================================
Top = Frame(root, width=700, height=50, bd=9, relief="raise")
Top.pack(side=TOP)
Button_Group=Frame(root, width=700, height=50)
Button_Group.pack(side=TOP)
Buttons = Frame(Button_Group, width=200, height=50)
Buttons.pack(side=LEFT)
Buttons1 = Frame(Button_Group, width=500, height=50)
Buttons1.pack(side=RIGHT)

V_Group=Frame(root, width=700, height=50,background='red')
V_Group.pack(side=TOP)
VL_Group=Frame(V_Group, width=700, height=50)
VL_Group.pack(side=LEFT)
Labels = Frame(VL_Group, width=200, height=50)
Labels.pack(side=LEFT)
Entrys = Frame(VL_Group, width=500, height=50)
Entrys.pack(side=LEFT)

Body = Frame(root, width=700, height=300, bd=8, relief="raise")
Body.pack(side=BOTTOM, expand=True, fill='both')
 
#==================================LABEL WIDGET=======================================
txt_title = Label(Top, width=300, font=('arial', 24), text = "Python - Display SQLite3 Data In TreeView")
txt_title.pack()
l1=Label(Buttons1,text='Output here',font=20) # display message
l1.pack(side=RIGHT)

#==================================METHODS============================================
def populateView(filter):
    tree.delete(*tree.get_children())
    print("attempting connection")
    connection.Database(db)
    print("connection extablished")
    connection.cursor.execute("SELECT * FROM `windchill_vault_20220224` where column4 like ?  ORDER BY `column14` ASC LIMIT 100 ", ('%'+filter+'%',))    
    fetch = connection.cursor.fetchall()
    columns = [column[0] for column in connection.cursor.description]
    # Headings of respective columns
    try:
        # column identifiers 
        tree["columns"] = columns
        
        for i in columns:
            tree.column(i,stretch=NO, minwidth=0, width=200)
            tree.heading(i, text =i)
    except Exception as e:
        print(e)

    tree['show'] = 'headings'#remove empty first column

    for data in fetch:
        tree.insert('', 'end', values=data)

    addWidgets(columns)

    connection.cursor.close()
    connection.conn.close()
    
    return fetch, columns

ref=[] # to store the references widgets
def addWidgets(columns):
    for j , name in enumerate(columns):
        l=Label(Labels,text=name,font=20,fg='white')
        l.grid(row=j,column=0,padx=3, pady= 6)
        
        my_search = StringVar(name=f'{j:02}')
        e = Entry(Entrys, font=20,bg='gray',textvariable=my_search) 
        e.grid(row=j, column=1,padx=10,pady=3) 
        my_search.trace("w", lambda name, index, mode, sv=my_search: filterTreeView(sv))

        ref.append(e) # store references 

def my_check():
    my_flag=False
    for w in ref:
        if(len(w.get())<3):
            my_flag=True
    if(my_flag==False):
        l1.config(text="Form can be submitted",fg='green')
    else:
        l1.config(text="Fill all the entries",fg='red' )
    l1.after(3000, lambda: l1.config(text=''))

def filterTreeView(sv):
    search = sv.get().capitalize()
    # first clear the treeview
    tree.delete(*tree.get_children())
    # then insert matched items into treeview
    # TODO: uncomment
    try:
        for item in data_rows:
            print()
            index=int(str(sv))
            print(f'{index:02}')
            print(index)
            if search in item[index]:
                tree.insert("", "end", values=item)
    except Exception as e:
        print(e)

#==================================BUTTONS WIDGET=====================================
btn_display = Button(Buttons, width=15, text="Display All", command=populateView)
btn_display.pack(side=LEFT,)

b1=Button(Buttons1,text='Search', bg='lightgreen',command=lambda: my_check(),font=18)
b1.pack(side=LEFT)
 
#==================================LIST WIDGET========================================
scrollbary = Scrollbar(Body, orient=VERTICAL)
scrollbarx = Scrollbar(Body, orient=HORIZONTAL)
tree = ttk.Treeview(Body, selectmode ='browse',yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
tree.grid(row=0,column=1,padx=30,pady=20)
tree.pack(expand=True, fill='both')

#==================================INITIALIZATION=====================================
# Populate data
data_rows,columns = populateView('{$CAD_NAME}')

if __name__ == '__main__':
    root.mainloop()
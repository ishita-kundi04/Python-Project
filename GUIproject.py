from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import json

win = Tk()

win.geometry("1100x700+0+0")
win.resizable(height=0,width=0)

win.title('Chitkara University')


win.configure(background='white')
frame=LabelFrame(win,height=440,width=800,padx=10,pady=10)
frame.place(x=150,y=100,height=440,width=800)


tc = ttk.Notebook(frame)
t1 = ttk.Frame(tc)
t2 = ttk.Frame(tc)
t3 = ttk.Frame(tc)
t4 = ttk.Frame(tc)
t5 = ttk.Frame(tc)
t6 = ttk.Frame(tc)
tc.add(t1, text ='New Student')
tc.add(t2, text ='Display')
tc.add(t3, text ='Course Creation')
tc.add(t4, text ='Display Courses')
tc.add(t5, text ='Course Allocation')
tc.pack(expand = 1, fill ="both")

for i in range(6):
    t1.columnconfigure(i,weight=1)

ttk.Label(t1,text ="Enter Your Name",font = ("Times New Roman", 12)).grid(column =0,row = 0,columnspan=2,sticky=E, padx = 10, pady = 10)
name=Entry(t1,width=50,borderwidth=2)
name.grid(row=0,column=4,columnspan=2, padx=10, pady=10)

ttk.Label(t1,text ="Enter Your Roll No",font = ("Times New Roman", 12)).grid(column =0,row = 1,columnspan=2,sticky=E, padx = 10, pady = 10)
rollno = Entry(t1,width=50,borderwidth=2)
rollno.grid(row=1,column=4,columnspan=2, padx=10, pady=10)

ttk.Label(t1,text ="Choose Your Gender",font = ("Times New Roman", 12)).grid(column =0,row = 2,columnspan=2,sticky=E, padx = 10, pady = 10)


gender = StringVar()
Radiobutton(t1,text="Male",value="Male",variable=gender,tristatevalue=0,font = ("Times New Roman", 12)).grid(column =4,row = 2,columnspan=1, padx = 10, pady = 10)
Radiobutton(t1,text="Female",value="Female",variable=gender,tristatevalue=0,font = ("Times New Roman", 12)).grid(column =5,row = 2,columnspan=1, padx = 10, pady = 10)

ttk.Label(t1,text ="Adress of Correspondance",font = ("Times New Roman", 12)).grid(column =0,row = 3,columnspan=2,sticky=E, padx = 10, pady = 10)
address=Entry(t1,width=50,borderwidth=2)
address.grid(row=3,column=4,columnspan=2, padx = 10, pady = 10)

ttk.Label(t1,text ="Phone no",font = ("Times New Roman", 12)).grid(column =0,row = 4,columnspan=2,sticky=E, padx = 10, pady = 10)
phoneno=Entry(t1,width=50,borderwidth=2)
phoneno.grid(row=4,column=4,columnspan=2, padx = 10, pady = 10)


ttk.Label(t1, text = "Your Batch",font = ("Times New Roman", 12)).grid(column = 0,row = 5,columnspan=2, padx = 10, pady = 10,sticky=E) 
  
n=StringVar() 
batch = ttk.Combobox(t1,state='readonly', width = 18,textvariable=n) 

batch['values'] = ('Batch-2020','Batch-2019','Batch-2018','Batch-2017','Batch-2016')
 
batch.grid(column=5, row=5)

batch.current(0)

ttk.Label(t1,text ="Do you Want Hostel",font = ("Times New Roman", 12)).grid(column =0,row = 6,columnspan=2,sticky=E, padx = 10, pady = 10)
hostel=StringVar()
checkbox1= Checkbutton(t1, text = "Click here",variable = hostel,
                      onvalue = 'yes', 
                      offvalue = 'no', 
                      height = 2, 
                      width = 10)
checkbox1.grid(column =5,row = 6,columnspan=2,sticky=W, padx = 0, pady = 10)
checkbox1.deselect()

def clear1():
        name.delete(0,END)
        rollno.delete(0,END)
        address.delete(0,END)
        phoneno.delete(0,END)
def msg_submit():

    messagebox.showinfo("Status", "Record added")
    clear1()
def msg_clear():
        messagebox.showinfo("Status", "Cleared")
        clear1()
def std_det_add():
        d1=name.get()
        d2=rollno.get()
        d3=gender.get() 
        d4=address.get()
        d5=phoneno.get()
        d6=n.get()
        d7=hostel.get()
        d8=False
        if d7=='yes':
                d8=True
        msg_submit()
        r={ "Rollno": d2, "Name": d1,
         "Gender": d3,"address": d4,
         "Phone no": d5, "Batch": " Batch "+d6,
         "Hostel": d8
        }
        with open('Student.json') as f:
                data=json.load(f)
        data["Students"].append(r)
        data_serialise=json.dumps(data, indent=2)

        with open('Student.json','w') as f:
                json.dump(data,f,indent=1)

ttk.Button(t1,text="Submit", width = 18,command=std_det_add).grid(column =3,row = 7,columnspan=1,sticky=W, padx = 10, pady = 10)
ttk.Button(t1,text="Clear", width = 18,command=msg_clear).grid(column =4,row = 7,columnspan=1,sticky=W, padx = 10, pady = 10)



win2_tree = ttk.Treeview(t2)

win2_tree['columns']=('RollNo','Name','Gender','Address','Phoneno','Batch','Hostel')

win2_tree.column('#0',width=0,minwidth=0)
win2_tree.column('RollNo',width=80,minwidth=80)
win2_tree.column('Name',width=120,minwidth=120)
win2_tree.column('Gender',width=80,minwidth=80)
win2_tree.column('Address',width=120,minwidth=120)
win2_tree.column('Phoneno',width=120,minwidth=120)
win2_tree.column('Batch',width=120,minwidth=120)
win2_tree.column('Hostel',width=80,minwidth=80)

win2_tree.heading('#0',text="",anchor=W)
win2_tree.heading('RollNo',text="RollNo",anchor=W)
win2_tree.heading('Name',text="Name",anchor=W)
win2_tree.heading('Gender',text="Gender",anchor=W)
win2_tree.heading('Address',text="Address",anchor=W)
win2_tree.heading('Phoneno',text="Phoneno",anchor=W)
win2_tree.heading('Batch',text="Batch",anchor=W)
win2_tree.heading('Hostel',text="Hostel",anchor=W)

def show():
        win2_tree.delete(*win2_tree.get_children())

        with open('Student.json') as f:
                data=json.load(f)
        temp=0
        for i in data['Students']:
                win2_tree.insert(parent='',index='end',iid=temp,text='',values=(i["Rollno"],i["Name"],i["Gender"],i["address"],i["Phone no"],i["Batch"],i['Hostel']))
                temp+=1

        win2_tree.place(x=0,y=0,width=800)

Button(t2,text="Display",bg='black',fg='white',command=show).place(x=350,y=300)


for i in range(6):
    t3.columnconfigure(i,weight=1)
ttk.Label(t3,text ="Course ID",font = ("Times New Roman", 12)).grid(column =1,row = 0,columnspan=2,sticky=E, padx = 10, pady = 45)
courseid=Entry(t3,width=50,borderwidth=2)
courseid.grid(row=0,column=4,columnspan=2, padx = 10, pady = 45)

ttk.Label(t3,text ="Course Name",font = ("Times New Roman", 12)).grid(column =1,row = 1,columnspan=2,sticky=E, padx = 10, pady = 5)
coursename=Entry(t3,width=50,borderwidth=2)
coursename.grid(row=1,column=4,columnspan=2, padx = 10, pady = 45)

def clear9():
        courseid.delete(0,END)
        coursename.delete(0,END)

def msg_submit1():

    messagebox.showinfo("Save", "Course added")
    clear9()
def msg_clear1():
        messagebox.showinfo("Status", "Cleared")
        clear9()

def course_add():
        e1=courseid.get()
        e2=coursename.get()
        r={"CourseID": e1, "CourseName": e2}
        msg_submit1()
        with open('Course.json') as f:
                data1=json.load(f)
        data1["Courses"].append(r)
        data_serialise=json.dumps(data1, indent=2)

        with open('Course.json','w') as f:
                json.dump(data1,f,indent=1)



ttk.Button(t3,text="Submit",command=course_add, width = 18).grid(column =4,row = 2,columnspan=1,sticky=W, padx = 10, pady = 45)
ttk.Button(t3,text="Clear",command=msg_clear1, width = 18).grid(column =5,row = 2,columnspan=1,sticky=W, padx = 10, pady = 45)


win4_tree=ttk.Treeview(t4)

win4_tree['columns']=('CourseID','CourseName')

win4_tree.column('#0',width=0,minwidth=0)
win4_tree.column('CourseID',width=80,minwidth=80)
win4_tree.column('CourseName',width=120,minwidth=120)

win4_tree.heading('#0',text="",anchor=W)
win4_tree.heading('CourseID',text="CourseID",anchor=W)
win4_tree.heading('CourseName',text="CourseName",anchor=W)

def show1():
        win4_tree.delete(*win4_tree.get_children())
        with open('Course.json') as f:
                data1=json.load(f)
        temp=0
        for i in data1['Courses']:
                win4_tree.insert(parent='',index='end',iid=temp,text='',values=(i["CourseID"],i["CourseName"]))
                temp+=1

        win4_tree.place(x=0,y=0,width=800)

Button(t4,text="Display",bg='black',fg='white',command=show1).place(x=350,y=300)




for i in range(6):
    t5.columnconfigure(i,weight=1)
ttk.Label(t5,text ="Student Roll no",font = ("Times New Roman", 12)).grid(column =1,row = 0,columnspan=2,sticky=E, padx = 10, pady = 45)
rollno1=Entry(t5,width=50,borderwidth=2)
rollno1.grid(row=0,column=4,columnspan=2, padx = 10, pady = 45)

ttk.Label(t5,text ="Course Name",font = ("Times New Roman", 12)).grid(column =1,row = 1,columnspan=2,sticky=E, padx = 10, pady = 5)
s=StringVar() 
allocate = ttk.Combobox(t5, state='readonly',width = 48,textvariable=s) 

with open('Course.json') as f:
        data1=json.load(f) 
allo=[]
for i in data1['Courses']:
                allo.append(i['CourseName'])
def refresh():
        with open('Course.json') as f:
                data2=json.load(f)
        global allo
        allo=[]
        for i in data2['Courses']:
                allo.append(i['CourseName'])
        allocate['values']=allo
allocate['values'] = allo
allocate.grid(column = 4, row = 1, padx = 10, pady = 5,columnspan=2) 

allocate.current(1)

Button(t5,text="Refresh",bg='black',fg='white',command=refresh).place(x=350,y=300)

def clear2():
        rollno1.delete(0,END)

def msg_submit2():

    messagebox.showinfo("Save", "Course added")
    clear2()
def msg_clear2():
        messagebox.showinfo("Status", "Cleared")
        clear2()
with open('Course.json') as f:
        data5=json.load(f)
def return_courseID(cn):
        for i in data5['Courses']:
                if i['CourseName']==cn:
                        return i['CourseID']
def course_add1():
        f1=rollno1.get()
        f2=s.get()
        f3=return_courseID(f2)
        r={"Rollno": f1, "CourseID": f3}
        msg_submit2()
        with open('Allocation.json') as f:
                data3=json.load(f)
        data3["Stu_Course"].append(r)
        data_serialise=json.dumps(data3, indent=2)
        with open('Allocation.json','w') as f:
                json.dump(data3,f,indent=1)



ttk.Button(t5,text="Allocate",command=course_add1 ,width = 18).grid(column =4,row = 2,columnspan=1,sticky=W, padx = 10, pady = 45)
ttk.Button(t5,text="Clear", command=msg_clear2,width = 18).grid(column =5,row = 2,columnspan=1,sticky=W, padx = 10, pady = 45)



win6_tree = ttk.Treeview(t6)
win6_tree['columns']=('Rollno','CourseID')

win6_tree.column('#0',width=0,minwidth=0)
win6_tree.column('Rollno',width=80,minwidth=80)
win6_tree.column('CourseID',width=120,minwidth=120)

win6_tree.heading('#0',text="",anchor=W)
win6_tree.heading('Rollno',text="Rollno",anchor=W)
win6_tree.heading('CourseID',text="CourseID",anchor=W)

def show2():
        win6_tree.delete(*win6_tree.get_children())

        with open('Allocation.json') as f:
                data3=json.load(f)
        temp=0
        for i in data3['Stu_Course']:
                win6_tree.insert(parent='',index='end',iid=temp,text='',values=(i["Rollno"],i["CourseID"]))
                temp+=1

        win6_tree.place(x=0,y=0,width=800)

Button(t6,text="Display",bg='black',fg='white',command=show2).place(x=350,y=300)

win.mainloop()

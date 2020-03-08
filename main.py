# import all the modules
from tkinter import *
import sqlite3
import requests
from PIL import Image, ImageTk
import tkinter.messagebox
import datetime
import math
import os
import random

conn = sqlite3.connect("C://Users//Charanpreet//tutorial.db")
c = conn.cursor()

# date
date = datetime.datetime.now().date()
time=datetime.datetime.now().time()

# temporary lists like sessions
class Application:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        # frames
        self.left = Frame(master, width=1920, height=1080)
        self.left.pack(side=LEFT)

        # components
        self.heading = Label(self.left, text="Employee Management Application", font=('Comic Sans MS',35),fg='brown')
        self.heading.place(x=400, y=0)

        self.date_l = Label(self.left, text=" Date: " + str(date), font=('Comic Sans MS',14), fg='blue')
        self.date_l.place(x=1150, y=700)

        #self.date_l = Label(self.right, text="Today's time: " + str(time), font=('oemfixed 16 italic'), bg='light blue')
        #self.date_l.place(x=400, y=17)

        # table invoice==============================================================
        self.tkvar = StringVar(root)
        choices = { 'Employee','Manager'}
        self.tkvar.set('Select') # set the default option
        self.popupMenu =OptionMenu(self.left, self.tkvar, *choices)
        self.popupMenu.config(width=30,font=('Comic Sans MS',16))
        #self.l=Label(self.left, text="SCROLL DOWN",font=("Comic Sans MS Italic",18),fg="blue")
        #self.l.place(x=0,y=100)
        self.popupMenu.place(x=500,y=100)
        # enter stuff
        def change_dropdown(*args):
            p=self.tkvar.get()
            self.flag=0
            if p=='Employee':
                self.flag=0
                self.enterid = Label(self.left, text="Emp_ID", font=('Comic Sans MS',18), fg='black')
                self.enterid.place(x=400, y=200)

                self.enteride = Entry(self.left, width=23, font=('Comic Sans MS',18), fg='black')
                self.enteride.place(x=620, y=200)
                self.enteride.focus()

                self.enteridc = Label(self.left, text="Password", font=('Comic Sans MS',18), fg='black')
                self.enteridc.place(x=400, y=350)

                self.enteridd = Entry(self.left, width=23, font=('Comic Sans MS',18), fg='black')
                self.enteridd.place(x=620, y=350)
                self.enteridd.focus()

                # button
                self.search_btn = Button(self.left, text="Search",font=('Comic Sans MS',10), width=18, height=2, bg='light blue', command=self.ajax)
                self.search_btn.place(x=500, y=460)
            else:
                self.flag=1
                self.enterid = Label(self.left, text="Man_ID", font=('Comic Sans MS',18), fg='black')
                self.enterid.place(x=400, y=200)

                self.enteride = Entry(self.left, width=23, font=('Comic Sans MS',18), fg='black')
                self.enteride.place(x=620, y=200)
                self.enteride.focus()

                self.enteridc = Label(self.left, text="Password", font=('Comic Sans MS',18), fg='black')
                self.enteridc.place(x=400, y=350)

                self.enteridd = Entry(self.left, width=23, font=('Comic Sans MS',18), fg='black')
                self.enteridd.place(x=620, y=350)
                self.enteridd.focus()

                # button
                self.search_btn = Button(self.left, text="Search", font=('Comic Sans MS',10),width=18, height=2, bg='light blue', command=self.ajax)
                self.search_btn.place(x=500, y=460)
                        
        self.tkvar.trace('w', change_dropdown)
        self.master.bind("<Return>", self.ajax)
        

    def ajax(self, *args, **kwargs):
        self.get_id = self.enteride.get()
        self.get_passwd=self.enteridd.get()
        if self.flag==0:
            self.g=Toplevel()
            self.g.geometry('1920x1080')
            self.g.title('Employee Page')
            self.g.iconbitmap(r'C:\\Users\\Charanpreet\\Downloads\\py.ico')

            query = "SELECT * FROM employee WHERE emp_id=? and passwd=?"
            result = c.execute(query, (self.get_id,self.get_passwd, ))
            a=[]
            for self.r in result:
                self.get_ip = self.r[0]
                a.append(self.get_id)
                #i+=1
                self.get_passwd = self.r[1]
                self.get_email = self.r[5]
                self.get_salary=self.r[4]
                self.get_name = self.r[2]
                self.get_address = self.r[3]
            if(len(a)>0):
                if self.get_id == a[0]:
                    
                    try:
                        c.execute('update attendence set attend="present" where emp_id='+str(self.get_ip))
                        conn.commit()
                    except sqlite3.IntegrityError:
                        pass
                    self.l3 = Label(self.g, text="email:"+self.get_email, font=('Comic Sans MS',18), bg='light blue')
                    self.l3.place(x=0, y=100)
                    self.l4 = Label(self.g, text="salary:"+str(self.get_salary), font=('Comic Sans MS',18), bg='light blue')
                    self.l4.place(x=0, y=150)
                    self.l4 = Label(self.g, text="##################################", font=('Comic Sans MS' ,18 ), bg='light blue')
                    self.l4.place(x=0, y=200)
                    
                    self.add_to_cart_btn = Button(self.g, text="OK", width=22, height=2, bg='light blue', command=self.test)
                    self.add_to_cart_btn.place(x=350, y=460)
                    button=Button(self.g,text='Exit',font=('Comic Sans Ms',14),fg='green',command=self.g.quit)
                    button.place(x=1400,y=0)
            else:
                tkinter.messagebox.showinfo("error","INVALID ID or PASSWORD")
        elif self.flag==1:
            self.h=Toplevel()
            self.h.geometry('1920x1080')
            self.h.title('Manager Page')
            self.h.iconbitmap(r'C:\\Users\\Charanpreet\\Downloads\\py.ico')

            query = "SELECT * FROM manager WHERE manager_id=? and passwd=?"
            result = c.execute(query, (self.get_id,self.get_passwd, ))
            a=[]
            for self.r in result:
                self.get_ip = self.r[0]
                a.append(self.get_ip)
                #i+=1
                self.get_passwd = self.r[1]
                self.get_email = self.r[4]
                self.get_name = self.r[2]
                self.get_address = self.r[3]
            if(len(a)>0):
                if self.get_ip == a[0]:
                    self.discount_l = Label(self.h, text="WELCOME!  "+self.get_name, font=('Comic Sans MS' ,18 ), bg='black',fg='white')
                    self.discount_l.place(x=600, y=100)
                    self.all = Button(self.h, text="ADD Employee", width=22, height=2, bg='orange', command=self.add)
                    self.all.place(x=500, y=460)
                    self.all = Button(self.h, text="Remove Employee", width=22, height=2, bg='orange', command=self.remove)
                    self.all.place(x=650, y=460)
                    # add to cart button
                    self.all = Button(self.h, text="GET STATUS", width=22, height=2, bg='orange', command=self.test)
                    self.all.place(x=800, y=460)  
                    button=Button(self.h,text='Exit',font=('Comic Sans Ms',14),fg='green',command=self.h.quit)
                    button.place(x=1400,y=0)  
            else:
                tkinter.messagebox.showinfo("error","INVALID ID or PASSWORD")
    def up(self,*args,**kwargs):
        if self.flag==0:
            q="update employee set "+self.var.get()+"=? where emp_id=?"
        else:
            q="update employee set emp_id=? where emp_id=?"
            c.execute(q,(self.enteri.get(),self.var.get()))
            
            d="update works_on set emp_id=? where emp_id=?"
            c.execute(d,(self.enteri.get(),self.var.get()))
            e="update leave set emp_id=? where emp_id=?"
            c.execute(e,(self.enteri.get(),self.var.get()))
            f=e="update attendence set emp_id=? where emp_id=?"
            c.execute(f,(self.enteri.get(),self.var.get()))
        conn.commit()
        tkinter.messagebox.showinfo("success!","change updated")


    def up_pas(self,*args,**kwargs):
        if self.enteri.get()==self.enteridn.get():
            q="update employee set "+self.var.get()+"=? where emp_id=?"
            c.execute(q,(self.enteri.get(),self.get_id))        #update wala ho gya h employee mein agar delete hua to karna h aur ye sab ,anager mein add karna h  
            conn.commit()
            tkinter.messagebox.showinfo('yipee..','updation successful')

        else:
            tkinter.messagebox.showinfo('passwd doesnot match','please enter same passwd')
    def updateHours(self,*args,**kwargs):
        h=Toplevel()
        h.geometry("800x800")
        h.title("UPDATE hours")
        h.iconbitmap(r'C:\\Users\\Charanpreet\\Downloads\\py.ico')

        frame= Frame(h, width=900, height=800, bg="white")
        frame.pack()
        self.var = StringVar(h)
        result=c.execute('select emp_id from employee')
        choices=[]
        for r in result:
            choices.append(str(r[0]))
        self.var.set('select') # set the default option
        popupMenu =OptionMenu(frame, self.var, *choices)
        l=Label(frame,text="Update hours",font=("Comic Sans MS Bold",18),fg="black")
        l.place(x=0,y=0)
        popupMenu.place(x=0,y=150)
        button=Button(frame,text='OK',font=('Comic Sans Ms',14),fg='green',command=self.go)
        button.place(x=200,y=200)
    def got(self,*args,**kwargs):
        c.execute('update works_on set hours=? where p_id=? and emp_id=?',(self.enterg.get(),str(self.vari.get()),self.var.get()))
        tkinter.messagebox.showinfo('success','hours updated')
        conn.commit()
    def gone(self,*args,**kwargs):
        h=Toplevel()
        h.geometry("800x800")
        h.title("UPDATE hours")
        h.iconbitmap(r'C:\\Users\\Charanpreet\\Downloads\\py.ico')

        frame= Frame(h, width=900, height=800, bg="white")
        frame.pack()
        l=Label(frame,text="Update hours:",font=("Comic Sans MS Bold",18),fg="black")
        l.place(x=420,y=350)
        self.enterg = Entry(frame, width=23, font=('Comic Sans MS',18), fg='black')
        self.enterg.place(x=620, y=350)
        self.enterg.focus()
        button=Button(frame,text='OK',font=('Comic Sans Ms',14),fg='green',command=self.got)
        button.place(x=500,y=400)
    def go(self,*args,**kwargs):
        h=Toplevel()
        h.geometry("800x800")
        h.title("UPDATE hours")
        h.iconbitmap(r'C:\\Users\\Charanpreet\\Downloads\\py.ico')

        frame= Frame(h, width=900, height=800, bg="white")
        frame.pack()
        self.vari = StringVar(h)
        result=c.execute('select p_id from works_on where emp_id='+self.var.get())
        choices=[]
        for r in result:
            choices.append(r[0])
        self.vari.set('select') # set the default option
        popupMenu =OptionMenu(frame, self.vari, *choices)
        l=Label(frame,text="Update hours",font=("Comic Sans MS Bold",18),fg="black")
        l.place(x=0,y=0)
        popupMenu.place(x=0,y=150)
        button=Button(frame,text='OK',font=('Comic Sans Ms',14),fg='green',command=self.gone)
        button.place(x=200,y=200)
    def up_emp(self,*args,**kwargs):
            h=Toplevel()
            h.geometry("800x800")
            h.title("UPDATE emp_id")
            h.iconbitmap(r'C:\\Users\\Charanpreet\\Downloads\\py.ico')

            frame= Frame(h, width=900, height=800, bg="white")
            frame.pack()
            self.var = StringVar(h)
            result=c.execute('select emp_id from employee')
            choices=[]
            for r in result:
                choices.append(str(r[0]))
            self.var.set('select') # set the default option
            popupMenu =OptionMenu(frame, self.var, *choices)
            l=Label(frame,text="Update emp_id",font=("Comic Sans MS Bold",18),fg="black")
            l.place(x=0,y=0)
            popupMenu.place(x=0,y=150)
            self.enter = Label(frame, text="NEW ID:", font=('times 18 bold'), fg='black')
            self.enter.place(x=0, y=350)

            self.enteri = Entry(frame, width=23, font=('Comic Sans MS',18), fg='black')
            self.enteri.place(x=220, y=350)
            self.enteri.focus() 
            button=Button(frame,text='OK',font=('Comic Sans Ms',14),fg='green',command=self.up)
            button.place(x=200,y=500)
            
            '''up_name = Button(frame, text="OK", width=22, height=2, bg='orange',command=self.up)
            up_name.place(x=110, y=460)'''
            button=Button(frame,text='Exit',font=('Comic Sans Ms',14),fg='green',command=h.quit)
            button.place(x=1400,y=0)
    def update(self,*args,**kwargs):
        h=Toplevel()
        h.geometry("800x800")
        h.title("UPDATE employee")
        h.iconbitmap(r'C:\\Users\\Charanpreet\\Downloads\\py.ico')

        frame= Frame(h, width=900, height=800, bg="white")
        frame.pack()
        self.var = StringVar(h)
        choices = { 'emp_id','name','salary','address','email','passwd'}
        self.var.set('select') # set the default option
        popupMenu =OptionMenu(frame, self.var, *choices)
        l=Label(frame,text="Update menu",font=("Comic Sans MS Bold",18),fg="black")
        l.place(x=0,y=0)
        popupMenu.place(x=0,y=150)
        
        def chang_dropdown(*args):
            if self.var.get()=='name':
                self.enter = Label(frame, text="NEW NAME:", font=('times 18 bold'), fg='black')
                self.enter.place(x=0, y=350)

                self.enteri = Entry(frame, width=23, font=('Comic Sans MS',18), fg='black')
                self.enteri.place(x=220, y=350)
                self.enteri.focus() 
                up_name = Button(frame, text="OK", width=22, height=2, bg='orange',command=self.up)
                up_name.place(x=110, y=460)
                button=Button(frame,text='Exit',font=('Comic Sans Ms',14),fg='green',command=h.quit)
                button.place(x=1400,y=0)
            elif self.var.get()=='emp_id':
                tkinter.messagebox.showinfo("error","cannot update emp_id..")
                '''self.enter = Label(frame, text="NEW ID:", font=('times 18 bold'), fg='black')
                self.enter.place(x=0, y=350)

                self.enteri = Entry(frame, width=23, font=('Comic Sans MS',18), fg='black')
                self.enteri.place(x=220, y=350)
                self.enteri.focus() 
                up_name = Button(frame, text="OK", width=22, height=2, bg='orange',command=self.up)
                up_name.place(x=110, y=460)
                button=Button(frame,text='Exit',font=('Comic Sans Ms',14),fg='green',command=h.quit)
                button.place(x=140,y=0)'''
                #tkinter.messagebox.showinfo('Acess Denied!','cannot update emp_id ')
            elif self.var.get()=='salary':
                tkinter.messagebox.showinfo('Acess Denied!','cannot update salary ')
            elif self.var.get()=='address':
                self.enter = Label(frame, text="NEW ADDRESS:", font=('times 18 bold'), fg='black')
                self.enter.place(x=0, y=350)
                self.enteri = Entry(frame, width=23, font=('Comic Sans MS',18), fg='black')
                self.enteri.place(x=220, y=350)
                self.enteri.focus()
                up_name = Button(frame, text="OK", width=22, height=2, bg='orange',command=self.up)
                up_name.place(x=110, y=460)
                button=Button(frame,text='Exit',font=('Comic Sans Ms',14),fg='green',command=h.quit)
                button.place(x=1400,y=0)
                
            elif self.var.get()=='email':
                self.enter = Label(frame, text="NEW EMAIL:", font=('times 18 bold'), fg='black')
                self.enter.place(x=0, y=350)
                self.enteri = Entry(frame, width=23, font=('Comic Sans MS',18), fg='black')
                self.enteri.place(x=220, y=350)
                self.enteri.focus()
                up_name = Button(frame, text="OK", width=22, height=2, bg='orange',command=self.up)
                up_name.place(x=110, y=460)
                button=Button(frame,text='Exit',font=('Comic Sans Ms',14),fg='green',command=h.quit)
                button.place(x=1400,y=0)
            elif self.var.get()=='passwd':
                self.enter = Label(frame, text="NEW PASSWD:", font=('times 18 bold'), fg='black')
                self.enter.place(x=0, y=350)
                self.enteri = Entry(frame, width=23, font=('Comic Sans MS',18), fg='black')
                self.enteri.place(x=220, y=350)
                self.enteri.focus()
                enteride = Label(frame, text="confirm PASSWD:", font=('times 18 bold'), fg='black')
                enteride.place(x=0, y=450)
                self.enteridn = Entry(frame, width=23, font=('Comic Sans MS',18), fg='black')
                self.enteridn.place(x=220, y=450)
                self.enteridn.focus()
                up_name = Button(frame, text="OK", width=22, height=2, bg='orange',command=self.up_pas)
                up_name.place(x=110, y=600)
                button=Button(frame,text='Exit',font=('Comic Sans Ms',14),fg='green',command=h.quit)
                button.place(x=1400,y=0)
                
        self.var.trace('w', chang_dropdown)
         
    

    def delete(self,*args,**kwargs):
        f="SELECT * FROM employee where emp_id=?"
        re=c.execute(f,(self.enteridp.get(),))
        resu=[]
        for resu in re:
            pe=resu[0]
            qe=resu[1]
            me=resu[2]
            ve=resu[3]
            fe=resu[4]
            ce=resu[5]
        if len(resu)==0:
            tkinter.messagebox.showinfo("employee does not exist")
            return
        else:
            c.execute("delete from employee where emp_id="+self.enteridp.get())
            c.execute("delete from works_on where emp_id="+self.enteridp.get())
            c.execute("delete from leave where emp_id="+self.enteridp.get())
            c.execute("delete from attendence where emp_id="+self.enteridp.get())

            #re=c.execute(g,(self.enteridp.get(),))
            conn.commit()
            tkinter.messagebox.showinfo("Success", "Done everything smoothly  ")  
    def remove(self,*args,**kwargs):
        d=Toplevel()
        d.geometry("1920x1080")
        d.title("remove employee")
        d.iconbitmap(r'C:\\Users\\Charanpreet\\Downloads\\py.ico')

        f=Frame(d,width=900,height=900,bg='white')
        f.pack()
        self.l5=Label(f,text="emp_id:",font=('Comic Sans MS',18),fg='black')
        self.l5.place(x=0,y=0)
        self.enteridp = Entry(f, width=23, font=('Comic Sans MS',18), fg='black')
        self.enteridp.place(x=220, y=0)
        self.enteridp.focus()
        self.all = Button(f, text="DELETE", width=22, height=2, bg='orange', command=self.delete)
        self.all.place(x=350, y=460)
        button=Button(f,text='Exit',font=('Comic Sans Ms',14),fg='green',command=d.quit)
        button.place(x=1400,y=0)
    def end(self, *args, **kwargs):
        c.execute('update attendence set attend="absent" where attend="present"')
        conn.commit()
    def test(self, *args, **kwargs):
        # get the quantity value and from the database
        if self.flag==1:
            h=Toplevel()
            h.geometry('1920x1080')
            h.title('employee database')
            h.iconbitmap(r'C:\\Users\\Charanpreet\\Downloads\\py.ico')
            button=Button(h,text='End of the day',font=('Comic Sans Ms',14),fg='green',command=self.end)
            button.place(x=1200,y=0)
            '''l=Button(h,text='Update hours',font=('Comic Sans Ms',14),fg='green',command=self.end)
            l.place(x=1100,y=0)'''
            p="Select e.emp_id,e.name,e.address,e.salary,e.email,l.leave_from,l.leave_to,w.p_name,w.hours from employee e,leave l,works_on w where e.emp_id=l.emp_id and l.emp_id=w.emp_id"
            res=c.execute(p)
            length=0
            breadth=100
            for r in res:
                self.l4=Label(h,text="emp_id:"+str(r[0]),font=('Comic Sans MS',18),fg='brown')
                self.l4.place(x=length,y=breadth+150)
                self.l4=Label(h,text="|",font=('Comic Sans MS',18),bg='white')
                self.l4.place(x=length+220,y=breadth+150)
                self.l4=Label(h,text="name:"+str(r[1]),font=('Comic Sans MS',18),fg='brown')
                self.l4.place(x=length,y=breadth+200)
                self.l4=Label(h,text="|",font=('Comic Sans MS',18),bg='white')
                self.l4.place(x=length+220,y=breadth+200)
                self.l4=Label(h,text="email:"+str(r[4]),font=('Comic Sans MS',18),fg='brown')
                self.l4.place(x=length,y=breadth+250)
                self.l4=Label(h,text="|",font=('Comic Sans MS',18),bg='white')
                self.l4.place(x=length+220,y=breadth+250)
                self.l4=Label(h,text="salary:"+str(r[3]),font=('Comic Sans MS',18),fg='brown')
                self.l4.place(x=length,y=breadth+300)
                self.l4=Label(h,text="|",font=('Comic Sans MS',18),bg='white')
                self.l4.place(x=length+220,y=breadth+300)
                self.l4=Label(h,text="address:"+str(r[2]),font=('Comic Sans MS',18),fg='brown')
                self.l4.place(x=length,y=breadth+350)
                self.l4=Label(h,text="|",font=('Comic Sans MS',18),bg='white')
                self.l4.place(x=length+220,y=breadth+350)
                self.l4=Label(h,text="leave from"+r[5],font=('Comic Sans MS',18),fg='brown')
                self.l4.place(x=length,y=breadth+400)
                self.l4=Label(h,text="|",font=('Comic Sans MS',18),bg='white')
                self.l4.place(x=length+220,y=breadth+400)
                self.l4=Label(h,text="leave to"+r[6],font=('Comic Sans MS',18),fg='brown')
                self.l4.place(x=length,y=breadth+450)
                self.l4=Label(h,text="|",font=('Comic Sans MS',18),bg='white')
                self.l4.place(x=length+220,y=breadth+450)
                self.l4=Label(h,text="project:"+r[7],font=('Comic Sans MS',18),fg='brown')
                self.l4.place(x=length,y=breadth+500)
                self.l4=Label(h,text="|",font=('Comic Sans MS',18),bg='white')
                self.l4.place(x=length+220,y=breadth+500)
                if r[8]<5:
                    self.l4=Label(h,text="amt of hours of work required="+str(5-r[8]))
                    self.l4.place(x=length,y=breadth+600)

                self.l4=Label(h,text="hours:"+str(r[8]),font=('Comic Sans MS',18),fg='brown')
                self.l4.place(x=length,y=breadth+550)
                self.l4=Label(h,text="|",font=('Comic Sans MS',18),bg='white')
                self.l4.place(x=length+220,y=breadth+550)
                length=length+230
                self.po = Button(h, text="update hours", width=22, height=2, bg='orange', command=self.updateHours)
                self.po.place(x=1000, y=0)
                self.powe = Button(h, text="update emp_id", width=22, height=2, bg='orange', command=self.up_emp)
                self.powe.place(x=800, y=0)
                
        else:
            self.j = Button(self.g, text="update my profile", width=22, height=2, bg='orange', command=self.update)
            self.j.place(x=1200, y=0)
            button=Button(self.g,text='Exit',font=('Comic Sans Ms',14),fg='green',command=self.g.quit)
            button.place(x=1400,y=0)

    def add(self, *args, **kwargs):
        self.x=0
        b=Toplevel()
        b.geometry("1920x1080")
        b.title("add employee")
        b.iconbitmap(r'C:\\Users\\Charanpreet\\Downloads\\py.ico')

        self.l5=Label(b,text="emp_id:",font=('Comic Sans MS',18),fg='black')
        self.l5.place(x=400,y=80)
        self.enterida = Entry(b, width=23, font=('Comic Sans MS',18), fg='black')
        self.enterida.place(x=620, y=80)
        self.enterida.focus()
        self.l5=Label(b,text="passwd:",font=('Comic Sans MS',18),fg='black')
        self.l5.place(x=400,y=160)
        self.enteridb = Entry(b, width=23, font=('Comic Sans MS',18), fg='black')
        self.enteridb.place(x=620, y=160)
        self.enteridb.focus()
        self.l5=Label(b,text="name",font=('Comic Sans MS',18),fg='black')
        self.l5.place(x=400,y=240)
        self.enterids = Entry(b, width=23, font=('Comic Sans MS',18), fg='black')
        self.enterids.place(x=620, y=240)
        self.enterids.focus()
        self.l5=Label(b,text="address",font=('Comic Sans MS',18),fg='black')
        self.l5.place(x=400,y=320)
        self.enteridh = Entry(b, width=23, font=('Comic Sans MS',18), fg='black')
        self.enteridh.place(x=620, y=320)
        self.enteridh.focus()
        self.l5=Label(b,text="email:",font=('Comic Sans MS',18),fg='black')
        self.l5.place(x=400,y=400)
        self.enteridg = Entry(b, width=23, font=('Comic Sans MS',18), fg='black')
        self.enteridg.place(x=620, y=400)
        self.enteridg.focus()
        self.l5=Label(b,text="salary:",font=('Comic Sans MS',18),fg='black')
        self.l5.place(x=400,y=480)
        self.enteridf = Entry(b, width=23, font=('Comic Sans MS',18), fg='black')
        self.enteridf.place(x=620, y=480)
        self.enteridf.focus()
        self.l5=Label(b,text="p_id:",font=('Comic Sans MS',18),fg='black')
        self.l5.place(x=400,y=560)
        self.enteridk = Entry(b, width=23, font=('Comic Sans MS',18), fg='black')
        self.enteridk.place(x=620, y=560)
        self.enteridk.focus()
        self.l5=Label(b,text="p_name:",font=('Comic Sans MS',18),fg='black')
        self.l5.place(x=400,y=640)
        self.enteridl = Entry(b, width=23, font=('Comic Sans MS',18), fg='black')
        self.enteridl.place(x=620, y=640)
        self.enteridl.focus()

            # insert into the transaction
        self.all = Button(b, text="OK", width=22, height=2, bg='orange',command=self.done)
        self.all.place(x=500, y=700)
        button=Button(b,text='Exit',font=('Comic Sans Ms',14),fg='green',command=b.quit)
        button.place(x=1400,y=0)
        
    def done(self,*args, **kwargs):
        initial = "SELECT * FROM employee WHERE emp_id=? "
        result = c.execute(initial,(self.enterida.get(),))
        v=[]
        for v in result:
                self.get_ip =v[0]
                #i+=1
                self.get_passwd = v[1]
                self.get_email = v[4]
                self.get_name = v[2]
                self.get_address = v[3]
        if len(v)>0:
            tkinter.messagebox.showinfo("error","ID already exists!")
        else:
            if int(self.enterida.get())>0:
                sql2 = "INSERT INTO employee (emp_id, passwd, name, address, salary, email) VALUES (?, ?, ?, ?, ?, ?)"
                c.execute(sql2, (self.enterida.get(),self.enteridb.get(),self.enterids.get(),self.enteridh.get(),self.enteridf.get(),self.enteridg.get()))
                sql1 = "INSERT INTO works_on (p_id, p_name,emp_id, hours) VALUES (?, ?, ?, ?)"
                c.execute(sql1,(self.enteridk.get(),self.enteridl.get(),self.enterida.get(),'0'))
                sql3 = "INSERT INTO leave (emp_id, leave_from,leave_to) VALUES (?, ?, ?)"
                c.execute(sql3,(self.enterida.get(),'--','--'))
                sql4 = "INSERT INTO attendence (emp_id, emp_name,attend) VALUES (?, ?, ?)"
                c.execute(sql4,(self.enterida.get(),self.enterids.get(),'absent'))
                conn.commit()
                self.x += 1
            else:
                tkinter.messagebox.showinfo("Error!","Invalid id,Enter positive value")

root = Tk()
root.iconbitmap(r'C:\\Users\\Charanpreet\\Downloads\\py.ico')
b = Application(root)

root.geometry("1920x1080+0+0")
button=Button(root,text='Exit',font=('Comic Sans Ms',14),fg='green',command=root.quit)
button.place(x=1400,y=0)
root.mainloop()

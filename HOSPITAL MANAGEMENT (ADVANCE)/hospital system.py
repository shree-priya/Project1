
import tkinter as tk
import mysql.connector as mys
from tkinter.font import Font
from tkinter import messagebox
#window=tk.Tk()

#run doctor main page
def Doctor():
    window=tk.Tk()
    window.title("HOSPITAL MANAGEMEANT SYSTEM")
    window.iconbitmap("favicon.ico")
    window.config(bg="violet")
    myfont=Font(family='times',size=20,weight="bold", slant="italic")
    la=tk.Label(window,text="Hospital Managmeant",font=myfont,bg="#0a3d62",fg="white",padx=40,pady=20,relief="raised")
       
    #la1=tk.Button(window,text="Doctor Details",font=myfont)
    fontq=Font(family='times',size=15,weight="bold")
    ba2=tk.Button(window,text="Doctor Entry",font=fontq,bg="white",fg="Black",activebackground="blue",width="30",command=ddetails)
    ba2.pack(pady="50")

    ba3=tk.Button(window,text="Show Doctor Details",font=fontq,bg="white",fg="Black",activebackground="blue",width="30",command=sddetails)
    ba3.pack(pady="50")

    ba4=tk.Button(window,text="Update Doctor Details",font=fontq,bg="white",fg="Black",activebackground="blue",width="30",command=uddetails)
    ba4.pack(pady="50")

    
    la.pack()
    
    window.minsize(600,600)
    window.mainloop()
#PATIENT MENU
def Patient():
    window=tk.Tk()
    window.title("HOSPITAL MANAGEMEANT SYSTEM")
    window.iconbitmap("favicon.ico")
    window.config(bg="violet")
    myfont=Font(family='times',size=20,weight="bold", slant="italic")
    la=tk.Label(window,text="Hospital Managmeant",font=myfont,bg="#0a3d62",fg="white",padx=40,pady=20,relief="raised")
       
    #la1=tk.Button(window,text="Doctor Details",font=myfont)
    fontq=Font(family='times',size=15,weight="bold")
    ba2=tk.Button(window,text="Patient Entry",font=fontq,bg="white",fg="Black",activebackground="blue",width="30",command=pdetails)
    ba2.pack(pady="50")

    ba3=tk.Button(window,text="Show Patient Details",font=fontq,bg="white",fg="Black",activebackground="blue",width="30",command=spdetails)
    ba3.pack(pady="50")

    ba4=tk.Button(window,text="Fetch Patient Details",font=fontq,bg="white",fg="Black",activebackground="blue",width="30",command=updetails)
    ba4.pack(pady="50")

    
    la.pack()
    
    window.minsize(600,600)
    window.mainloop()
#update doctor details

def uddetails():
    window=tk.Tk()
    window.title("HOSPITAL MANAGEMEANT SYSTEM")
    window.iconbitmap("favicon.ico")
    window.config(bg="violet")
    myfont=Font(family='times',size=20,weight="bold", slant="italic")
    fontq=Font(family='times',size=15,weight="bold")
    la=tk.Label(window,text="Hospital Managmeant",font=myfont,width="80",bg="#0a3d62",fg="white",padx=40,pady=20,relief="raised")
    la.pack()
    ldd8=tk.Label(window,text="Enter  doctor name:",font=myfont,fg="black")
    techdd2=tk.Entry(window,width=30,font=("times",20),bg="white",fg="black")
    ldd8.pack(pady="25")
    techdd2.pack()

    ldd9=tk.Label(window,text="Enter  doctor updated salary:",font=myfont,fg="black")
    techdd1=tk.Entry(window,width=30,font=("times",20),bg="white",fg="black")
    ldd9.pack(pady="25")
    techdd1.pack()

    def upd():
     dsal1=techdd1.get()
     dname1=techdd2.get()
     con= mys.connect(host='localhost',user='root',passwd='rk2004',database="tk")
     cur=con.cursor()
           
     Query="update Doctor_details set dsal='{}' where dname='{}';".format(dsal1,dname1)
     cur.execute(Query)
     con.commit()
     messagebox.showinfo("updated","successfully updated")
     sumbit()
    ba=tk.Button(window,text="Proceed->",font=fontq,bg="green",fg="white",activebackground="blue",width="10",command=upd)

    

    ba1=tk.Button(window,text="Cancel ×",font=fontq,bg="red",fg="white",activebackground="blue",width="10",)

    ba.pack(side="left")
    ba1.pack(side="right")


#to fetch patient_details

def updetails():
    window=tk.Tk()
    window.title("HOSPITAL MANAGEMEANT SYSTEM")
    window.iconbitmap("favicon.ico")
    window.config(bg="violet")
    myfont=Font(family='times',size=20,weight="bold", slant="italic")
    fontq=Font(family='times',size=15,weight="bold")
    la=tk.Label(window,text="Hospital Managmeant",font=myfont,width="80",bg="#0a3d62",fg="white",padx=40,pady=20,relief="raised")
    la.pack()
    ldd8=tk.Label(window,text="Enter  patient no:",font=myfont,fg="black")
    techdd2=tk.Entry(window,width=30,font=("times",20),bg="white",fg="black")
    ldd8.pack(pady="25")
    techdd2.pack()

    ldd9=tk.Label(window,text="Enter patient name :",font=myfont,fg="black")
    techdd1=tk.Entry(window,width=30,font=("times",20),bg="white",fg="black")
    ldd9.pack(pady="25")
    techdd1.pack()

    def upd():
     window=tk.Tk()
     window.title("HOSPITAL MANAGEMEANT SYSTEM")
     window.iconbitmap("favicon.ico")
     window.config(bg="violet")
     myfont=Font(family='times',size=20,weight="bold", slant="italic")
     fontq=Font(family='times',size=15,weight="bold")
     la=tk.Label(window,text="Hospital Managmeant",font=myfont,width="83",bg="#0a3d62",fg="white",padx=40,pady=20,relief="raised")
    
     #la.pack()   
     #la1=tk.Button(window,text="Doctor Details",font=myfont)
     fontq=Font(family='times',size=15,weight="bold")
     dsal1=techdd2.get()
     dname1=techdd1.get()
     con= mys.connect(host='localhost',user='root',passwd='rk2004',database="tk")
     cur=con.cursor()
           
     Query="select * from Patient_details where pno='{}' or pname='{}';".format(dsal1,dname1)
     cur.execute(Query)
    
     result=cur.fetchall()
     la.grid(row=0,column=0,columnspan=len(result[0]))
     for i,row in enumerate(result):
       for j,value in enumerate(row):
          lable=tk.Label(window,text=value,padx="50",font=myfont)
          lable.grid(row=i+1,column=j)
     con.commit()
     #messagebox.showinfo("updated","successfully updated")
    
    
     window.minsize(600,600)
     window.mainloop()
     messagebox.showinfo("SHOW INFO","successfully FETCHED")
     #sumbit()
    ba=tk.Button(window,text="Proceed->",font=fontq,bg="green",fg="white",activebackground="blue",width="10",command=upd)

    

    ba1=tk.Button(window,text="Cancel ×",font=fontq,bg="red",fg="white",activebackground="blue",width="10",)

    ba.pack(side="left")
    ba1.pack(side="right")

#to show doctor details
def sddetails():
    window=tk.Tk()
    window.title("HOSPITAL MANAGEMEANT SYSTEM")
    window.iconbitmap("favicon.ico")
    window.config(bg="violet")
    myfont=Font(family='times',size=20,weight="bold", slant="italic")
    fontq=Font(family='times',size=15,weight="bold")
    la=tk.Label(window,text="Hospital Managmeant",font=myfont,width="83",bg="#0a3d62",fg="white",padx=40,pady=20,relief="raised")
    
    #la.pack()   
    #la1=tk.Button(window,text="Doctor Details",font=myfont)
    fontq=Font(family='times',size=15,weight="bold")
    con= mys.connect(host='localhost',user='root',passwd='rk2004',database="tk")
    cur=con.cursor()
           
    Query="select * from Doctor_details"
    cur.execute(Query)
    result=cur.fetchall()
    la.grid(row=0,column=0,columnspan=len(result[0]))
    for i,row in enumerate(result):
       for j,value in enumerate(row):
          lable=tk.Label(window,text=value,padx="50",font=myfont)
          lable.grid(row=i+1,column=j)
    con.commit()
    #messagebox.showinfo("updated","successfully updated")
    
    
    window.minsize(600,600)
    window.mainloop()
#to show patient details
def spdetails():
    window=tk.Tk()
    window.title("HOSPITAL MANAGEMEANT SYSTEM")
    window.iconbitmap("favicon.ico")
    window.config(bg="violet")
    myfont=Font(family='times',size=20,weight="bold", slant="italic")
    fontq=Font(family='times',size=15,weight="bold")
    la=tk.Label(window,text="Hospital Managmeant",font=myfont,width="83",bg="#0a3d62",fg="white",padx=40,pady=20,relief="raised")
    
    #la.pack()   
    #la1=tk.Button(window,text="Doctor Details",font=myfont)
    fontq=Font(family='times',size=15,weight="bold")
    con= mys.connect(host='localhost',user='root',passwd='rk2004',database="tk")
    cur=con.cursor()
           
    Query="select * from Patient_details"
    cur.execute(Query)
    result=cur.fetchall()
    la.grid(row=0,column=0,columnspan=len(result[0]))
    for i,row in enumerate(result):
       for j,value in enumerate(row):
          lable=tk.Label(window,text=value,padx="50",font=myfont)
          lable.grid(row=i+1,column=j)
    con.commit()
    #messagebox.showinfo("updated","successfully updated")
    
    
    window.minsize(600,600)
    window.mainloop()

#function perform after login page


def sumbit():
  tech="MIOT"
  #tech=tech1.get()
  if(tech=="MIOT"):
    
    from tkinter.font import Font
    window=tk.Tk()
    window.title("HOSPITAL MANAGEMEANT SYSTEM")
    window.iconbitmap("favicon.ico")
    window.config(bg="violet")
    myfont=Font(family='times',size=20,weight="bold", slant="italic")
    la=tk.Label(window,text="Hospital Managmeant",font=myfont,bg="#0a3d62",fg="white",padx=40,pady=20,relief="raised")
       
    #la1=tk.Button(window,text="Doctor Details",font=myfont)
    fontq=Font(family='times',size=15,weight="bold")
    ba1=tk.Button(window,text="Doctor Details",font=fontq,bg="white",fg="Black",activebackground="blue",width="30",command=Doctor)
    ba1.pack(pady="50")


    ba2=tk.Button(window,text="Patient Details",font=fontq,bg="white",fg="Black",activebackground="blue",width="30",command=Patient)
    ba2.pack(pady="50")
    

    ba3=tk.Button(window,text="Ambulance Details",font=fontq,bg="white",fg="Black",activebackground="blue",width="30")
    ba3.pack(pady="50")

    '''ba4=tk.Button(window,text="Doctor Details",font=fontq,bg="white",fg="Black",activebackground="blue",width="30")
    ba4.pack(pady="100")'''

    
    la.pack()
    
    window.minsize(600,600)
    window.mainloop()
  else:
      messagebox.showinfo("invalid","Wrong password/UserName")


#ddetails


def ddetails():
    from tkinter.font import Font
    window=tk.Tk()
    window.title("HOSPITAL MANAGEMEANT SYSTEM")
    window.iconbitmap("favicon.ico")
    window.config(bg="violet")
    myfont=Font(family='times',size=15,weight="bold", slant="italic")
    la=tk.Label(window,text="Hospital Managmeant",width="80",font=myfont,bg="#0a3d62",fg="white",padx=40,pady=20,relief="raised")
    la.pack()   
    #la1=tk.Button(window,text="Doctor Details",font=myfont)
    fontq=Font(family='times',size=15,weight="bold")
    #ldd1=tk.Label(window,text="********************************************************* ",font=myfont,bg="#0a3d62",fg="white",padx=40,pady=20,relief="raised")
    ldd2=tk.Label(window,text="WELCOME TO MIOT DOCTOR DETAILS ENTRY ",font=myfont,bg="#0a3d62",fg="white",padx=40,pady=20,relief="raised")
    #ldd3=tk.Label(window,text="********************************************************* ",font=myfont,bg="#0a3d62",fg="white",padx=40,pady=20,relief="raised")
    
    #ldd1.pack()
    
    ldd2.pack()
    
    #ldd3.pack()
    ldd7=tk.Label(window,text="Enter entry no of Doctor:",font=myfont,fg="black")
    techdd1=tk.Entry(window,width=30,font=("times",20),bg="white",fg="black")
    ldd7.pack()
    techdd1.pack()

    
    ldd8=tk.Label(window,text="Enter  doctor name:",font=myfont,fg="black")
    techdd2=tk.Entry(window,width=30,font=("times",20),bg="white",fg="black")
    ldd8.pack()
    techdd2.pack()
    
    ldd9=tk.Label(window,text="Enter  doctor age:",font=myfont,fg="black")
    techdd3=tk.Entry(window,width=30,font=("times",20),bg="white",fg="black")
    ldd9.pack()
    techdd3.pack()

    ldd10=tk.Label(window,text="Enter doctor specialist:",font=myfont,fg="black")
    techdd4=tk.Entry(window,width=30,font=("times",20),bg="white",fg="black")
    ldd10.pack()
    techdd4.pack()
    
    ldd11=tk.Label(window,text="Enter  doctor joining year:",font=myfont,fg="black")
    techdd5=tk.Entry(window,width=30,font=("times",20),bg="white",fg="black")
    ldd11.pack()
    techdd5.pack()

    
    ldd12=tk.Label(window,text="Enter patient phone no:",font=myfont,fg="black")
    techdd6=tk.Entry(window,width=30,font=("times",20),bg="white",fg="black")
    ldd12.pack()
    techdd6.pack()

    


    ldd13=tk.Label(window,text="Enter patient room no:",font=myfont,fg="black")
    techdd7=tk.Entry(window,width=30,font=("times",20),bg="white",fg="black")
    ldd13.pack()
    techdd7.pack()
    
   
    '''pno=techdd1.get()
     pname=techdd2.get()
     page=techdd3.get()
     pproblem=techdd4.get()
     prd=techdd5.get()
     pph=techdd6.get()
     prn=techdd7.get()  '''

    '''con= mys.connect(host='localhost',user='root',passwd='rk2004',database="tk")
    cur=con.cursor()

    Query="insert into patient_details values('{}','{}','{}','{}','{}','{}','{}')".format(pno,pname,page,pproblem,prd,pph,prn)
    cur.execute(Query)
    con.commit() '''
    def udpd():
         dno=techdd1.get()
         dname=techdd2.get()
         dage=techdd3.get()
         dspec=techdd4.get()
         dsal=techdd5.get()
         dph=techdd6.get()
         dyear=techdd7.get() 
         con= mys.connect(host='localhost',user='root',passwd='rk2004',database="tk")
         cur=con.cursor()
           
         Query="insert into doctor_details values('{}','{}','{}','{}','{}','{}','{}')".format(dno,dname,dage,dspec,dsal,dph,dyear)
         cur.execute(Query)
         con.commit()
         messagebox.showinfo("updated","successfully updated")
         sumbit()
    ba=tk.Button(window,text="Proceed->",font=fontq,bg="green",fg="white",activebackground="blue",width="10",command=udpd)

    

    ba1=tk.Button(window,text="Cancel ×",font=fontq,bg="red",fg="white",activebackground="blue",width="10",)

    ba.pack(side="left")
    ba1.pack(side="right")
    
    
#patient details



def pdetails():
    from tkinter.font import Font
    window=tk.Tk()
    window.title("HOSPITAL MANAGEMEANT SYSTEM")
    window.iconbitmap("favicon.ico")
    window.config(bg="violet")
    myfont=Font(family='times',size=15,weight="bold", slant="italic")
    la=tk.Label(window,text="Hospital Managmeant",font=myfont,bg="#0a3d62",fg="white",padx=40,pady=20,relief="raised")
    la.pack()   
    #la1=tk.Button(window,text="Doctor Details",font=myfont)
    fontq=Font(family='times',size=15,weight="bold")
    #ldd1=tk.Label(window,text="********************************************************* ",font=myfont,bg="#0a3d62",fg="white",padx=40,pady=20,relief="raised")
    ldd2=tk.Label(window,text="WELCOME TO MIOT PATIENT DETAILS ENTRY ",font=myfont,bg="#0a3d62",fg="white",padx=40,pady=20,relief="raised")
    #ldd3=tk.Label(window,text="********************************************************* ",font=myfont,bg="#0a3d62",fg="white",padx=40,pady=20,relief="raised")
    
    #ldd1.pack()
    
    ldd2.pack()
    
    #ldd3.pack()
    ldd7=tk.Label(window,text="Enter entry no of patient:",font=myfont,fg="black")
    techdd1=tk.Entry(window,width=30,font=("times",20),bg="white",fg="black")
    ldd7.pack()
    techdd1.pack()

    
    ldd8=tk.Label(window,text="Enter  patient name:",font=myfont,fg="black")
    techdd2=tk.Entry(window,width=30,font=("times",20),bg="white",fg="black")
    ldd8.pack()
    techdd2.pack()
    
    ldd9=tk.Label(window,text="Enter  patient age:",font=myfont,fg="black")
    techdd3=tk.Entry(window,width=30,font=("times",20),bg="white",fg="black")
    ldd9.pack()
    techdd3.pack()

    ldd10=tk.Label(window,text="Enter patient problem:",font=myfont,fg="black")
    techdd4=tk.Entry(window,width=30,font=("times",20),bg="white",fg="black")
    ldd10.pack()
    techdd4.pack()
    
    ldd11=tk.Label(window,text="Enter  patient recommended doctor:",font=myfont,fg="black")
    techdd5=tk.Entry(window,width=30,font=("times",20),bg="white",fg="black")
    ldd11.pack()
    techdd5.pack()

    
    ldd12=tk.Label(window,text="Enter patient phone no:",font=myfont,fg="black")
    techdd6=tk.Entry(window,width=30,font=("times",20),bg="white",fg="black")
    ldd12.pack()
    techdd6.pack()

    


    ldd13=tk.Label(window,text="Enter patient room no:",font=myfont,fg="black")
    techdd7=tk.Entry(window,width=30,font=("times",20),bg="white",fg="black")
    ldd13.pack()
    techdd7.pack()
    
   
    '''pno=techdd1.get()
     pname=techdd2.get()
     page=techdd3.get()
     pproblem=techdd4.get()
     prd=techdd5.get()
     pph=techdd6.get()
     prn=techdd7.get()  '''

    '''con= mys.connect(host='localhost',user='root',passwd='rk2004',database="tk")
    cur=con.cursor()

    Query="insert into patient_details values('{}','{}','{}','{}','{}','{}','{}')".format(pno,pname,page,pproblem,prd,pph,prn)
    cur.execute(Query)
    con.commit() '''
    def udpd():
         dno=techdd1.get()
         dname=techdd2.get()
         dage=techdd3.get()
         dspec=techdd4.get()
         dsal=techdd5.get()
         dph=techdd6.get()
         dyear=techdd7.get() 
         con= mys.connect(host='localhost',user='root',passwd='rk2004',database="tk")
         cur=con.cursor()
           
         Query="insert into patient_details values('{}','{}','{}','{}','{}','{}','{}')".format(dno,dname,dage,dspec,dsal,dph,dyear)
         cur.execute(Query)
         con.commit()
         messagebox.showinfo("updated","successfully updated")
         sumbit()
    ba=tk.Button(window,text="Proceed->",font=fontq,bg="green",fg="white",activebackground="blue",width="10",command=udpd)

    

    ba1=tk.Button(window,text="Cancel ×",font=fontq,bg="red",fg="white",activebackground="blue",width="10",)

    ba.pack(side="left")
    ba1.pack(side="right")
    
#ambulanence




def adetails():
    from tkinter.font import Font
    window=tk.Tk()
    window.title("HOSPITAL MANAGEMEANT SYSTEM")
    window.iconbitmap("favicon.ico")
    window.config(bg="violet")
    myfont=Font(family='times',size=15,weight="bold", slant="italic")
    la=tk.Label(window,text="Hospital Managmeant",font=myfont,bg="#0a3d62",fg="white",padx=40,pady=20,relief="raised")
    la.pack()   
    #la1=tk.Button(window,text="Doctor Details",font=myfont)
    fontq=Font(family='times',size=15,weight="bold")
    #ldd1=tk.Label(window,text="********************************************************* ",font=myfont,bg="#0a3d62",fg="white",padx=40,pady=20,relief="raised")
    ldd2=tk.Label(window,text="MIOT AMBULANCE DRIVER  ENTRY ",font=myfont,bg="#0a3d62",fg="white",padx=40,pady=20,relief="raised")
    #ldd3=tk.Label(window,text="********************************************************* ",font=myfont,bg="#0a3d62",fg="white",padx=40,pady=20,relief="raised")
    
    #ldd1.pack()
    
    ldd2.pack()
    
    #ldd3.pack()
    ldd7=tk.Label(window,text="Enter entry no of driver:",font=myfont,fg="black")
    techdd1=tk.Entry(window,width=30,font=("times",20),bg="white",fg="black")
    ldd7.pack()
    techdd1.pack()

    
    ldd8=tk.Label(window,text="Enter  driver name:",font=myfont,fg="black")
    techdd2=tk.Entry(window,width=30,font=("times",20),bg="white",fg="black")
    ldd8.pack()
    techdd2.pack()
    
    ldd9=tk.Label(window,text="Enter  driver age:",font=myfont,fg="black")
    techdd3=tk.Entry(window,width=30,font=("times",20),bg="white",fg="black")
    ldd9.pack()
    techdd3.pack()

    ldd10=tk.Label(window,text="Enter driver licence no:",font=myfont,fg="black")
    techdd4=tk.Entry(window,width=30,font=("times",20),bg="white",fg="black")
    ldd10.pack()
    techdd4.pack()
    
    ldd11=tk.Label(window,text="Enter  driver salary:",font=myfont,fg="black")
    techdd5=tk.Entry(window,width=30,font=("times",20),bg="white",fg="black")
    ldd11.pack()
    techdd5.pack()

    
    ldd12=tk.Label(window,text="Enter driver phone no:",font=myfont,fg="black")
    techdd6=tk.Entry(window,width=30,font=("times",20),bg="white",fg="black")
    ldd12.pack()
    techdd6.pack()

    


    ldd13=tk.Label(window,text="Enter driver year of joined:",font=myfont,fg="black")
    techdd7=tk.Entry(window,width=30,font=("times",20),bg="white",fg="black")
    ldd13.pack()
    techdd7.pack()
    
   
    def udpd():
         ano=techdd1.get()
         aname=techdd2.get()
         aage=techdd3.get()
         alice=techdd4.get()
         asal=techdd5.get()
         aph=techdd6.get()
         ayear=techdd7.get() 
         con= mys.connect(host='localhost',user='root',passwd='rk2004',database="tk")
         cur=con.cursor()
           
         Query="insert into ambulance_driver_details values('{}','{}','{}','{}','{}','{}','{}')".format(ano,aname,aage,alice,asal,aph,ayear)
         cur.execute(Query)
         con.commit()
         messagebox.showinfo("updated","successfully updated")
         sumbit()
    ba=tk.Button(window,text="Proceed->",font=fontq,bg="green",fg="white",activebackground="blue",width="10",command=udpd)

    

    ba1=tk.Button(window,text="Cancel ×",font=fontq,bg="red",fg="white",activebackground="blue",width="10",)

    ba.pack(side="left",padx="250")
    ba1.pack(side="right",padx="250",anchor=tk.E)
    '''anchor right to left pading'''
    



def login():
   window=tk.Tk()
   #window.maxsize(800,800)
   window.title("HOSPITAL MANAGEMEANT SYSTEM")
   window.iconbitmap("favicon.ico")
   window.config(bg="violet")
   myfont=Font(family='times',size=20,weight="bold",slant="italic")
   la=tk.Label(window,text="Welcome Hospital Managmeant",font=myfont,bg="#0a3d62",fg="white",padx=40,pady=20,relief="raised")
   fontq=Font(family='times',size=15,weight="bold")
   l11=tk.Label(window,text="Login",font=myfont,fg="black")
   l12=tk.Label(window,text="Username",font=myfont,fg="black")
   tech1=tk.Entry(window,width=30,font=("times",20),bg="white",fg="black")
   l13=tk.Label(window,text="Password",font=myfont,fg="black")
   tech2=tk.Entry(window,width=30,font=("times",20),bg="white",fg="black",show="*")
   ba=tk.Button(window,text="Proceed->",font=fontq,bg="green",fg="white",activebackground="blue",width="10",command=sumbit)

    

   ba1=tk.Button(window,text="Cancel ×",font=fontq,bg="red",fg="white",activebackground="blue",width="10",)

   #ba.place(x=1300,y=500)
   la.pack()


   l11.pack(pady=50)
   l12.pack(pady=3)
   tech1.pack(pady=2)
   l13.pack(pady=5)
   tech2.pack(pady=4)

   ba.pack(side="left",padx=250)#padx=900,pady=350) 
   ba1.pack(side="right",padx=200)
   ba1.pack()

   window.mainloop()
login()



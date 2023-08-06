import mysql.connector as mys
con= mys.connect(host='localhost',user='root',passwd='rk2004',database='PROJECT')
if con.is_connected():

   cur=con.cursor()

   print("*********************HOSPITAL MANAGEMENT SYSTEM****************************")
   print("STAY SAFE STAY ALIVE")
   print("1:LOGIN")
   print("2:EXIST")
   choice=int(input("Enter 1 to login:")) 
   if choice==1:
      user_id=input("Enter your user id:")

      password=input("Enter your password:")

      if user_id=="MIOT" and password=="MIOT62":
       def title():
         print("You are successfully login")
         print("WELCOME MIOT INTERNATIONAL HOSPITAL")
         print("1.Registering Patient details")
         print("2.Registering Doctor details")
         print("3.Registering worker details")
         print("4.Total Patient details")
         print("5.Total doctor details")
         print("6.Total worker details")
         print("7.Searching patient details")
         print("8.Searching doctor details")
         print("9.Searching worker details")
         print("10.Occupied room number")
         print("11.Billing for medicine and room")
         print("12.Avalibility of medicine")
         print("13.Update doctor details")
         print("14.Update worker details")
         print("15.Update patient details")
         print("16.Number of  Patient in the hospital")
         print("17.Number of doctor in the hospital")
         print("18.Available of doctor")
         print("19.Ambulance driver details")
         print("20.Ambulance Availability")
         print("21.Exist")
         choice=int(input("Enter your choice:"))

         if choice==1:
           print("*********************************************************")
           print("WELCOME TO MIOT PATIENT DETAILS ENTRY")
           print("*********************************************************")
           Patient_entryno=int(input("Enter entry no of patient:"))
           Patient_name=input("Enter Patient name:")
           Patient_age=int(input("Enter Patient age:"))
           Patient_problem=input("Enter Patient Problem:")
           Doctor_recommended=input("Enter recommended doctor name:")
           Patient_ph=input("Enter Patient phone number:")
           Patient_roomno=int(input("Enter Patient room no;")) 
           Query="insert into patient_details values({},'{}',{},'{}','{}',{},{})".format(Patient_entryno,Patient_name,Patient_age,Patient_problem,Doctor_recommended,Patient_ph,Patient_roomno)
           cur.execute(Query)
           con.commit()
           print("successfully registered")
           A=input("Do you want to continue(y/n):")


         elif choice==2:
           print("*********************************************************")
           print("WELCOME TO MIOT DOCTOR DETAILS ENTRY")
           print("**********************************************************")
           Doctor_entryno=int(input("Enter entry no of doctor:"))
           Doctor_name=input("Enter Doctor name:")
           Doctor_age=int(input("Enter Doctor age:"))
           Doctor_graduation=input("Enter Doctor graduation:")
           Doctor_department=input("Enter Doctor department:") 
           Doctor_Salary=input("Enter Doctor Salary:")
           Doctor_ph=input("Enter Doctor phone number:")
           Doctor_available=input("Enter Doctor is available/not available(y/n):")
           Doctor_roomno=int(input("Enter Doctor room no:"))
           Query1="insert into Doctor_details values({},'{}',{},'{}','{}','{}',{},'{}',{})".format(Doctor_entryno,Doctor_name,Doctor_age,Doctor_graduation,Doctor_department,Doctor_Salary,Doctor_ph,Doctor_available,Doctor_roomno)
           cur.execute(Query1)
           con.commit()
           print("successfully registered")
           A=input("Do you want to continue(y/n):")
           elif choice==3:
           print("*********************************************************")
           print("WELCOME TO MIOT WORKER DETAILS ENTRY")
           print("**********************************************************")
           Worker_entryno=int(input("Enter entry no of worker:"))
           Worker_name=input("Enter worker name:")
           Worker_age=int(input("Enter worker age:"))  
           Worker_graduation=input("Enter worker graduation:")
           Worker_Salary=input("Enter worker Salary:")
           Worker_WorkName=input("Enter workname:")
           Worker_Roomno=int(input("Enter worker room no:"))
           Worker_ph=int(input("Enter worker phone number:"))
           Query2="insert into worker_details values({},'{}',{},'{}','{}','{}',{},{})".format(Worker_entryno,Worker_name,Worker_age,Worker_graduation,Worker_WorkName,Worker_Salary,Worker_Roomno,Worker_ph)
           cur.execute(Query2)
           con.commit()
           print("successfully registered")

           
         elif choice==4:
            print("**************************************************")
            print("*********TOTAL PATIENT DETAILS**********")
            print("**************************************************")
            Query3="select * from patient_details"
            cur.execute(Query3)
            a=cur.fetchall()
            for i in a:
               print(a)

               
         elif choice==5:
              print("**************************************************")
              print("*********TOTAL DOCTOR DETAILS**********")
              print("**************************************************")
              Query4="select * from doctor_details"
              cur.execute(Query4)
              b=cur.fetchall()
              for i in b:
                   print(b)

                   
         elif choice==6:
              print("*****************************************************") 
         print("*********TOTAL WORKERS DETAILS**********")
              print("*****************************************************")
              Query6="select * from Worker_details"
              cur.execute(Query6)
              c=cur.fetchall()
              for i in c:
                   print(c)

                   
         elif choice==7:
               print("****************************************************")
               print("WELCOME TO SEARCH PATIENT DETAILS")
               print("****************************************************")
               entryno=int(input("Enter patient entry number:"))
               Query7="select * from patient_details where patient_entryno={}".format(entryno)
               cur.execute(Query7)
               data=cur.fetchone()
               if data!=None:
                  print(data)
               else:
                  print("Record is not found!!!")

                  
         elif choice==8:
               print("****************************************************")
               print("WELCOME TO SEARCH DOCTOR DETAILS")
               print("****************************************************")
               entryno1=int(input("Enter doctor entry number:"))
               Query8="select * from doctor_details where doctor_entryno={}".format(entryno1)
               cur.execute(Query8)
               data=cur.fetchone()
               if data!=None:
                  print(data)
               else:
                  print("Record is not found!!!")

                  
         elif choice==9:
               print("****************************************************")
               print("WELCOME TO SEARCH WORKERS DETAILS")
               print("****************************************************")
               entryno2=int(input("Enter worker entry number:"))
               Query9="select * from worker_details where worker_entryno={}".format(entryno2)
               cur.execute(Query9)
               data=cur.fetchone()
                         if data!=None:
                  print(data)
               else:
                  print("Record is not found!!!")

                  
         elif choice==10:
               print("**********************************")
               print("OCCUPIED ROOM NUMBER")
               print("**********************************")
               Query10="select patient_roomno 'OCCUPIED ROOM NUMBER'  from patient_details"
               cur.execute(Query10)
               data=cur.fetchall()
               if data!=None:
                   print(data)
               else:
                    print("Record is not found")

                    
         elif choice==11:
               print("******************************************************")
               print("*****MIOT INTERNATIONAL HOSPITAL*********")
               print("*******************************************************")
               Dates_of_activity=input("Enter the date when product is buyed:")
               Item_description=input("Enter product name:")
               Qty=int(input("Enter number of product buyed:"))
               Charges=int(input("Enter Charge of the product:"))
               query="insert into billing values('{}','{}',{},{})".format(Dates_of_activity,Item_description,Qty,Charges)
               cur.execute(query)
               con.commit()
               print("successfully registered")

               
         elif choice==12:
               print("*******************************************************")
               print("**********AVAILABLE OF MEDICINE**************")
               print("********************************************************")
               Name=input("Enter the name of medicine:")
               query1="select * from billing where Item_description='{}'".format(Name)
               cur.execute(query1)
               m=cur.fetchone()
               if m!=None:
                  print(m)
                         else:
                  print("Record not found!!!")

                  
         elif choice==13:
                 print("****************************************************")
                 print("********UPDATE DOCTOR DETAILS***********")
                 print("****************************************************")
                 salary=int(input("Enter Doctor salary do you want to update:"))
                 entryno=int(input("Enter doctor_entryno:"))
                 query="update Doctor_details set Doctor_salary={} where Doctor_entryno={}".format(salary,entryno)
                 cur.execute(query)
                 con.commit()

         elif choice==14:
                 print("****************************************************")
                 print("********UPDATE WORKER DETAILS***********")
                 print("****************************************************")
                 salary=int(input("Enter Worker salary do you want to update:"))
                 entryno=int(input("Enter Worker_entryno:"))
                 query="update Worker_details set Worker_salary={} where Worker_entryno={}".format(salary,entryno)
                 cur.execute(query)
                 con.commit()

         elif choice==15:
                 print("****************************************************")
                 print("********UPDATE PATIENT DETAILS***********")
                 print("****************************************************")
                 no=int(input("Enter Patient room no do you want to update:"))
                 entryno=int(input("Enter Patient_entryno:"))
                 query="update Patient_details set  Patient_roomno={} where Patient_entryno={}".format(no,entryno)
                 cur.execute(query)
                 con.commit()

         elif choice==16:
                 print("**************************************************")
                 print("***Number of  Patient in the hospital*********")
                 print("**************************************************")
                 query="select count(Patient_name) 'number of patient in the hospital' from patient_details"
                 cur.execute(query)
                 data=cur.fetchall()
                          for i in data:
                    print(i)

         elif choice==17:
                 print("**************************************************")
                 print("***Number of Doctor in the hospital*********")
                 print("**************************************************")
                 query="select count(doctor_name) 'number of doctor in the hospital' from doctor_details"
                 cur.execute(query)
                 data=cur.fetchall()
                 for i in data:
                    print(i)

         elif choice==18:
                 print("**************************************************")
                 print("***Available of Doctor in the hospital*********")
                 print("**************************************************")
                 query="select *  from doctor_details where doctor_available='Y' "
                 cur.execute(query)
                 data=cur.fetchall()
                 for i in data:
                    print(i)

         elif choice==19:
           print("*********************************************************")
           print("WELCOME TO MIOT DRIVER DETAILS ENTRY")
           print("**********************************************************")
           Driver_entryno=int(input("Enter entry no of Driver:"))
           Driver_name=input("Enter Driver name:")
           Driver_age=int(input("Enter Driver age:"))  
           Driver_graduation=input("Enter Driver graduation:")
           Driver_Salary=input("Enter Driver Salary:")
           Driver_Licensesno=input("Enter Driver_Licensesno:")
           Driver_ph=int(input("Enter worker phone number:"))
           Driver_Available=input("Enter Driver Available:")
           Query2="insert into Driver_details values({},'{}',{},'{}',{},{},{},'{}')".format(Driver_entryno,Driver_name,Driver_age,Driver_graduation,Driver_Salary,Driver_Licensesno,Driver_ph,Driver_Available)
           cur.execute(Query2)
           con.commit()
           print("successfully registered")

           
         elif choice==20:
                          print("**************************************************")
                 print("***Available of Ambulance in the hospital*********")
                 print("**************************************************")
                 query="select *  from driver_details where driver_available='Y' "
                 cur.execute(query)
                 data=cur.fetchall()
                 for i in data:
                    print(i)

         elif choice==21:
                 print("*********")
                 print("-EXIST-")
                 print("*********")
               
         else:
            print("Enter correct choice")

title()  
Con.close()






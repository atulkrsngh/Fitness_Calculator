from tkinter import *

# basic function coding

def generate_report():
   def intro():
      print("                                                          *** FITNESS REPORT ***")

   def bmi():
       bmi=float(E3.get())/(float(E4.get())*float(E4.get()))
       print("Bmi(body mass index):",bmi)
   def BP():
      if(float(E6.get())>=140 and float(E5.get())>=90):
         print("BP(high/medium/low):","high")
      elif(140>=float(E6.get())>=90 and 90>=float(E5.get())>=60):
         print("BP(high/medium/low):","medium")
      elif(float(E6.get())<=90 and float(E5.get())<=60):
         print("BP(high/medium/low):","Low")
   def pulserate():
        if(float(E7.get())>=100):
            print("WBC count(high/medium/low):","high")

        elif(100>=float(E7.get())>=60):
                print("WBC count(high/medium/low):","medium")
        elif(float(E7.get())<=60):
                print("WBC count(high/medium/low):","low")
   def RBCcount():
        if(float(E8.get())>=6.1):
            print("RBC count(high/medium/low):","high")
        elif(6.1>=float(E8.get())>=4.7):
                print("RBC count(high/medium/low):","medium")
        elif(float(E8.get())<=4.7):
                print("RBC count(high/medium/low):","low")
   def WBCcount():
        if(float(E9.get())>=10000):
            print("WBC count(high/medium/low):","high")
        elif(10000>=float(E9.get())>=4000):
                print("WBC count(high/medium/low):","medium")
        elif(float(E9.get())<=4000):
                print("WBC count(high/medium/low):","low")
   def platelets():
        if(float(E10.get())>=450):
            print("platelets (high/medium/low):","high")
        elif(450>=float(E10.get())>=150):
                print("platelets (high/medium/low):","medium")
        elif(int(E10.get())<=150):
                print("platelets (high/medium/low):","low")
   def HB():
        if(float(E11.get())>=175):
            print(" HB (high/medium/low):","high")
        elif(175>=float(E11.get())>=135):
                print("HB (high/medium/low):","medium")
        elif(float(E11.get())<=135):
                print("HB (high/medium/low):","low")
   def uric_acid():
        if(float(E12.get())>=7.0):
            print(" uric acid(high/medium/low):","high")
        elif(7.0>=float(E12.get())>=3.4):
                print("uric acid(high/medium/low):","medium")
        elif(float(E12.get())<=3.4):
                print("uric acid(high/medium/low):","low")
   def cholestrol():
        if(float(E13.get())>=240):
            print("cholestrol(high/medium/low):","high")
        elif(240>=float(E13.get())>=200):
                print("cholestrol(high/medium/low):","medium")
        elif(float(E13.get())<=200):
                print("cholestrol(high/medium/low):","low")
   def basic():
        print("name:",E1.get())
        print("age:",E2.get())
   basic()
   intro()
   bmi()
   BP()
   #pulserate()
   RBCcount()
   WBCcount()
   platelets()
   HB()
   uric_acid()
   cholestrol()
def generate_report2():
   def bmi():
      bmi=pow((int(E3.get())*int(E4.get())),2)
      print("Bmi(body mass index):",bmi)
   def BP():
      if(int(E6.get())>=140 and int(E5.get())>=90):
        print("BP(high/medium/low):","high")
      elif(140>=int(E6.get())>=90 and 90>=int(E5.get())>=60):
         print("BP(high/medium/low):","medium")
      elif(int(E6.get())<=90 and int(E5.get())<=60):
         print("BP(high/medium/low):","Low")
   def pulserate():
      if(int(E7.get())>=100):
            print("WBC count(high/medium/low):","high")
      elif(100>=int(E7.get())>=60):
                print("WBC count(high/medium/low):","medium")
      elif(int(E7.get())<=60):
                print("WBC count(high/medium/low):","low")
   def RBCcount():
        if(int(E8.get())>=5.4):
            print("RBC count(high/medium/low):","high")
        elif(5.4>=int(E8.get())>=4.2):
                print("RBC count(high/medium/low):","medium")
        elif(int(E8.get())<=4.2):
                print("RBC count(high/medium/low):","low")
   def WBCcount():
        if(int(E9.get())>=10000):
            print("WBC count(high/medium/low):","high")
        elif(10000>=int(E9.get())>=4000):
                print("WBC count(high/medium/low):","medium")
        elif(int(E9.get())<=4000):
                print("WBC count(high/medium/low):","low")
   def platelets():
        if(int(E10.get())>=450):
            print("platelets (high/medium/low):","high")
        elif(450>=int(E10.get())>=150):
                print("platelets (high/medium/low):","medium")
        elif(int(E10.get())<=150):
                print("platelets (high/medium/low):","low")
   def HB():
        if(int(E11.get())>=155):
           print("HB(high/medium/low):","high")
        elif(155>=int(E11.get())>=120):
                print("HB(high/medium/low):","medium")
        elif(int(E11.get())<=120):
                print("HB(high/medium/low):","low")
   def uric_acid():
        if(int(E12.get())>=6.0):
            print("uric acid(high/medium/low):","high")
        elif(6.0>=int(E12.get())>=2.4):
              print("uric acid(high/medium/low):","medium")
        elif(int(E12.get())<=2.4):
                print("uric acid(high/medium/low):","low")
   def cholestrol():
        if(int(E13.get())>=240):
            print("cholestrol(high/medium/low):","high")
        elif(240>=int(E13.get())>=200):
                print("cholestrol(high/medium/low):","medium")
        elif(int(E13.get())<=200):
                print("cholestrol(high/medium/low):","low")
   def basic():
       print("name:",E1.get()) 
       print("age:",E2.get()) 
   
   basic()
   bmi()
   BP()
   #pulserate()
   RBCcount()
   WBCcount()
   platelets()
   HB()
   uric_acid()
   cholestrol()
def submit():
 if(v.get()==1):
      generate_report()
 elif(v.get()==2):
      generate_report2()

# gui coding for interface                     
master= Tk()
master.title("Fitness calculator")
master.configure(background="orange")
Label(master, text="Name",bg='brown').grid(row=0)
Label(master,text="age(in year)",bg='brown').grid(row=0,column=2)
Label(master,text="weight(in kg)",bg='brown').grid(row=2)
Label(master,text="height(in meters)",bg='brown').grid(row=3)
Label(master,text="BP low(in mm hg)",bg='brown').grid(row=4)
Label(master,text="BP high(in mm hg)",bg='brown').grid(row=5)
Label(master,text="pulse rate(in bpm)",bg='brown').grid(row=6)
Label(master,text="RBC count(in million/l)",bg='brown').grid(row=7)
Label(master,text="WBC count(in mm3)",bg='brown').grid(row=8)
Label(master,text="platelets(in billion/l)",bg='brown').grid(row=9)
Label(master,text="HB(in g/l)",bg='brown').grid(row=10)
Label(master,text="uric acid(in mg/dl)",bg='brown').grid(row=11)
Label(master,text="cholestrol(in mg/dl)",bg='brown').grid(row=12)
frame=Frame(master,width=100,heigh=100,bd=11)
v = IntVar()
Label(master, 
      text="""Gender:""",
      
      justify = LEFT,
      padx = 20,bg='brown').grid(row=1,column=0)
r1=Radiobutton(master, 
            text="Male",
            padx = 20, 
            variable=v, 
            value=1,bg='yellow').grid(row= 1,column=1)
r2=Radiobutton(master, 
            text="Female",
            padx = 20, 
            variable=v, 
            value=2,bg='yellow').grid(row=1,column=2)

E1=Entry(master,bg='yellow')
E2=Entry(master,bg='yellow')
E3=Entry(master,bg='yellow')
E4=Entry(master,bg='yellow')
E5=Entry(master,bg='yellow')
E6=Entry(master,bg='yellow')
E7=Entry(master,bg='yellow')
E8=Entry(master,bg='yellow')
E9=Entry(master,bg='yellow')
E10=Entry(master,bg='yellow')
E11=Entry(master,bg='yellow')
E12=Entry(master,bg='yellow')
E13=Entry(master,bg='yellow')
E1.grid(row=0 ,column=1)
E2.grid(row=0,column=3)
E3.grid(row=2,column=1)
E4.grid(row=3,column=1)
E5.grid(row=4,column=1)
E6.grid(row=5,column=1)
E7.grid(row=6,column=1)
E8.grid(row=7,column=1)
E9.grid(row=8,column=1)

E10.grid(row=9,column=1)
E11.grid(row=10,column=1)
E12.grid(row=11,column=1)
E13.grid(row=12,column=1)
Button(master, text='generate_report', command=submit,bg='brown').grid(row=12, column=5, sticky=W, pady=6  )
mainloop()

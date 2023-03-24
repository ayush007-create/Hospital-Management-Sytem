from tkinter import *
from tkinter import ttk
import random
import datetime
import time
from tkinter import messagebox


class hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1640x900+0+0")
        lbtitle=Label(self.root,bd=10,relief="groove",text="HOSPITAL MANAGEMENT SYSTEM",fg='red',bg='white',font=("Montserrat",50,"bold"))
        lbtitle.pack(fill=X)
        self.nameoftablets=StringVar()
        self.ref=StringVar()
        self.dose=StringVar()
        self.noftablets=StringVar()
        self.lot=StringVar()
        self.issuedate=StringVar()
        self.expirydate=StringVar()
        self.sideeffect=StringVar()
        self.dailydose=StringVar()
        self.furtherinfo=StringVar()
        self.bloodpressure=StringVar()
        self.storageadvice=StringVar()
        self.medication=StringVar()
        self.patientname=StringVar()
        self.dateofbirth=StringVar()
        self.patientaddress=StringVar()
        #-------------------DataFrame-----------------
        dataframe=Frame(self.root,bd='3',relief='solid')
        dataframe.place(x=1,y=100,width=1630,height=400)

        dataframeleft=LabelFrame(dataframe,bd='2',relief='solid',padx=10,text="Patient Information",font=("Open Sans",10,"bold"))
        dataframeleft.place(x=3,y=5,width=980,height=380)
        dataframeright = LabelFrame(dataframe, bd='15', fg="blue",relief='ridge', padx=10, text="Prescription",
                                   font=("Montserrat", 15, "bold"))
        dataframeright.place(x=1010,y=5,width=600,height=380)

        #---------------------buttonframe--------------
        buttonframe = Frame(self.root, bd='3', relief='solid')
        buttonframe.place(x=1, y=510, width=1630, height=70)

        #---------------------detailsframe---------------
        detailsframe = Frame(self.root, bd='3', relief='solid')
        detailsframe.place(x=1, y=600, width=1630, height=290)
        #-------------------detailsdataframeleft----------
        tablet=Label(dataframeleft,text="Name of Tablets :",font=("Times New Roman",12,"bold"),padx=10,pady=10)
        tablet.grid(row=0,column=0,sticky=W)

        tabletbox=ttk.Combobox(dataframeleft,textvariable=self.nameoftablets,font=('arial',12,"bold"),width=30)
        tabletbox['values']=("Paracitemol","Nice","Sartel-AM","Pandy","Zerdol")
        tabletbox.grid(row=0,column=1)

        refernce = Label(dataframeleft, text="Reference No. :", font=("Times New Roman", 12, "bold"), padx=10, pady=10)
        refernce.grid(row=1,column=0,sticky=W)
        refentry=Entry(dataframeleft,textvariable=self.ref,font=('arial',12,'bold'),width=30)
        refentry.grid(row=1,column=1)

        dose = Label(dataframeleft, text="Dose :", font=("Times New Roman", 12, "bold"), padx=10, pady=10)
        dose.grid(row=2, column=0,sticky=W)

        doseentry=Entry(dataframeleft,textvariable=self.dose,font=('arial',12,'bold'),width=30)
        doseentry.grid(row=2,column=1)

        noftablets = Label(dataframeleft,text="Number Of Tablets :", font=("Times New Roman", 12, "bold"), padx=10, pady=10)
        noftablets.grid(row=3, column=0, sticky=W)

        noftabletsentry=Entry(dataframeleft,textvariable=self.noftablets,font=('arial',12,'bold'),width=30)
        noftabletsentry.grid(row=3,column=1)

        lot = Label(dataframeleft, text="Lot :", font=("Times New Roman", 12, "bold"), padx=10,pady=10)
        lot.grid(row=4, column=0, sticky=W)

        lotentry=Entry(dataframeleft,textvariable=self.lot,font=('arial',12,'bold'),width=30)
        lotentry.grid(row=4,column=1)

        issuedate = Label(dataframeleft, text="Issue Date :", font=("Times New Roman", 12, "bold"), padx=10,pady=10)
        issuedate.grid(row=5, column=0, sticky=W)

        issuedateentry=Entry(dataframeleft,textvariable=self.issuedate,font=('arial',12,'bold'),width=30)
        issuedateentry.grid(row=5,column=1)

        expirydate = Label(dataframeleft, text="Expiry Date :", font=("Times New Roman", 12, "bold"), padx=10,pady=10)
        expirydate.grid(row=6, column=0, sticky=W)

        expirydateentry=Entry(dataframeleft,textvariable=self.expirydate,font=('arial',12,'bold'),width=30)
        expirydateentry.grid(row=6,column=1)

        dailydose = Label(dataframeleft, text="Daily Dose :", font=("Times New Roman", 12, "bold"), padx=10,pady=10)
        dailydose.grid(row=7, column=0, sticky=W)

        dailydoseentry=Entry(dataframeleft,textvariable=self.dailydose,font=('arial',12,'bold'),width=30)
        dailydoseentry.grid(row=7,column=1)

        sideeffect = Label(dataframeleft, text="Side Effects :", font=("Times New Roman", 12, "bold"), padx=40)
        sideeffect.grid(row=0, column=2,sticky=W)

        sideeffectentry=Entry(dataframeleft,textvariable=self.sideeffect,font=('arial',12,'bold'),width=30)
        sideeffectentry.grid(row=0,column=3)

        furtherinfo = Label(dataframeleft,text="Further Information :", font=("Times New Roman", 12, "bold"), padx=40)
        furtherinfo.grid(row=1, column=2,sticky=W)

        furtherinfoentry=Entry(dataframeleft,textvariable=self.furtherinfo,font=('arial',12,'bold'),width=30)
        furtherinfoentry.grid(row=1,column=3)

        bloodpressure = Label(dataframeleft,text="Blood Pressure :", font=("Times New Roman", 12, "bold"), padx=40)
        bloodpressure.grid(row=2, column=2,sticky=W)

        bloodpressureentry=Entry(dataframeleft,textvariable=self.bloodpressure,font=('arial',12,'bold'),width=30)
        bloodpressureentry.grid(row=2,column=3)

        storageadvice = Label(dataframeleft,text="Storage Advice :", font=("Times New Roman", 12, "bold"), padx=40)
        storageadvice.grid(row=3, column=2,sticky=W)

        storageadviceentry=Entry(dataframeleft,textvariable=self.storageadvice,font=('arial',12,'bold'),width=30)
        storageadviceentry.grid(row=3,column=3)

        Medication = Label(dataframeleft,text="Medication :", font=("Times New Roman", 12, "bold"), padx=40)
        Medication.grid(row=4, column=2,sticky=W)

        Medicationentry=Entry(dataframeleft,textvariable=self.medication,font=('arial',12,'bold'),width=30)
        Medicationentry.grid(row=4,column=3)

        patientname = Label(dataframeleft,text="Patient Name :", font=("Times New Roman", 12, "bold"), padx=40)
        patientname.grid(row=5, column=2,sticky=W)

        patientnameentry=Entry(dataframeleft,textvariable=self.patientname,font=('arial',12,'bold'),width=30)
        patientnameentry.grid(row=5,column=3)

        dateofbirth = Label(dataframeleft,text="Date Of Birth :", font=("Times New Roman", 12, "bold"), padx=40)
        dateofbirth.grid(row=6, column=2,sticky=W)

        dateofbirthentry=Entry(dataframeleft,textvariable=self.dateofbirth,font=('arial',12,'bold'),width=30)
        dateofbirthentry.grid(row=6,column=3)

        patientaddress = Label(dataframeleft,text="Patient Address :", font=("Times New Roman", 12, "bold"), padx=40)
        patientaddress.grid(row=7, column=2,sticky=W)

        patientaddressentry=Entry(dataframeleft,textvariable=self.patientaddress,font=('arial',12,'bold'),width=30)
        patientaddressentry.grid(row=7,column=3)

        #-----------------------------------Dataframeright-------------------
        textfield=Text(dataframeright,font=("Montserrat", 12, "bold"),width=60,height=16,padx=2,pady=6)
        textfield.grid(row=0,column=0)

        #------------------------------buttons-------------------------------
        prescriptionbutton=Button(buttonframe,text="Prescription",fg="white",font=("Arial",12,"bold"),bg="green",width=22,height=2,padx=2,pady=6)
        prescriptionbutton.grid(row=0,column=0)

        databutton = Button(buttonframe,text="Prescription Data", fg="white", font=("Arial", 12, "bold"),bg="green", width=22, height=2, padx=25, pady=6)
        databutton.grid(row=0, column=1)

        updatebutton = Button(buttonframe, text="Update", fg="white", font=("Arial", 12, "bold"),bg="green", width=22, height=2, padx=25, pady=6)
        updatebutton.grid(row=0, column=2)

        deletebutton = Button(buttonframe, text="Delete", fg="white", font=("Arial", 12, "bold"),bg="green", width=22, height=2, padx=25, pady=6)
        deletebutton.grid(row=0, column=3)

        clearbutton = Button(buttonframe, text="Clear", fg="white", font=("Arial", 12, "bold"),bg="green", width=22,height=2, padx=25, pady=6)
        clearbutton.grid(row=0, column=4)

        exitbutton = Button(buttonframe, text="Exit", fg="white", font=("Arial", 12, "bold"),bg="green", width=22, height=2, padx=25, pady=6)
        exitbutton.grid(row=0, column=5)

        #-----------------------------------table--------------------------
        #----------------------------------scrollbar-----------------------
        scroll_x=ttk.Scrollbar(detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(detailsframe,orient=VERTICAL)
        self.hospitaltable=ttk.Treeview(detailsframe,columns=("nameoftablets","referenceno","dose","numberoftablets","lot",
        "issuedate","expirydate","dailydose","sideeffects","furtherinformation","bloodpressure","storageadvice","medications",
        "patientname","dateofbirth","patientaddress"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x=ttk.Scrollbar(command=self.hospitaltable.xview)
        scroll_y=ttk.Scrollbar(command=self.hospitaltable.yview)

        self.hospitaltable.heading("nameoftablets",text="Name Of Tablets")
        self.hospitaltable.heading("referenceno", text="Reference")
        self.hospitaltable.heading("dose", text="Dose")
        self.hospitaltable.heading("numberoftablets", text="Number Of Tablets")
        self.hospitaltable.heading("lot", text="Lot")
        self.hospitaltable.heading("issuedate", text="Issue Date")
        self.hospitaltable.heading("expirydate", text="Expiry Date")
        self.hospitaltable.heading("dailydose", text="Daily Dose")
        self.hospitaltable.heading("sideeffects", text="Side Effects")
        self.hospitaltable.heading("bloodpressure", text="Blood Pressure")
        self.hospitaltable.heading("furtherinformation", text="Further Information")
        self.hospitaltable.heading("storageadvice", text="Storage Advice")
        self.hospitaltable.heading("medications", text="Medications")
        self.hospitaltable.heading("patientname", text="Patient Name")
        self.hospitaltable.heading("dateofbirth", text="Date Of Birth")
        self.hospitaltable.heading("patientaddress", text="Patient Address")

        self.hospitaltable["show"]="headings"
        self.hospitaltable.pack(fill=BOTH,expand=1)
        self.hospitaltable.column("nameoftablets",width=100)
        self.hospitaltable.column("referenceno",width=100)
        self.hospitaltable.column("dose",width=100)
        self.hospitaltable.column("numberoftablets",width=100)
        self.hospitaltable.column("lot",width=100)
        self.hospitaltable.column("issuedate",width=100)
        self.hospitaltable.column("expirydate",width=100)
        self.hospitaltable.column("dailydose",width=100)
        self.hospitaltable.column("sideeffects",width=100)
        self.hospitaltable.column("bloodpressure",width=100)
        self.hospitaltable.column("furtherinformation",width=100)
        self.hospitaltable.column("storageadvice",width=100)
        self.hospitaltable.column("medications",width=100)
        self.hospitaltable.column("patientname",width=100)
        self.hospitaltable.column("dateofbirth",width=100)
        self.hospitaltable.column("patientaddress",width=100)
        self.hospitaltable.pack(fill=BOTH,expand=1)

root=Tk()
hos=hospital(root)
root.mainloop()


from tkinter import*
import customtkinter
import tkinter.messagebox as tmsg
import os
import math,random

customtkinter.set_appearance_mode("System")   # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green") # Themes: blue (default), dark-blue, green

class Billing:
    #theme changer
    def change_mode(self):
        if self.switch_2.get() == 1:
            customtkinter.set_appearance_mode("dark")
        else:
            customtkinter.set_appearance_mode("light")

    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x1200")
        
        self.root.attributes("-fullscreen", True)
        self.root.title("Billing software")
        
        # frame head
        Heading=customtkinter.CTkLabel(self.root, text="Billing software",width=120,height=20,text_font=("elephant",30),fg_color=("white", "black"),corner_radius=0)
        Heading.place(relwidth=1)
        self.root.config(bg="black")
        F_H= customtkinter.CTkFrame(Heading, corner_radius=0)
        F_H.place(x=-2,y=5,width=200, height=45)
        self.switch_2 = customtkinter.CTkSwitch(F_H,
                                                text="Dark Mode/Light mode",
                                                command=self.change_mode)
        self.switch_2.grid(row=0, column=0, pady=10, padx=20)
        # ----------Variable Declaration------------#
        self.CustomerName1 =StringVar()
        self.Contact_No_1 =StringVar()
        self.Bill_No_1 = StringVar()
        x=random.randint(1000,9999)
        self.Bill_No_1.set(x)
        self.Search_bill= StringVar()

        # ----------Variable Declaration F2-----------#
        self.Bath_Soap_1 = IntVar()
        self.Face_Cream_1 =IntVar()
        self.Face_Wash_1 =IntVar()
        self.Hair_Spray_1 =IntVar()
        self.Hair_Gel_1 =IntVar()
        self.Body_Losan_1 =IntVar()
        # ----------Variable Declaration F3------------#
        self.Rice_1 =IntVar()
        self.Wheat_1 =IntVar()
        self.Sugar_1 =IntVar()
        self.Tea_1 =IntVar()
        self.Daal_1 =IntVar()
        self.Food_oil_1 =IntVar()
        # ----------Variable Declaration F4------------#
        self.Maza_1 =IntVar()
        self.Coca_1=IntVar()
        self.Thumbs_up_1 =IntVar()
        self.Fruti_1 =IntVar()
        self.Sprite_1 =IntVar()
        self.Limca_1 =IntVar()
        # ----------Variable Declaration F5------------#
        self.Total_Cosmatic_1=IntVar()
        self.Total_Grocery_1 = IntVar()
        self.Total_colddrink_1 = IntVar()
        self.Cosmatic_Tax_1=IntVar()
        self.Grocery_Tax_1 = IntVar()
        self.colddink_Tax_1 = IntVar()
        #----------Frame_1------------#
        
        F1= customtkinter.CTkFrame(master=self.root, corner_radius=15)
        F1.place(x=0,y=59,relwidth=1, height=70)

        Customer_Details=customtkinter.CTkLabel(F1,text="Customer Details",width=120,height=10,text_font=("arial",10,"bold"), corner_radius=10)
        Customer_Details.place(x=1,y=0)
        Customer_Name=customtkinter.CTkLabel(F1,text="Customer Name",text_font=("times new roman",17,"bold"))
        Customer_Name.grid(row=0,column=0,pady=20,padx=16)
        C1= customtkinter.CTkEntry(F1,placeholder_text="name",width=160,height=35,border_width=1, corner_radius=10,textvariable=self.CustomerName1)
        C1.grid(row=0, column=1)
        Contact_No=customtkinter.CTkLabel(F1,text="Contact No.",text_font=("times new roman",17,"bold"))
        Contact_No.grid(row=0,column=2,pady=20,padx=16)
        C_1= customtkinter.CTkEntry(F1,placeholder_text="phone number",width=160,height=35,border_width=1, corner_radius=10,textvariable=self.Contact_No_1)
        C_1.grid(row=0, column=3)
        Bill_No= customtkinter.CTkLabel(F1, text="Bill No.",text_font=("times new roman",17,"bold"))
        Bill_No.grid(row=0, column=4, pady=20, padx=16)
        B1 =  customtkinter.CTkEntry(F1,placeholder_text="Bill no.",width=160,height=35,border_width=1, corner_radius=10,textvariable=self.Bill_No_1)
        B1.grid(row=0, column=5,padx=16)
        # Search_butt=Button(F1,text="Search",font=("times new roman",15,"bold"),width=10,command=self.Search)
        Search_butt=customtkinter.CTkButton(F1,
                                 width=130,
                                 height=15,
                                 border_width=3,
                                 corner_radius=8,
                                 text=" Search ",
                                 text_font=("Roboto Medium",20),
                                 command=self.Search)
        Search_butt.grid(row=0,column=6,padx=30)
        # ----------Frame_2------------#

        F2 =customtkinter.CTkFrame(master=self.root, corner_radius=15)
        F2.place(x=0, y=145, width=265, height=350)
        Costmatic=customtkinter.CTkLabel(F2,text="Cosmatic",width=120,height=10,text_font=("arial",10,"bold"), corner_radius=10)
        Costmatic.place(x=1, y=0)
        Bath_Soap=customtkinter.CTkLabel(F2,text="Bath Soap",text_font=("arial",14,"bold"))
        Bath_Soap.grid(row=0,column=0,pady=15,padx=16)
        B_S1 =  customtkinter.CTkEntry(F2,width=90,height=30,border_width=1, corner_radius=10,textvariable=self.Bath_Soap_1)
        B_S1.grid(row=0, column=1)
        Face_Cream = customtkinter.CTkLabel(F2,text="Face cream",text_font=("arial",14,"bold"))
        Face_Cream.grid(row=1, column=0, pady=15, padx=16)
        F_C1 =  customtkinter.CTkEntry(F2,width=90,height=30,border_width=1, corner_radius=10,textvariable=self.Face_Cream_1)
        F_C1.grid(row=1, column=1)
        Face_Wash = customtkinter.CTkLabel(F2,text="Face wash",text_font=("arial",14,"bold"))
        Face_Wash.grid(row=3, column=0, pady=10, padx=16)
        F_W1 =  customtkinter.CTkEntry(F2,width=90,height=30,border_width=1, corner_radius=10,textvariable=self.Face_Wash_1)
        F_W1.grid(row=3, column=1)
        Hair_Spray = customtkinter.CTkLabel(F2,text="Hair oil",text_font=("arial",14,"bold"))
        Hair_Spray.grid(row=4, column=0, pady=15, padx=16)
        H_S1=  customtkinter.CTkEntry(F2,width=90,height=30,border_width=1, corner_radius=10,textvariable=self.Hair_Spray_1)
        H_S1.grid(row=4, column=1)
        Hair_Gel = customtkinter.CTkLabel(F2,text="Hair gel",text_font=("arial",14,"bold"))
        Hair_Gel.grid(row=5, column=0,pady=15, padx=16)
        H_G1 =  customtkinter.CTkEntry(F2,width=90,height=30,border_width=1, corner_radius=10,textvariable=self.Hair_Gel_1)
        H_G1.grid(row=5, column=1)
        Body_Losan = customtkinter.CTkLabel(F2,text="Body Losan",text_font=("arial",14,"bold"))
        Body_Losan.grid(row=6, column=0, pady=15, padx=16)
        B_L1 =  customtkinter.CTkEntry(F2,width=90,height=30,border_width=1, corner_radius=10,textvariable=self.Body_Losan_1)
        B_L1.grid(row=6, column=1)
        # ----------Frame_3------------#

        F3 = customtkinter.CTkFrame(master=self.root, corner_radius=15)
        F3.place(x=280, y=145, width=265, height=350)
        Grocery = customtkinter.CTkLabel(F3,text="Grocery",width=120,height=10,text_font=("arial",10,"bold"), corner_radius=10)
        Grocery.place(x=1, y=0)
        Rice = customtkinter.CTkLabel(F3,text="Rice",text_font=("arial",14,"bold"))
        Rice.grid(row=0, column=0, pady=15, padx=16)
        R1=  customtkinter.CTkEntry(F3,width=90,height=30,border_width=1, corner_radius=10,textvariable=self.Rice_1)
        R1.grid(row=0, column=1)
        Food_oil = customtkinter.CTkLabel(F3,text="Food oil",text_font=("arial",14,"bold"))
        Food_oil.grid(row=1, column=0, pady=15, padx=16)
        F_O1 = customtkinter.CTkEntry(F3,width=90,height=30,border_width=1, corner_radius=10,textvariable=self.Food_oil_1)
        F_O1.grid(row=1, column=1)
        Daal = customtkinter.CTkLabel(F3,text="Daal",text_font=("arial",14,"bold"))
        Daal.grid(row=3, column=0, pady=10, padx=16)
        D1 =  customtkinter.CTkEntry(F3,width=90,height=30,border_width=1, corner_radius=10,textvariable=self.Daal_1)
        D1.grid(row=3, column=1)
        Wheat = customtkinter.CTkLabel(F3,text="Wheat",text_font=("arial",14,"bold"))
        Wheat.grid(row=4, column=0, pady=15, padx=16)
        W1 =  customtkinter.CTkEntry(F3,width=90,height=30,border_width=1, corner_radius=10,textvariable=self.Wheat_1)
        W1.grid(row=4, column=1)
        Sugar = customtkinter.CTkLabel(F3,text="sugar",text_font=("arial",14,"bold"))
        Sugar.grid(row=5, column=0, pady=15, padx=16)
        S1 =  customtkinter.CTkEntry(F3,width=90,height=30,border_width=1, corner_radius=10,textvariable=self.Sugar_1)
        S1.grid(row=5, column=1)
        Tea = customtkinter.CTkLabel(F3,text="Biscuits",text_font=("arial",14,"bold"))
        Tea.grid(row=6, column=0, pady=15, padx=16)
        T1 = customtkinter.CTkEntry(F3,width=90,height=30,border_width=1, corner_radius=10,textvariable=self.Tea_1)
        T1.grid(row=6, column=1)
        # ----------Frame_4------------#

        F4 = customtkinter.CTkFrame(master=self.root, corner_radius=15)
        F4.place(x=560, y=145, width=265, height=350)
        Cold_Drink= customtkinter.CTkLabel(F4,text="Cold drinks",width=120,height=10,text_font=("arial",10,"bold"), corner_radius=10)
        Cold_Drink.place(x=1, y=0)
        Maza= customtkinter.CTkLabel(F4,text="Maza",text_font=("arial",14,"bold"))
        Maza.grid(row=0, column=0, pady=15, padx=16)
        M1 = customtkinter.CTkEntry(F4,width=90,height=30,border_width=1, corner_radius=10,textvariable=self.Maza_1)
        M1.grid(row=0, column=1)
        Coca= customtkinter.CTkLabel(F4,text="Dew",text_font=("arial",14,"bold"))
        Coca.grid(row=1, column=0, pady=15, padx=16)
        Co_1 = customtkinter.CTkEntry(F4,width=90,height=30,border_width=1, corner_radius=10,textvariable=self.Coca_1)
        Co_1.grid(row=1, column=1)
        Fruti = customtkinter.CTkLabel(F4,text="Fruti",text_font=("arial",14,"bold"))
        Fruti.grid(row=3, column=0, pady=10, padx=16)
        F1 =customtkinter.CTkEntry(F4,width=90,height=30,border_width=1, corner_radius=10,textvariable=self.Fruti_1)
        F1.grid(row=3, column=1)
        Thumbs_up = customtkinter.CTkLabel(F4,text="Thumbs up",text_font=("arial",14,"bold"))
        Thumbs_up.grid(row=4, column=0, pady=15, padx=16)
        T_u1 = customtkinter.CTkEntry(F4,width=90,height=30,border_width=1, corner_radius=10,textvariable=self.Thumbs_up_1)
        T_u1.grid(row=4, column=1)
        Sprite = customtkinter.CTkLabel(F4,text="Sprite",text_font=("arial",14,"bold"))
        Sprite.grid(row=5, column=0, pady=15, padx=16)
        Sp1 =customtkinter.CTkEntry(F4,width=90,height=30,border_width=1, corner_radius=10,textvariable=self.Sprite_1)
        Sp1.grid(row=5, column=1)
        Limca= customtkinter.CTkLabel(F4,text="Limca",text_font=("arial",14,"bold"))
        Limca.grid(row=6, column=0, pady=15, padx=16)
        L1 = customtkinter.CTkEntry(F4,width=90,height=30,border_width=1, corner_radius=10,textvariable=self.Limca_1)
        L1.grid(row=6, column=1)
        # ----------Frame_5------------#
        F4 = customtkinter.CTkFrame(master=self.root, corner_radius=15)
        F4.place(x=840, y=145, width=440, height=350)
        Heading_2= customtkinter.CTkLabel(F4,text="Bill Detail",text_font=("times new roman",20,"bold"))
        Heading_2.pack(fill=X)
        Scroll_y=Scrollbar(F4,orient=VERTICAL)
        Scroll_y.pack(side=RIGHT,fill=Y)
        self.Text_1= Text(F4,yscrollcommand=Scroll_y.set)
        self.Text_1.pack(side=LEFT, fill=BOTH)
        Scroll_y.config(command=self.Text_1.yview)

        # ----------Frame_6------------#
        F6 = customtkinter.CTkFrame(master=self.root, corner_radius=15)
        F6.place(x=0, y=510, relwidth=1, height=170)
        Billing_Menu= customtkinter.CTkLabel(F6,text="Billing Menu",width=120,height=10,text_font=("arial",10,"bold"), corner_radius=10)
        Billing_Menu.place(x=1, y=0)

        Total_Cosmatic= customtkinter.CTkLabel(F6,text="Total Cosmatic Price",text_font=("times new roman",15,"bold"))
        Total_Cosmatic.grid(row=0, column=0,pady=16)
        T_C1 = customtkinter.CTkEntry(F6,placeholder_text="Bill no.",width=120,height=35,border_width=1, corner_radius=10,textvariable=self.Total_Cosmatic_1)
        T_C1.grid(row=0, column=1)
        Costmatic_Tax=customtkinter.CTkLabel(F6,text="Cosmatic Tax",text_font=("times new roman",15,"bold"))
        Costmatic_Tax.grid(row=0, column=2)
        C_T1 = customtkinter.CTkEntry(F6,placeholder_text="Bill no.",width=120,height=35,border_width=1, corner_radius=10,textvariable=self.Cosmatic_Tax_1)
        C_T1.grid(row=0, column=3)
        Total_Grocery = customtkinter.CTkLabel(F6,text="Total Grocery Price",text_font=("times new roman",15,"bold"))
        Total_Grocery.grid(row=1, column=0,pady=10)
        T_G1 = customtkinter.CTkEntry(F6,placeholder_text="Bill no.",width=120,height=35,border_width=1, corner_radius=10,textvariable=self.Total_Grocery_1)
        T_G1.grid(row=1, column=1)
        Grocery_Tax = customtkinter.CTkLabel(F6,text="Grocery Tax",text_font=("times new roman",15,"bold"))
        Grocery_Tax.grid(row=1, column=2 )
        G_T1 = customtkinter.CTkEntry(F6,placeholder_text="Bill no.",width=120,height=35,border_width=1, corner_radius=10,textvariable=self.Grocery_Tax_1)
        G_T1.grid(row=1, column=3)
        Total_Cold_Drink = customtkinter.CTkLabel(F6,text="Total Cold Drink Price",text_font=("times new roman",15,"bold"))
        Total_Cold_Drink.grid(row=2, column=0,pady=10)
        T_CD1 = customtkinter.CTkEntry(F6,placeholder_text="Bill no.",width=120,height=35,border_width=1, corner_radius=10,textvariable=self.Total_colddrink_1)
        T_CD1.grid(row=2, column=1)
        Cold_Drink_Tax =customtkinter.CTkLabel(F6,text="Cold Drink Tax",text_font=("times new roman",15,"bold"))
        Cold_Drink_Tax.grid(row=2, column=2,padx=16,pady=10)
        C_DT1 = customtkinter.CTkEntry(F6,placeholder_text="Bill no.",width=120,height=35,border_width=1, corner_radius=10,textvariable=self.colddink_Tax_1)
        C_DT1.grid(row=2, column=3)
        # ----------Frame-6_1------------#
        F6_1=customtkinter.CTkFrame(F6, corner_radius=15)
        F6_1.place(x=690,y=10,width=520, height=140 )
        Total_butt=customtkinter.CTkButton(F6_1,
                                 width=200,
                                 height=10,
                                 border_width=3,
                                 corner_radius=8,
                                 text="Total",
                                 text_font=("Roboto Medium",22),command=self.Total)
        Total_butt.grid(row=1,column=0,padx=30,pady=10)
        Bill_Generate_butt = customtkinter.CTkButton(F6_1,
                                 width=200,
                                 height=10,
                                 border_width=3,
                                 corner_radius=8,
                                 text="Generate Bill ",
                                 text_font=("Roboto Medium",22),command=self.Bill_Generate)
        Bill_Generate_butt.grid(row=2, column=0, padx=30, pady=10)
        Clear_butt = customtkinter.CTkButton(F6_1,
                                 width=200,
                                 height=10,
                                 border_width=3,
                                 corner_radius=8,
                                 text="Clear",
                                 text_font=("Roboto Medium",22),command=self.Clear)
        Clear_butt.grid(row=1, column=2, padx=30, pady=10)
        Exit_butt = customtkinter.CTkButton(F6_1,
                                 width=200,
                                 height=10,
                                 border_width=3,
                                 corner_radius=8,
                                 text="Exit",
                                 text_font=("Roboto Medium",22,"bold"),command=exit)
        Exit_butt.grid(row=2, column=2, padx=30, pady=10)
        self.Welcome_bill()
        # print(x)

        #---------------Function Declaration---------#
    def Clear(self):
        # ----------Variable Declaration------------#
        self.CustomerName1.set("")
        self.Contact_No_1.set("")
        self.Bill_No_1.set("")
        # ----------Variable Declaration F2-----------#
        self.Bath_Soap_1.set("0")
        self.Face_Cream_1.set("0")
        self.Face_Wash_1.set("0")
        self.Hair_Spray_1.set("0")
        self.Hair_Gel_1.set("0")
        self.Body_Losan_1.set("0")
        # ----------Variable Declaration F3------------#
        self.Rice_1.set("0")
        self.Wheat_1.set("0")
        self.Sugar_1.set("0")
        self.Tea_1 .set("0")
        self.Daal_1.set("0")
        self.Food_oil_1.set("0")
        # ----------Variable Declaration F4------------#
        self.Maza_1.set("0")
        self.Coca_1.set("0")
        self.Thumbs_up_1.set("0")
        self.Fruti_1.set("0")
        self.Sprite_1.set("0")
        self.Limca_1.set("0")
        # ----------Variable Declaration F5------------#
        self.Total_Cosmatic_1.set("")
        self.Total_Grocery_1.set("")
        self.Total_colddrink_1.set("")
        self.Cosmatic_Tax_1.set("")
        self.Grocery_Tax_1.set("")
        self.colddink_Tax_1.set("")
        self.Welcome_bill()
    def Total(self):
        self.c_b_s=(self.Bath_Soap_1.get()*20)
        self.c_f_c=(self.Face_Cream_1.get() * 110)
        self.c_f_w=(self.Face_Wash_1.get() * 65)
        self.c_h_s= (self.Hair_Spray_1.get() * 200)
        self.c_h_g=(self.Hair_Gel_1.get() * 70)
        self.c_b_l=(self.Body_Losan_1.get() * 40)
        a=(     self.c_b_s+
               self.c_f_c+
               self.c_f_w+
               self.c_h_s+
               self.c_h_g+
               self.c_b_l
          )
        self.Total_Cosmatic_1.set(f"Rs {str(a)}")
        self.g_r=( self.Rice_1.get()*40)
        self.g_d= (self.Daal_1.get()*35)
        self.g_s= (self.Sugar_1.get()*50)
        self.g_t=(self.Tea_1.get()*30)
        self.g_w= (self.Wheat_1.get()*30)
        self.g_f_o=(self.Food_oil_1.get()*30)
        b=(  self.g_r+
        self.g_d+
        self.g_s+
        self.g_t+
        self.g_w+
        self.g_f_o)
        self.Total_Grocery_1.set(f"Rs {str(b)}")
        self.c_m=(self.Maza_1.get()*12)
        self.c_t=(self.Thumbs_up_1.get()*12)
        self.c_f= (self.Fruti_1.get()*12)
        self.c_c=(self.Coca_1.get()*12)
        self.c_s=(self.Sprite_1.get()*12)
        self.c_l= (self.Limca_1.get()*12)
        c=( self.c_m+
        self.c_t+
        self.c_f+
        self.c_c+
        self.c_s+
        self.c_l)
        self.Total_colddrink_1.set(f"Rs {str(c)}")
        #-----------Calculate_Cosmatic_tax----------#
        self.c_tax=round(a*(10/100))
        self.Cosmatic_Tax_1.set(f"Rs {self.c_tax}")
        self.g_tax=round(b*(10/100))
        self.Grocery_Tax_1.set(f"Rs {self.g_tax}")
        self.cd_tax=round(c*(5/100))
        self.colddink_Tax_1.set(f"Rs {self.cd_tax}")
        self.Total= float(self.c_tax+self.g_tax+self.cd_tax+c+a+b)
    def Welcome_bill(self):
        self.Text_1.delete(1.0,END)
        self.Text_1.insert(END,"\t\t     Shop & Smile \n")
        self.Text_1.insert(END,"\t\t   NEW DELHI-110001 \n")
        self.Text_1.insert(END,"\t\t   phone: 8977544557 \n")
        self.Text_1.insert(END,"\t\t     GSTIN:XYZ \n")
        self.Text_1.insert(END, f"____________________________________________________\n")

        self.Text_1.insert(END,"---------------------TAX INVOICE--------------------\n")

        self.Text_1.insert(END, f"Bill No.:   {self.Bill_No_1.get()} \n")
        self.Text_1.insert(END, f"Customer Name : {self.CustomerName1.get()}\n")
        self.Text_1.insert(END, f"Contact No. :{self.Contact_No_1.get()}\n")
        self.Text_1.insert(END, f"----------------------------------------------------\n")
        self.Text_1.insert(END, f"Product\t\t\tQuantity\t\tPrice\n")
        self.Text_1.insert(END, f"----------------------------------------------------\n")

    def Bill_Generate(self):
        self.Welcome_bill()
        if self.CustomerName1.get()=="" and self.Contact_No_1.get()=="":
            tmsg.showerror("Error","Fill Customer Name and Contact No")
        else:
            self.bill_area()
        a=tmsg.askquestion("Billing","Do you want to save this bill?")
        # print (a)
        if a=="yes":
            f=open("files/"+str(self.Bill_No_1.get())+".txt","w")
            f.write(
                    self.Text_1.get(1.0,END)
                    )
            f.close()
    def bill_area(self):
        self.Welcome_bill()
        # -------------Cosmatic-----------#
        if self.Bath_Soap_1.get() != 0:
            self.Text_1.insert(END, f"Bath Soap\t\t\t{self.Bath_Soap_1.get()}\t\t{self.c_b_s}\n")
        if self.Face_Cream_1.get() != 0:
            self.Text_1.insert(END, f"Face Cream\t\t\t{self.Face_Cream_1.get()}\t\t{self.c_f_c}\n")
        if self.Face_Wash_1.get() != 0:
            self.Text_1.insert(END, f"Face Wash\t\t\t{self.Face_Wash_1.get() }\t\t{self.c_f_w}\n")
        if self.Hair_Spray_1.get() != 0:
            self.Text_1.insert(END, f"Hair Spray\t\t\t{self.Hair_Spray_1.get()}\t\t{self.c_h_s}\n")
        if self.Hair_Gel_1.get() != 0:
            self.Text_1.insert(END, f"Hair Gel\t\t\t{self.Hair_Gel_1.get() }\t\t{self.c_h_g}\n")
        if self.Body_Losan_1.get() != 0:
            self.Text_1.insert(END, f"Body Losan\t\t\t{self.Body_Losan_1.get() }\t\t{self.c_b_l}\n")
            # -------------Grocery-----------#
        if self.Rice_1.get() != 0:
            self.Text_1.insert(END, f"Rice\t\t\t{self.Rice_1.get()}\t\t{self.g_r}\n")
        if self.Wheat_1.get() != 0:
            self.Text_1.insert(END, f"Wheat\t\t\t{self.Wheat_1.get()}\t\t{self.g_w}\n")
        if self.Daal_1.get() != 0:
            self.Text_1.insert(END, f"Daal \t\t\t{self.Daal_1.get() }\t\t{self.g_d}\n")
        if self.Food_oil_1.get() != 0:
            self.Text_1.insert(END, f"Food oil\t\t\t{self.Food_oil_1.get()}\t\t{self.g_f_o}\n")
        if self.Sugar_1.get() != 0:
            self.Text_1.insert(END, f"Sugar\t\t\t{self.Sugar_1.get() }\t\t{self.g_s}\n")
        if self.Tea_1.get() != 0:
            self.Text_1.insert(END, f"Tea\t\t\t{self.Tea_1.get() }\t\t{self.g_t}\n")
            # -------------Coldrink--------------#
        if self.Maza_1.get() != 0:
            self.Text_1.insert(END, f"Maza\t\t\t{self.Maza_1.get()}\t\t{self.c_m}\n")
        if self.Coca_1.get() != 0:
            self.Text_1.insert(END, f"Coca\t\t\t{self.Coca_1.get()}\t\t{self.c_c}\n")
        if self.Fruti_1.get() != 0:
            self.Text_1.insert(END, f"Fruti \t\t\t{self.Fruti_1.get() }\t\t{self.c_f}\n")
        if self.Thumbs_up_1.get() != 0:
            self.Text_1.insert(END, f"Thumbs up\t\t\t{self.Thumbs_up_1.get()}\t\t{self.c_t}\n")
        if self.Sprite_1.get() != 0:
            self.Text_1.insert(END, f"Sprite\t\t\t{self.Sprite_1.get() }\t\t{self.c_s}\n")
        if self.Limca_1.get() != 0:
            self.Text_1.insert(END, f"Limca\t\t\t{self.Limca_1.get() }\t\t{self.c_l}\n")
            # ----------Total Tax--------------#
        self.Text_1.insert(END, f"----------------------------------------------------\n")
        if self.c_tax != 0:
            self.Text_1.insert(END, f"Cosmatic Tax:\t\t\t\t\t{self.c_tax}\n")
        if self.g_tax != 0:
            self.Text_1.insert(END, f"Grocery Tax:\t\t\t\t\t{self.g_tax}\n")
        if self.cd_tax != 0:
            self.Text_1.insert(END, f"Cold Drink Tax:\t\t\t\t\t{self.cd_tax}\n")
        self.Text_1.insert(END, f"----------------------------------------------------\n")
        self.Text_1.insert(END, f"Total:\t\t\t\t\t{self.Total}\n")
        self.Text_1.insert(END, f"----------------------------------------------------\n")
        self.Text_1.insert(END, f" \t\t  Thanks for visiting <3 \n")
        
    def Search(self):
        present="no"
        files=os.listdir("files/")
        if len(files)>0:
            for i in files:
                # print(i)
                if i.split(".")[0]==self.Bill_No_1.get():
                    # print("yes")
                    present="yes"
                    f1=open(f"files/{i}","r")
                    self.Text_1.delete(1.0,END)
                    for j in f1:
                        self.Text_1.insert(END,j)
                    f1.close()
        if present=="no":
            tmsg.showerror("Error","File doesn't Existed.")
root=Tk()
B1=Billing(root)
root.mainloop()
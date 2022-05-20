# -*- coding: utf-8 -*-
import time
"""
Created on Thu Dec 30 23:51:01 2021
215321701332
@author: faiza
"""
clients = {
    '000': {
        'name': 'Ahmed Abdelrazek Mohamed',
        'password': '1111',
        'balance': 3500166,
    },
    }
'''
    '203659302214': {
        'name': 'Salma Mohamed Foaad',
        'password': '1390',
        'balance': 520001,
    },
    '126355700193': {
        'name': 'Adel Khaled Abdelrahman',
        'password': '1214',
        'balance': 111000,
    },
    '201455998011': {
        'name': 'Saeed Amin Elsawy',
        'password': '2001',
        'balance': 1200,
    },
    '201122369851': { 
        'name': 'Amir Salama Elgendy',
        'password': '8935',
        'balance': 178933,
    },
    '201356788002': {
        'name': 'Wael Mohamed khairy',
        'password': '3420',
        'balance': 55000,
    },
    '203366789564': {
        'name': 'Mina Sameh Bishoy',
        'password': '1179',
        'balance': 18000,
    },
    '201236787812': {
        'name': 'Omnia Ahmed Awad',
        'password': '1430',
        'balance': 180350,
    },
}
'''

import tkinter as tk                
from tkinter import font  as tkfont 

class My_Atm(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.shared_data = {'Balance':tk.IntVar()}
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, MenuPage,Fawry_Service, Phone,WithdrawPage, Password_changePage, BalancePage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg = "#458B74")
        self.controller = controller
        self.controller.title("Screen")
        self.controller.state("zoomed")
        label1 = tk.Label(self, text = "ATM", fg = "white", bg = "#458B74", font = ("TimeNewRoman",45, 'bold'))
        label1.pack(pady = 25)
        def pass_check():
           global pssing
           global passing_Entry
           Cash_Withdraw=tk.Toplevel()
           Cash_Withdraw.geometry("270x130+500+200")
           Cash_Withdraw.title("checking pass")
           Cash_Withdraw.resizable(width=False, height=False)
           pass_Label=tk.Label(Cash_Withdraw, text="Enter your pass")
           pass_Label.grid(row=0,column=0)
           passing_Entry=tk.Entry(Cash_Withdraw)
           passing_Entry.configure(fg = 'black', show='*')
           passing_Entry.grid(row=0,column=1)
           passing_Button = tk.Button(Cash_Withdraw,text="OK",command=lambda: [Cash_Withdraw.destroy(), controller.show_frame('MenuPage')])
           passing_Button.grid(row=2,column=1) 
           #controller.show_frame('MenuPage')
        label_space = tk.Label(self, height = 4, bg = "#458B74")
        label_space.pack(ipady = 7)
        password_label = tk.Label(self,font =("Tome", 14), fg= "white",text = "Enter your password", height = 4, bg = "#458B74")
        password_label.pack()
        account_No = tk.StringVar()
        account_No_entry = tk.Entry(self,
                                      textvariable = account_No,
                                      font =("Tome", 14), width = 24)
        #ipady for the space
        account_No_entry.pack(ipady = 10)
        account_No_entry.focus_set()
        def account_No_check():
            for i in clients.keys():
                if account_No.get()==i:
                    pass_check()
                    
                    #controller.show_frame("MenuPage")
                    account_No.set('')
                    incorrect_account_no__label['text']=''
                else:
                    incorrect_account_no__label['text']='incorrect account nomber'
        entry_button = tk.Button(self,
                                 text = "Enter",
                                 command = account_No_check,
                                 relief= 'raised',
                                 borderwidth=3,
                                 width= 37,
                                 height= 3)
        entry_button.pack(pady = 10)
        def  handle_focus_in(_):
            account_No_entry.configure(fg = 'black', show='*')
            
        account_No_entry.bind('<FocusIn>',handle_focus_in)
        
        incorrect_account_no__label = tk.Label(self,font =("Tome", 14), fg= "white",text = "", height = 4, bg = "#45B888")
        incorrect_account_no__label.pack(fill='both', expand=True)
        
        bottom_frame = tk.Frame(self, relief ='raised', borderwidth=3)
        bottom_frame.pack(fill = 'x', side = 'bottom')
    
    
        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)

        time_label = tk.Label(bottom_frame,font=('orbitron',12))
        time_label.pack(side='right')

        tick()
class MenuPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg = "#458B74")
        self.controller = controller
        label1 = tk.Label(self, text = "ATM", fg = "white", bg = "#8B864E", font = ("TimeNewRoman",45, 'bold'))
        label1.pack(pady = 25)
        bottom_frame = tk.Frame(self, relief ='raised', borderwidth=3)
        bottom_frame.pack(fill = 'x', side = 'bottom')
        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)

        time_label = tk.Label(bottom_frame,font=('orbitron',12))
        time_label.pack(side='right')

        tick()
        #My main menu word
        
        main_menu_label = tk.Label(self,
                                 text='Main Menu',
                                 font=('orbitron',20, 'bold'),
                                 fg='white',
                                 bg = '#8B864E')
        main_menu_label.pack(ipady = 0)
        label_space = tk.Label(self, height = 1, bg = "#458B74")
        label_space.pack(ipady = 7)
        #my selection table
        selection_label = tk.Label(self,
                                 text='Please make a selection',
                                 font=('orbitron',13),
                                 fg='white',
                                 bg='#8B864E',
                                 anchor='w')
        selection_label.pack(fill='x',ipady = 5)
        label_space = tk.Label(self, height = 1, bg = "#458B74")
        label_space.pack(ipady = 7)
        button_frame = tk.Frame(self,bg='#33334d')
        button_frame.pack(fill='both',expand=True)

        def withdraw():
            controller.show_frame('WithdrawPage')

        withdraw_button = tk.Button(button_frame,
                                text='Withdraw',
                                command=withdraw,
                                relief='raised',
                                borderwidth=3,
                                width=30,
                                font =("Tome", 10, 'bold'),
                                height=4)
        withdraw_button.grid(row=0,column=0,pady=5)

        def Password_change():
            controller.show_frame('Password_changePage')

        Password_change_button = tk.Button(button_frame,
                                 text='Password_change',
                                 command=Password_change,
                                 relief='raised',
                                 borderwidth=3,
                                 width=30,
                                font =("Tome", 10, 'bold'),
                                 height=4)
        Password_change_button.grid(row=1,column=0,pady=5)


        def balance():
            controller.show_frame('BalancePage')

        balance_button = tk.Button(button_frame,
                                   text='Balance',
                                   command=balance,
                                   relief='raised',
                                   borderwidth=3,
                                   width=30,
                                font =("Tome", 10, 'bold'),
                                   height=4)
        balance_button.grid(row=2,column=0,pady=5)
        
        def Phone():
            controller.show_frame('Phone')

        balance_button = tk.Button(button_frame,
                                   text='Phone',
                                   command=Phone,
                                   relief='raised',
                                   borderwidth=3,
                                   width=30,
                                   font =("Tome", 10, 'bold'),
                                   height=4)
        balance_button.grid(row=3,column=0,pady=2)

        def Fawry_Service():
            controller.show_frame('Fawry_Service')

        balance_button = tk.Button(button_frame,
                                   text='Fawry_Service',
                                   command=Fawry_Service,
                                   relief='raised',
                                   borderwidth=3,
                                   width=30,
                                   font =("Tome", 10, 'bold'),
                                   height=4)
        balance_button.grid(row=3,column=0,pady=2)

        def exit():
            controller.show_frame('StartPage')

        exit_button = tk.Button(button_frame,
                                text='Exit',
                                command=lambda: main_window.destroy(),
                                relief='raised',
                                borderwidth=3,
                                width=30,
                                font =("Tome", 10, 'bold'),
                                height=2)
        exit_button.grid(row=4,column=0,pady=5)

class WithdrawPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg = "#458B74")
        self.controller = controller
        label1 = tk.Label(self, text = "ATM", fg = "white", bg = "#8B864E", font = ("TimeNewRoman",45, 'bold'))
        label1.pack(pady = 25)
        bottom_frame = tk.Frame(self, relief ='raised', borderwidth=3)
        bottom_frame.pack(fill = 'x', side = 'bottom')
        choose_amount_label = tk.Label(self,
                                 text='choose the amount that you want to withdraw',
                                 font=('orbitron',20, 'bold'),
                                 fg='white',
                                 bg = '#8B864E')
        choose_amount_label.pack(ipady = 0)
                
        def pass_check():
           global pssing
           global passing_Entry
           Cash_Withdraw=tk.Toplevel()
           Cash_Withdraw.geometry("270x130+500+200")
           Cash_Withdraw.title("checking pass")
           Cash_Withdraw.resizable(width=False, height=False)
           pass_Label=tk.Label(Cash_Withdraw, text="Enter CashwithDraw")
           pass_Label.grid(row=0,column=0)
           passing_Entry=tk.Entry(Cash_Withdraw)
           passing_Entry.grid(row=0,column=1)
           passing_Button = tk.Button(Cash_Withdraw,text="OK",command=lambda:controller.show_frame('MenuPage'))
           passing_Button.grid(row=2,column=1) 

                        
           
        def Cash_Withdraw_Window():
           global Cash_Withdraw
           global Cash_Withdraw_Entry
           Cash_Withdraw=tk.Toplevel()
           Cash_Withdraw.geometry("270x130+500+200")
           Cash_Withdraw.title("ATM Cash WithDraw")
           Cash_Withdraw.resizable(width=False, height=False)

           Cash_Withdraw_Label=tk.Label(Cash_Withdraw, text="Enter CashwithDraw")
           Cash_Withdraw_Label.grid(row=0,column=0)
           Cash_Withdraw_Entry=tk.Entry(Cash_Withdraw)
           Cash_Withdraw_Entry.grid(row=0,column=1)
           Cash_Withdraw_Button = tk.Button(Cash_Withdraw,text="OK",command=lambda:[Cash_Withdraw.destroy(),ThankYou_Window()])
           Cash_Withdraw_Button.grid(row=2,column=1)    
           
        
        def ThankYou_Window():
        	global ThankYou
        	ThankYou=tk.Toplevel()
        	ThankYou.geometry("270x100+500+200")
        	ThankYou.title("ATM Thanks")
        	ThankYou.resizable(width=False, height=False)
        	ThankYou_Label=tk.Label(ThankYou, text="Thank you")
        	ThankYou_Label.grid(row=0,column=2)
        	ThankYou_Button = tk.Button(ThankYou,text="Ok",command=lambda:[ThankYou.destroy(),controller.show_frame('MenuPage')])
        	ThankYou_Button.grid(row=1,column=2)
        
            
        button_frame = tk.Frame(self,bg='#33334d')
        button_frame.pack(fill='both',expand=True)
        twenty_button = tk.Button(button_frame,
                                                       text='New CashWith Draw Operation',
                                                       command=lambda:Cash_Withdraw_Window(),
                                                       relief='raised',
                                                       font = ("TimeNewRoman",10, 'bold'),
                                                       borderwidth=3,
                                                       width=50,
                                                       height=5)
        twenty_button.grid(row=0,column=0,pady=5)
        
        
        bottom_frame = tk.Frame(self, relief ='raised', borderwidth=3)
        bottom_frame.pack(fill = 'x', side = 'bottom')
        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)

        time_label = tk.Label(bottom_frame,font=('orbitron',12))
        time_label.pack(side='right')

        tick()
        
      
class Password_changePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg = "#458B74")
        self.controller = controller
        label1 = tk.Label(self, text = "Password change", fg = "white", bg = "#8B864E", font = ("TimeNewRoman",45, 'bold'))
        label1.pack(pady = 25)
        bottom_frame = tk.Frame(self, relief ='raised', borderwidth=3)
        bottom_frame.pack(fill = 'x', side = 'bottom')
        

        password_label = tk.Label(self,font =("Tome", 14), fg= "white",text = "Enter the new password", height = 4, bg = "#458B74")
        password_label.pack()
        account_No = tk.StringVar()
        account_No_entry1 = tk.Entry(self,
                                      textvariable = account_No,
                                      font =("Tome", 14), width = 24)
        #ipady for the space
        account_No_entry1.pack(ipady = 10)
        account_No_entry1.focus_set()
        
        password_label = tk.Label(self,font =("Tome", 14), fg= "white",text = "Please repeate the password", height = 4, bg = "#458B74")
        password_label.pack()
        account_No = tk.StringVar()
        account_No_entry2 = tk.Entry(self,
                                      textvariable = account_No,
                                      font =("Tome", 14), width = 24)
        account_No_entry1.configure(fg = 'black', show='*')
        account_No_entry2.configure(fg = 'black', show='*')
        #ipady for the space
        account_No_entry2.pack(ipady = 10)
        account_No_entry2.focus_set()
            
        label_space = tk.Label(self, height = 4, bg = "#458B74")
        label_space.pack(ipady = 7)
        Thank_Button = tk.Button(self,text="Ok",command=lambda:controller.show_frame('MenuPage'))
        Thank_Button.pack()
        #checking
        if account_No_entry1.get() == account_No_entry2.get():
           controller.show_frame('MenuPage')
        elif account_No_entry1.get() != account_No_entry2.get():
        	sorry=tk.Toplevel()
        	sorry.geometry("270x100+500+200")
        	sorry.title("ATM Thanks")
            
class Fawry_Service(tk.Frame):


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg = "#458B74")
        self.controller = controller
        label1 = tk.Label(self, text = "FawryService", fg = "white", bg = "#8B864E", font = ("TimeNewRoman",45, 'bold'))
        label1.pack(pady = 25)
        bottom_frame = tk.Frame(self, relief ='raised', borderwidth=3)
        bottom_frame.pack(fill = 'x', side = 'bottom')
        
        
        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)

        time_label = tk.Label(bottom_frame,font=('orbitron',12))
        time_label.pack(side='right')
        label_space = tk.Label(self, height = 1, bg = "#458B74")
        label_space.pack(ipady = 7)
        tick()
        balance_button = tk.Button(self,
                                   text='Orange Recharge ',
                                   command=lambda:controller.show_frame('Phone'), 
                                   relief='raised',
                                   borderwidth=3,
                                   width=50,
                                   font =("Tome", 10, 'bold'),
                                   height=4)
        balance_button.pack()
        label_space = tk.Label(self, height = 1, bg = "#458B74")
        label_space.pack(ipady = 7)
        balance_button = tk.Button(self,
                                   text='Etisalat Recharge',
                                   command=lambda:controller.show_frame('Phone'), 
                                   relief='raised',
                                   borderwidth=3,
                                   width=50,
                                   font =("Tome", 10, 'bold'),
                                   height=4)
        balance_button.pack()
        label_space = tk.Label(self, height = 1, bg = "#458B74")
        label_space.pack(ipady = 7)
        balance_button = tk.Button(self,
                                   text='Vodafone Recharge',
                                   command=lambda:controller.show_frame('Phone'), 
                                   relief='raised',
                                   borderwidth=3,
                                   width=50,
                                   font =("Tome", 10, 'bold'),
                                   height=4)
        balance_button.pack()
        label_space = tk.Label(self, height = 1, bg = "#458B74")
        label_space.pack(ipady = 7)
        balance_button = tk.Button(self,
                                   text='We Recharge',
                           command=lambda:controller.show_frame('Phone'),                           
                                   relief='raised',
                                   borderwidth=3,
                                   width=50,
                                   font =("Tome", 10, 'bold'),
                                   height=4)
        balance_button.pack()

class Phone(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg = "#458B74")
        self.controller = controller
        label1 = tk.Label(self, text = "Contact", fg = "white", bg = "#8B864E", font = ("TimeNewRoman",45, 'bold'))
        label1.pack(pady = 25)
        
        password_label = tk.Label(self,font =("Tome", 14), fg= "white",text = "Please enter your phone number", height = 4, bg = "#458B74")
        password_label.pack()
        account_No = tk.StringVar()
        account_No_entry2 = tk.Entry(self,
                                      textvariable = account_No,
                                      font =("Tome", 14), width = 24)
        #ipady for the space
        account_No_entry2.pack(ipady = 10)
        account_No_entry2.focus_set()
        label_space = tk.Label(self, height = 1, bg = "#458B74")
        label_space.pack(ipady = 7)
        password_label = tk.Label(self,font =("Tome", 14), fg= "white",text = "Please enter the amount of charge", height = 4, bg = "#458B74")
        password_label.pack()
        account_No = tk.StringVar()
        account_No_entry2 = tk.Entry(self,
                                      textvariable = account_No,
                                      font =("Tome", 14), width = 10)
        #ipady for the space
        account_No_entry2.pack(ipady = 10)
        account_No_entry2.focus_set()
            
        
        
      
class BalancePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg = "#458B74")
        self.controller = controller
        label1 = tk.Label(self, text = "YourBalanc", fg = "white", bg = "#8B864E", font = ("TimeNewRoman",45, 'bold'))
        label1.pack(pady = 25)
        bottom_frame = tk.Frame(self, relief ='raised', borderwidth=3)
        bottom_frame.pack(fill = 'x', side = 'bottom')
        bottom_frame = tk.Frame(self, relief ='raised', borderwidth=3)
        bottom_frame.pack(fill = 'x', side = 'bottom')
        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)

        time_label = tk.Label(bottom_frame,font=('orbitron',12))
        time_label.pack(side='right')

        tick()
    
   
            
        balance_button = tk.Button(self,
                                   text=str(clients['000']['name']),
                                   command='',
                                   relief='raised',
                                   borderwidth=3,
                                   width=30,
                                font =("Tome", 10, 'bold'),
                                   height=4)
        balance_button.pack()
        
        label_space = tk.Label(self, height = 1, bg = "#458B74")
        label_space.pack(ipady = 7)
        
        balance_button = tk.Button(self,
                                   text=str(clients['000']['balance']),
                                   command='',
                                   relief='raised',
                                   borderwidth=3,
                                   width=30,
                                font =("Tome", 10, 'bold'),
                                   height=4)
        balance_button.pack()

        label_space = tk.Label(self, height = 1, bg = "#458B74")
        label_space.pack(ipady = 7)
        balance_button = tk.Button(self,
                                   text='Ok',
                                   command=lambda:controller.show_frame('MenuPage'),                                   relief='raised',
                                   borderwidth=3,
                                   width=10,
                                font =("Tome", 10, 'bold'),
                                   height=2)
        balance_button.pack()



if __name__ == "__main__":
    main_window = My_Atm()
    main_window.mainloop()

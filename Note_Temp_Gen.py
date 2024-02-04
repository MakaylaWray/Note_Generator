import tkinter as tk
from tkinter import Scrollbar

class RootWindow(tk.Tk):
    #Creates the root window to hold all frames and widgets created
    def __init__(self):
        super().__init__()
        self.title("Note Template Generator")
        self.geometry("400x150")
        LoginFrame(self)
    

class LoginFrame(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.grid()
        self.configure(width=400, height = 150)
        self.create_login_widgets()
    
    def create_login_widgets(self):
        self.msid_label = tk.Label(self, text = "Enter Your MSID").grid(row=0, column=0)
        self.msid_entry = tk.Entry(self)
        self.msid_entry.grid(row=0, column=1)
        self.continue_button = tk.Button(self, text="Continue", command = self.continue_button_clicked).grid(row=2)

    def gather_msid(self):
        self.msid = self.msid_entry.get()
        return self.msid
    
    def continue_button_clicked(self):   
        self.gather_msid()    
        self.destroy_login_widgets()
        PendCode(self)
    
    def destroy_login_widgets(self):
        for frame in self.winfo_children ():
            frame.destroy()


class PendCode(tk.Frame):
        def __init__(self, container):
            super().__init__(container)
            self.grid()
            self.configure(width=400, height = 150)
            self.create_pendcode_widgets()

        def create_pendcode_widgets(self):
            self.pend_label = tk.Label(self, text="Select Pend Code").grid(row=0, column=0)
            options = ["PNP 001 / PNP 004", "PNP 002", "PNP 005", "PNP 006", "PNP 007 / PNP 011", "PNP 015", "PNP 024", "Chronic PNP 002 / PNP 018"]
            self.clicked = tk.StringVar(self)
            self.clicked.set("Pend Code")
            self.pend_menu = tk.OptionMenu(self, self.clicked, *options).grid(row=0, column=1)
            self.continue_button = tk.Button(self, text="Continue", command= self.continue_button_clicked).grid(row=1)

        def gather_pend_code(self):
            self.pend_code = self.clicked.get()
            return self.pend_code
        
        def continue_button_clicked(self):   
            self.gather_pend_code()    
            self.destroy_verification_widgets()
            OutreachStatus(self)

        def destroy_verification_widgets(self):
             for frame in self.winfo_children ():
                frame.destroy()

class OutreachStatus(tk.Frame):
        def __init__(self, container):
            super().__init__(container)
            self.grid()
            self.configure(width=400, height = 150)
            self.create_outreach_widgets()

        def create_outreach_widgets(self):
            #Creates the Widgets needed for Outreach Status Frame
            self.label_1 = tk.Label(self, text = "Select Outreach Status").grid(row=0, column=0)
            self.made_contact_button = tk.Button(self, text="Made Contact",  command = self.gather_outreach_status).grid(row=1, column=0)
            #self.no_contact_button = tk.Button(self, text="No Contact or Voicemail", command = self.no_contact).grid(row=2, column=0)
            #self.left_message_button = tk.Button(self, text="Left Message/ Voicemail", command = self.left_message).grid(row=3, column=0)
        """
        def no_contact(self):
            self.label_2 = tk.Label(self, text="Did Automated Voice Recording verify provider?").grid(row=4, column=0)
            self.yes_avr = tk.Button(self, text="Yes").grid(row=5, column=0)
            self.no_avr=tk.Button(self, text="No").grid(row=5, column=1)
            
        def left_message(self):
            self.label_2 = tk.Label(self, text="Did Automated Voice Recording/Office verify provider?").grid(row=4, column=0)
            self.yes_avr = tk.Button(self, text="Yes").grid(row=5, column=0)
            self.no_avr=tk.Button(self, text="No").grid(row=5, column=1)
        """        
        def gather_outreach_status(self):
            self.destroy_pendcode_widgets()
            Verification(self)


        def destroy_pendcode_widgets(self):
             for frame in self.winfo_children ():
                frame.destroy()

    

class Verification(tk.Frame):
        def __init__(self, container):
            super().__init__(container)
            self.grid()
            self.configure(width=400, height = 150)
            self.create_verification_widgets()

        def create_verification_widgets(self):
            self.label_1 = tk.Label(self, text = "Verification Information").grid(row= 0, column=1)   
            self.verifiedCI_label =tk.Label(self, text ="Verified Chart ID(s)").grid(row= 1, column=0)
            self.verifiedCI_entry = tk.Entry(self)
            self.verifiedCI_entry.grid(row=1, column=1)
                
            self.unverifiedCI_label =tk.Label(self, text ="Unverified Chart ID(s)").grid(row= 2, column=0)
            self. unverifiedCI_entry=tk.Entry(self)
            self.unverifiedCI_entry.grid(row = 2, column=1)
                
            self.verified_provider_label =tk.Label(self, text ="Verified Provider(s)").grid(row=3, column=0)
            self.verified_provider_entry=tk.Entry(self)
            self.verified_provider_entry.grid(row=3, column=1)
                
            self.unverified_provider_label =tk.Label(self, text ="Unverified Provider(s)").grid(row=4, column =0)
            self.unverified_provider_entry=tk.Entry(self)
            self.unverified_provider_entry.grid(row=4, column=1)
                
            self.address_label =tk.Label(self, text ="Address").grid(row=5, column=0)
            self.address_entry = tk.Entry(self)
            self.address_entry.grid(row=5, column=1)

            self.destination_label =tk.Label(self, text ="Destination Method").grid(row=6, column=0)
            self.destination_methods = ["Fax", "Mail", "Ciox Portal", "Ciox Embedded Site", "Ciox Remote", "HIH"]
            self.clicked_destination = tk.StringVar(self)
            self.clicked_destination.set("Fax")
            self.destination_menu = tk.OptionMenu(self, self.clicked_destination, *self.destination_methods)
            self.destination_menu.grid(row=6, column=1)

            self.additional_information_label = tk.Label(self, text="Additional Information").grid(row=7, column= 0)
            self.additional_information = tk.Entry(self)
            self.additional_information.grid(row=7, column=1)
            
            self.continue_button = tk.Button(self, text="Continue", command=self.continue_button_clicked)
            self.continue_button.grid()

        def gather_information(self):
            self.verifiedCI = self.verifiedCI_entry.get()
            self.unverifiedCI = self. unverifiedCI_entry.get()
            self.verified_provider = self.verified_provider_entry.get()
            self.unverified_provider = self.unverified_provider_entry.get()
            self.address = self.address_entry.get()                                                                                                                                                                                                                                    
            self.clicked_destination  = self.clicked_destination.get()
            self.additional_information = self.additional_information.get()
            return self.verifiedCI , self.unverifiedCI , self.verified_provider , self.unverified_provider, self.address, self.clicked_destination, self.additional_information

        def continue_button_clicked(self):   
            self.gather_information()    
            self.destroy_verification_widgets()
            CollectionAllInformation()

        def destroy_verification_widgets(self):
            for frame in self.winfo_children ():
                frame.destroy()



class CollectionAllInformation(tk.Frame):
    print('Makayla Wray')

    


    



if __name__ == "__main__":
    root = RootWindow()
    root.mainloop()

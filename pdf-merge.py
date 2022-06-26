import tkinter
import customtkinter
from tkinter import messagebox, filedialog
from tkinter import *


class MergeApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.location_var = tkinter.StringVar()
        self.destination_var = tkinter.StringVar()
        self.geometry("750x300")
        self.title("PDF Merger")
        
        

        
        self.frame = customtkinter.CTkFrame(master=self, width=600,height=160,corner_radius=10)
        self.frame.pack(padx=20, pady=40)
        self.frame.place(relx=0.12, rely=0.14)
        
        
        
        self.frame2 = customtkinter.CTkFrame(master=self, corner_radius=10)
        self.frame2.pack()
        self.frame2.place(relx=0.12, rely=0.34)
        
        self.link_Label = customtkinter.CTkLabel(master=self.frame, text ="Files To Copy")
        self.link_Label.pack(side="left", padx=11, pady=11)
        
        
        self.source_browseButton = customtkinter.CTkButton(master=self.frame, text ="Browse", command = self.SourceBrowse, width = 15)
        self.source_browseButton.pack(side="right", padx=11, pady=11)
        
        
        self.sourceText = customtkinter.CTkEntry(master=self.frame, width = 300, textvariable = self.location_var)
        self.sourceText.pack(side="left", padx=11,pady=11)
        


        self.link_Label2 = customtkinter.CTkLabel(master=self.frame2, text ="Destination")
        self.link_Label2.pack(side="left", padx=11, pady=11)
        
        
        self.source_browseButton2 = customtkinter.CTkButton(master=self.frame2, text ="Browse", command = self.DestinationBrowse, width = 15)
        self.source_browseButton2.pack(side="right", padx=11, pady=11)
        
        
        self.destinationText = customtkinter.CTkEntry(master=self.frame2, width = 300, textvariable = self.destination_var)
        self.destinationText.pack(side="left", padx=11,pady=11)




        self.copyButton = customtkinter.CTkButton(master=self, text ="Copy Files", command = self.SourceBrowse, width = 15)
        # self.copyButton.pack(padx=11,pady=11)
        self.copyButton.place(relx=0.2, rely=0.55)

        self.moveButton = customtkinter.CTkButton(master=self, text ="Move Files", command = self.SourceBrowse, width = 15)
        # self.moveButton.pack(padx=11,pady=11)
        self.moveButton.place(relx=0.33, rely=0.55)
        
        self.mergeButton = customtkinter.CTkButton(master=self, text ="Merge Files", command = self.SourceBrowse, width = 15, fg_color="green", hover_color="darkgreen")
        # self.mergeButton.pack(side="top", padx=11, pady=11)
        self.mergeButton.place(relx=0.7, rely=0.55)

        self.removeButton = customtkinter.CTkButton(master=self, text ="Remove Files", command = self.SourceBrowse, width = 15, fg_color="red", hover_color="darkred")
        # self.removeButton.pack(side="top", padx=11, pady=11)
        self.removeButton.place(relx=0.5, rely=0.74)
        
        

        # self.button = customtkinter.CTkButton(self, text="Create Toplevel", command=self.create_toplevel)
        # self.button.pack(side="bottom", padx=40, pady=40)
        # self.button.place(relx=0.6, rely=0.7)
        

    def create_toplevel(self):
        window = customtkinter.CTkToplevel(self)
        window.geometry("400x200")

        # create label on CTkToplevel window
        label = customtkinter.CTkLabel(window, text="CTkToplevel window")
        label.pack(side="top", fill="both", expand=True, padx=40, pady=40)


    def SourceBrowse(self):
        self.files_list = list(filedialog.askopenfilenames(initialdir =""))
        self.sourceText.insert('1', self.files_list)
    
    def DestinationBrowse(self):
        self.destinationdirectory = filedialog.askdirectory(initialdir ="")
        self.destinationText.insert('1', self.destinationdirectory)

app = MergeApp()
app.mainloop()

import os
import shutil
import tkinter
import customtkinter
from PyPDF2 import PdfFileMerger

from tkinter import filedialog
from tkinter import *


class MergeApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x350")
        self.title("PDF Merger")

        self.merger = PdfFileMerger()


        self.location_var = tkinter.StringVar()
        self.destinationLocation = tkinter.StringVar()
        self.mergeLocation = tkinter.StringVar()
        
        self.frame = customtkinter.CTkFrame(master=self, width=600,height=160,corner_radius=10)
        self.frame.pack(padx=20, pady=40)
        self.frame.place(relx=0.12, rely=0.14)
        
        
        
        self.frame2 = customtkinter.CTkFrame(master=self, corner_radius=10)
        self.frame2.pack()
        self.frame2.place(relx=0.12, rely=0.30)


        self.frame3 = customtkinter.CTkFrame(master=self, corner_radius=10)
        self.frame3.pack()
        self.frame3.place(relx=0.12, rely=0.55)
        
        
        self.copyLabel = customtkinter.CTkLabel(master=self.frame, text ="Files To Copy")
        self.copyLabel.pack(side="left", padx=11, pady=11)
        
        
        self.source_browseButton = customtkinter.CTkButton(master=self.frame, text ="Browse", command = self.SourceBrowse, width = 15)
        self.source_browseButton.pack(side="right", padx=11, pady=11)
        
        
        self.sourceText = customtkinter.CTkEntry(master=self.frame, width = 300, textvariable = self.location_var)
        self.sourceText.pack(side="left", padx=11,pady=11)
        


        self.destinationLabel = customtkinter.CTkLabel(master=self.frame2, text ="Destination")
        self.destinationLabel.pack(side="left", padx=11, pady=11)
        
        
        self.dest_browseButton2 = customtkinter.CTkButton(master=self.frame2, text ="Browse", command = self.DestinationBrowse, width = 15)
        self.dest_browseButton2.pack(side="right", padx=11, pady=11)
        
        
        self.destinationText = customtkinter.CTkEntry(master=self.frame2, width = 300, textvariable = self.destinationLocation)
        self.destinationText.pack(side="left", padx=11,pady=11)



        self.mergeLabel = customtkinter.CTkLabel(master=self.frame3, text ="Merge From")
        self.mergeLabel.pack(side="left", padx=11, pady=11)

        self.dest_browseButton3 = customtkinter.CTkButton(master=self.frame3, text ="Browse", command = self.MergeBrowse, width = 15)
        self.dest_browseButton3.pack(side="right", padx=11, pady=11)
        
        
        self.mergebrowseText = customtkinter.CTkEntry(master=self.frame3, width = 300, textvariable = self.mergeLocation)
        self.mergebrowseText.pack(side="left", padx=11,pady=11)


        self.copyButton = customtkinter.CTkButton(master=self, text ="Copy Files", command = self.CopyFile, width = 15)
        self.copyButton.place(relx=0.2, rely=0.75)

        self.moveButton = customtkinter.CTkButton(master=self, text ="Move Files", command = self.MoveFile, width = 15)
        self.moveButton.place(relx=0.33, rely=0.75)
        
        self.mergeButton = customtkinter.CTkButton(master=self, text ="Merge Files", command = self.MergeFiles, width = 15, fg_color="green", hover_color="darkgreen")
        self.mergeButton.place(relx=0.7, rely=0.75)

        self.removeButton = customtkinter.CTkButton(master=self, text ="Remove Files", command = self.RemoveFiles, width = 15, fg_color="red", hover_color="darkred")
        self.removeButton.place(relx=0.5, rely=0.75)
        


    def create_toplevel(self):
        window = customtkinter.CTkToplevel(self)
        window.geometry("400x200")

        # create label on CTkToplevel window
        label = customtkinter.CTkLabel(window, text="CTkToplevel window")
        label.pack(side="top", fill="both", expand=True, padx=40, pady=40)

        # Open filedialog and allow user to select files
    def SourceBrowse(self):
        self.files_list = list(filedialog.askopenfilenames(initialdir =""))
        self.sourceText.insert('1', self.files_list)
    
        # Open filedialog and ask for directory as destination
    def DestinationBrowse(self):
        self.destinationdirectory = filedialog.askdirectory(initialdir ="")
        self.destinationText.insert('1', self.destinationdirectory)

    def MergeBrowse(self):
        self.files_list = filedialog.askdirectory(initialdir ="")
        self.mergebrowseText.insert('1', self.files_list)


        # Gets the files selected by the user in the SourceBrowse()
    def CopyFile(self):
        files_list = self.files_list
        destination_location = self.destinationLocation.get()

        for f in files_list:
            print("FROM COPY:",f)
            shutil.copy(f, destination_location)

        window = customtkinter.CTkToplevel(self)
        window.geometry("300x150")
        window.title("PDF Merger - Copy")
        window.grab_set()
        # Create label on Copy window
        label = customtkinter.CTkLabel(window, text="Successfully copied all files.", text_color="lightgreen")
        label.pack(side="top", fill="both", expand=True, padx=20, pady=20)
        

        # Remove all files ending with'pdf' from mergeLocation
    def RemoveFiles(self):
        mergeLocation = self.mergeLocation.get()
        source_dir = mergeLocation
        file_list = self.files_list
        os.chdir(file_list)

        for item in os.listdir(source_dir):
            if item.endswith('pdf'):
                os.remove(item)


    def MoveFile(self):
        files_list = self.files_list
        destination_location = self.destinationLocation.get()

        for f in files_list:
            shutil.move(f, destination_location)

        window = customtkinter.CTkToplevel(self)
        window.geometry("300x150")
        window.title("PDF Merger - Move")
        
        # Create label on Move window
        label = customtkinter.CTkLabel(window, text="Successfully moved all files.", text_color="lightgreen")
        label.pack(side="top", fill="both", expand=True, padx=20, pady=20)

        # Open filedialog and ask for location. Merge files and save in selected location.
    def MergeFiles(self):
        mergeLocation = self.mergeLocation.get()
        source_dir = mergeLocation


        save_location = filedialog.asksaveasfile(
                        mode = 'wb',
                        defaultextension='pdf')
        pdf_files = []
        count = 0

        if save_location != None:

            for item in os.listdir(source_dir):
                if item.endswith('pdf'):
                    pdf_files.append(item)
                    
            file_list = self.files_list
            os.chdir(file_list)


            for file in pdf_files:
                self.merger.append(file)
                count += 1
                # total = len(pdf_files)
            self.merger.write(save_location)
            self.merger.close()
    

            window = customtkinter.CTkToplevel(self)
            window.geometry("300x150")
            window.title("PDF Merger - Save")
            window.grab_set()

            # Create label on Save window
            label = customtkinter.CTkLabel(window, text="Files merged successfully!", text_color="lightgreen")
            label.pack(side="top", fill="both", expand=True, padx=20, pady=20)

app = MergeApp()
app.mainloop()

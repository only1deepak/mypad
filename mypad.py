
import tkinter 
import os     
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
  
class Notepad: 
  
    __root = Tk() 
  
     
    __thisWidth = 300
    __thisHeight = 300
    __thisTextArea = Text(__root) 
    __thisMenuBar = Menu(__root) 
    __thisFileMenu = Menu(__thisMenuBar, tearoff=0) 
    __thisEditMenu = Menu(__thisMenuBar, tearoff=0) 
    __thisHelpMenu = Menu(__thisMenuBar, tearoff=0) 
      
     
    __thisScrollBar = Scrollbar(__thisTextArea)      
    __file = None
  
    def __init__(self,**kwargs): 
  
        # icon 
        try: 
                self.__root.wm_iconbitmap("Notepad.ico")  
        except: 
                pass
  
        # Set window size  
  
        try: 
            self.__thisWidth = kwargs['width'] 
        except KeyError: 
            pass
  
        try: 
            self.__thisHeight = kwargs['height'] 
        except KeyError: 
            pass
  
        # window text 
        self.__root.title("Unnamed - Deepak's Note") 
  
         
        screenWidth = self.__root.winfo_screenwidth() 
        screenHeight = self.__root.winfo_screenheight() 
      
        # For left-allign
        left = (screenWidth / 2) - (self.__thisWidth / 2)  
          
        # For right-allign 
        top = (screenHeight / 2) - (self.__thisHeight /2)  
          
        # For top and bottom 
        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth, 
                                              self.__thisHeight, 
                                              left, top))  
  
        # To make the textarea auto resizable 
        self.__root.grid_rowconfigure(0, weight=1) 
        self.__root.grid_columnconfigure(0, weight=1) 
  
         
        self.__thisTextArea.grid(sticky = N + E + S + W) 
          
        # To open new file 
        self.__thisFileMenu.add_command(label="New", 
                                        command=self.__newFile)     
          
        # To open an existing file 
        self.__thisFileMenu.add_command(label="Open", 
                                        command=self.__openFile) 
          
        # To save current file 
        self.__thisFileMenu.add_command(label="Save", 
                                        command=self.__saveFile)     
  
        # To create a line in the dialog         
        self.__thisFileMenu.add_separator()                                          
        self.__thisFileMenu.add_command(label="Exit", 
                                        command=self.__quitApplication) 
        self.__thisMenuBar.add_cascade(label="File", 
                                       menu=self.__thisFileMenu)      
          
        #cut  
        self.__thisEditMenu.add_command(label="Cut", 
                                        command=self.__cut)              
      
        #copy     
        self.__thisEditMenu.add_command(label="Copy", 
                                        command=self.__copy)          
          
        # paste 
        self.__thisEditMenu.add_command(label="Paste", 
                                        command=self.__paste)  
        # alignment feature
        self.__thisEditMenu.add_command(label="Left Align", 
                                        command=self.__leftAlign)
        self.__thisEditMenu.add_command(label="Center Align", 
                                        command=self.__centerAlign)
        self.__thisEditMenu.add_command(label="Right Align", 
                                        command=self.__rightAlign)                                      
          
        #editing 
        self.__thisMenuBar.add_cascade(label="Edit", 
                                       menu=self.__thisEditMenu)      
          
        # description of the notepad 
        self.__thisHelpMenu.add_command(label="About Notepad", 
                                        command=self.__showAbout)  
        self.__thisMenuBar.add_cascade(label="Help", 
                                       menu=self.__thisHelpMenu) 
  
        self.__root.config(menu=self.__thisMenuBar) 
  
        self.__thisScrollBar.pack(side=RIGHT,fill=Y)                     
          
                 
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)      
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set) 
      
          
    def __quitApplication(self): 
        self.__root.destroy() 
         
  
    def __showAbout(self): 
        showinfo("Notepad","Deepak Sinha") 
  
    def __openFile(self): 
          
        self.__file = askopenfilename(defaultextension=".txt", 
                                      filetypes=[("All Files","*.*"), 
                                        ("Text Documents","*.txt")]) 
  
        if self.__file == "": 
              
            # no file to open 
            self.__file = None
        else: 
              
             
            # set the window title 
            self.__root.title(os.path.basename(self.__file) + " - Deepak's Note") 
            self.__thisTextArea.delete(1.0,END) 
  
            file = open(self.__file,"r") 
  
            self.__thisTextArea.insert(1.0,file.read()) 
  
            file.close() 
  
          
    def __newFile(self): 
        self.__root.title("Untitled - Deepak's Note") 
        self.__file = None
        self.__thisTextArea.delete(1.0,END) 
  
    def __saveFile(self): 
  
        if self.__file == None: 
            # Save as new file 
            self.__file = asksaveasfilename(initialfile='Untitled.txt', 
                                            defaultextension=".txt", 
                                            filetypes=[("All Files","*.*"), 
                                                ("Text Documents","*.txt")]) 
  
            if self.__file == "": 
                self.__file = None
            else: 
                  
                # Try to save the file 
                file = open(self.__file,"w") 
                file.write(self.__thisTextArea.get(1.0,END)) 
                file.close() 
                  
                
                self.__root.title(os.path.basename(self.__file) + " - Deepak's Note") 
                  
              
        else: 
            file = open(self.__file,"w") 
            file.write(self.__thisTextArea.get(1.0,END)) 
            file.close() 
  
    def __cut(self): 
        self.__thisTextArea.event_generate("<<Cut>>") 
  
    def __copy(self): 
        self.__thisTextArea.event_generate("<<Copy>>") 
  
    def __paste(self): 
        self.__thisTextArea.event_generate("<<Paste>>") 
    def __centerAlign(self):
        self.__thisTextArea.tag_configure("center", justify='center')
        self.__thisTextArea.tag_add("center", 1.0, "end")
    def __leftAlign(self):
        self.__thisTextArea.tag_configure("left", justify='left')
        self.__thisTextArea.tag_add("left", 1.0, "end")

    def __rightAlign(self):
        self.__thisTextArea.tag_configure("right", justify='right')
        self.__thisTextArea.tag_add("right", 1.0, "end")

  
    def run(self): 
  
        # Run main  
        self.__root.mainloop() 
  
  
  
  
# main application 
notepad = Notepad(width=600,height=400) 
notepad.run() 
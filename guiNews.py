import spacy
import os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from Preprocessing.XParser_Module import XParser
from Preprocessing.Text_Preprocessing import TextPrep
from Spacy_NER import Spacy_NER_Model
from Nltk_summarization_nyt import Text_Summarizer
from Pke_keyphrase import PKE_KEA_Model
from spacy.util import set_data_path

"""
Script to initiaze the graphical user inteface and to call all functions from it

"""


def resource_path(relative_path):
    """
    Function to output path to resource depending on whether the program is run from from the command line or the stanalone bundle
    """
    try:
        # Assumes the it is run from the standalone bundle and attempts to find the temp folder
        base_path = sys._MEIPASS
    except Exception:
        # If the temp folder cant be found, then get path to current folder
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class guiProgram:
    """
    Class to encompass all the functions required by the grahical user interface

    Attributes
    ----------
    filename: String
        Path to nyt corpus file to process

    outputDirectory: String 
        Path to output directory

    nlpModel: A spacy nlp model

    nerModel: A class instance of Spacy_NER_Model from Spacy_NER.py

    Methods
    -------
    browseFiles()
        opens a dialog window for the user to select the nyt corpus file to process
    @returns: String
        a string of the path to nyt corpus file to process

    findOutputDirectory()
        opens a dialog window for the user to select the output directory
    @returns: String
        a string of the path to the output directory

    run()
        processes the file specified and outputs the summary, named entities and the keyphrases to the specified directory

    """
    def __init__(self):
        self.filename = ''
        self.outputDirectory = ''
        self.nlpModel = spacy.load(resource_path("en_core_web_md-2.3.1"), disable = ["tagger", "ner"])
        self.nerModel = Spacy_NER_Model()


    def browseFiles(self): 
        curr_directory = os.getcwd()
        self.filename = filedialog.askopenfilename(initialdir = curr_directory, 
                                              title = "Select a File", 
                                              filetypes = (("Xml Files", 
                                                            "*.xml"), 
                                                           ("all files", 
                                                            "*.*"))) 
           
        label_file_explorer.configure(text="File Opened: "+ self.filename)
        
    
    def findOutputDirectory(self): 
        curr_directory = os.getcwd()
        self.outputDirectory = filedialog.askdirectory (initialdir = curr_directory, 
                                              title = "Select a Directory") 
        label_folder_explorer.configure(text="Ouput directory: "+ self.outputDirectory)
           
    def run(self):
        # Checking if the file is a valid path, and that the user has selected a valid directory
        if self.filename == '' or os.path.splitext(self.filename)[1] != '.xml':
            noFileError = messagebox.showinfo("You have not selected a valid file")
            print(noFileError)
        elif self.outputDirectory == "":
            noFolderError = messagebox.showinfo("You have not selected an output folder")
            print(noFolderError)
        else:
            # Getting a string of the article from the xml file
            obj = XParser(self.filename)
            fullText = obj.getFullText()

            """
            Code to get the Keyphrases from the document using the module Pke_keyphrases and outputs the keyphrases to output_keyphrase.txt
            """
            pkeModel = PKE_KEA_Model()
            someKeyphrases = pkeModel.get_keyphrases(fullText)
            outputFileKeyPhrase = os.path.join(self.outputDirectory, "output_keyphrase.txt")
            with open(outputFileKeyPhrase,"w+") as f:
                f.write("=Keyphrases=\n")
                f.write("============\n")
                for keyphrase in  someKeyphrases:
                    f.write(str(keyphrase[0]))
                    f.write('\n\n')


            """
            Code to get the summary from the document using the module Pke_keyphrases and outputs the keyphrases to output_summary.txt
            """
            Text_Summarizer_Object = Text_Summarizer(obj,fullText)
            summary = Text_Summarizer_Object.get_Summary()
            outputFileSummary= os.path.join(self.outputDirectory, "output_summary.txt")
            with open(outputFileSummary,"w+") as f:
                f.write("=Summary=\n")
                f.write("=========\n\n")
                f.write(summary)

            """
            Code to get the Named entities from the document using the module Pke_keyphrases and outputs the keyphrases to output_NER.txt
            """
            prep = TextPrep(fullText, self.nlpModel)
            sentences = prep.sentencizer()
            namedEntities = self.nerModel.ouputSentenceEntities(sentences)
            catList = ['WHO', 'WHERE', 'WHEN']
            outputFileNER= os.path.join(self.outputDirectory, "output_NER.txt")
            with open(outputFileNER,"w+") as f:
                f.write("=Named Entities=\n================")
                for cat in catList:
                    f.write("\n\n--" + cat + "--\n\n")
                    for ent in namedEntities:
                        if ent[1] == cat:
                            f.write(ent[0])
                            f.write('\n')
            

"""
Creating the a gui object
"""
# initializing an instance of the class newGui above
newGui = guiProgram()

window = Tk()

# Title of window
window.title('NYT Natural Language Processing Toolkit') 
   
# Size of window
window.geometry("900x400") 

# Background colour
window.config(background = "white") 


"""
Code to pupulate the main window
"""
# Creating widgets
# Label to display the instructions and the location of the file selected
label_file_explorer = Label(window,  
                            text = "Select NYT Corpus file to process", 
                            width = 100, height = 4,  
                            fg = "blue") 

# Label to display the instructions and the location of the directory selected
label_folder_explorer = Label(window,  
                            text = "Select Output Directory", 
                            width = 100, height = 4,  
                            fg = "blue") 

# Button to call the function to locate the file to process and
button_explore = Button(window,  
                        text = "Browse Files", 
                        command = lambda: newGui.browseFiles()) 

# Button to call the function to locate the directory to save the output files to 
button_find_ouput_directory = Button(window,
                                    text = "Select Output Directory",
                                    command= lambda: newGui.findOutputDirectory())

# Button to call the function to process the article
button_run = Button(window,  
                     text = "Process File", 
                     command = lambda: newGui.run())
  

# Adding widgets to main window
label_file_explorer.grid(column = 1, 
                        row = 1) 
   
button_explore.grid(column = 1, 
                    row = 2) 

label_folder_explorer.grid(column = 1, 
                            row = 3)

button_find_ouput_directory.grid(column = 1, 
                                row = 4)

button_run.grid(column = 1, 
                row = 6, 
                pady=40, 
                ipadx= 30, 
                ipady=10)


""" 
Code for menubar 
"""
# Creating and populating the dropdown menubar object 
# Creating the menu object
menubar = Menu(window)

filemenu = Menu(menubar, 
                tearoff=0)

# Adding a menu item to locate the file
filemenu.add_command(label="Open", 
                    command=lambda: newGui.browseFiles())

# Adding a menu item to locate the output directory
filemenu.add_command(label="Output Directory", 
                    command=lambda: newGui.findOutputDirectory())

filemenu.add_separator()

# Adding a menu item to exit the program
filemenu.add_command(label="Exit", 
                    command=window.destroy)

# Populating the menubar
menubar.add_cascade(label="File", 
                    menu=filemenu)


# Adding the menubar to the window
window.config(menu=menubar)



# Code to start the Graphical User interface
window.mainloop()



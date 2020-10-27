"""
    @project: Keyword Extraction and Summarization of Newspaper Articles
    @program: File Filter and Copy.py
    @author: Bombompow
    @last updated: 28/7/2020

    A program to perform the following:
    - Parse tgz files and create corresponding directories.
    - Filter news articles that contains an tags predetermined by the user
    - Copy the filtered documents into respective directories.
"""

import os
import tarfile
import re
import xml.etree.ElementTree as ET
import sys
"""
    @function: Filter_Copy
    @param: directory - The main directory which stores the tgz files
    @precond: Valid directory path for Windows.
"""
def Filter_Copy(directory, searchList):
    os.chdir(directory)

    for (dirpath, dirnames, filenames) in os.walk(directory):
       
        # Create necessary path 
        year = dirpath[-4:]
        if year != "data":
            currentDirectory = "D:\Corpus Dataset\withAbstract"+ "\\" + str(year)
            os.mkdir(currentDirectory)
            f = []
            for afile in filenames:
                tempPath = str(dirpath + "\\" + afile)
                f.append(tempPath)
            allfiles = []

            # Extract tgz archives
            for theFile in f:     
                targz = tarfile.open(theFile, "r:gz")
                tar = targz.getmembers()

                # Create directories 
                for subTarFile in tar:
                    if len(subTarFile.name) == 2:
                        os.mkdir(currentDirectory + '\\' + subTarFile.name)
                    elif len(subTarFile.name) == 5:
                        os.mkdir(currentDirectory + '\\' + subTarFile.name[:2] + '\\' + subTarFile.name[-2:])
                        intermediateDirectory = (currentDirectory + '\\' + subTarFile.name[:2] + '\\' + subTarFile.name[-2:])
                    else:   # Filter files with abstract
                        extract = targz.extractfile(subTarFile)
                        fileName = subTarFile.name[-11:]
                        xmlFile = extract.read()
                        root = ET.fromstring(xmlFile)

                        # Copy filtered files into appropriate directories
                        for elem in root.iter():
                            for item in searchList:
                                if elem.tag == item
                                    with open(intermediateDirectory + '\\'+ fileName, 'wb') as writeFile:
                                        writeFile.write(ET.tostring(root))
                                    break
                        
                targz.close()

def processArgs():
    """
    Return the list of arguments provided as a list of tags to search for
    """
    searchList = []
    for i in range(1, len(inputArgs)):
        searchList.append(i)
    return searchList




if __name__ == "__main__":
    # Get arguments
    searchList = processArgs()
    # Run the program to filter the nyt corpus for articles with predetermined tags
    Filter_Copy(r'D:\Corpus Dataset\nyt_corpus_LDC2008T19\nyt_corpus\data', searchList)

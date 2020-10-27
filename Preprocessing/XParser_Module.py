"""
    @project: Keyword Extraction and Summarization of Newspaper Articles
    @program: XML_Parser_Module.py
    @author: Bombompow
    @last updated: 24/8/2020
"""
import xml.etree.ElementTree as ET


class XParser:
    """
    Attributes
    ----------
    file : an XML file
        The XML file to be parsed.
    
    Methods
    -------
    getTitle()
        returns a string of the title

    getIndexDesc()
        Returns a set of strings of hand-annotated descriptor data

    getOnlineDesc()
        Returns a set of strings of algorithmically-annotated descriptor data

    getIndexPerson()
        Returns a set of strings of hand-annotated person data (who)

    getOnlinePerson()
        Returns a set of strings of algorithmically-annotated person data (who)

    getIndexOrg()
        Returns a set of strings of hand-annotated organization data (who)

    getOnlineOrg()
        Returns a set of strings of algorithmically-annotated organization data (who)

    getIndexLoc()
        Returns a set of strings of hand-annotated location data (where)

    getOnlineLoc()
        Returns a set of strings of algorithmically-annotated location data (where)

    getFullText()
        Returns a string of the full body text

    getAbstract()
        Returns a string of the abstract

    Example
    -------
    To create XParser object:
    parser = XParser("file.xml")

    Getting required data from XParser object:
    fullBodyText = parser.getFullText()
    
    """

    def __init__(self, file):
        """
        Parameters
        ----------
        file : and XML file
            The XML file to be parsed
        """
        self.tree = ET.parse(file)
        self.root = self.tree.getroot()
        self.classifierPath = self.root.findall(".//classifier")
        self.personPath = self.root.findall(".//person")
        self.orgPath = self.root.findall(".//org")
        self.locPath = self.root.findall(".//location")
        
    def getTitle(self):
       return self.root.findall(".//title")[0].text

    def getIndexDesc(self):
        indexDesc = set()
        for classifier in self.classifierPath:
            if classifier.attrib['class'] == "indexing_service" and classifier.attrib['type'] == "descriptor":
                for word in classifier.text.split():
                    indexDesc.add(word)
        
        return indexDesc
    
    def getOnlineDesc(self):
        onlineDesc = set()
        for classifier in self.classifierPath:
            if classifier.attrib['class'] == "online_producer":
                if classifier.attrib['type'] == ("descriptor" or "general_descriptor"):
                    for word in classifier.text.split():
                        onlineDesc.add(word)
        
        return onlineDesc
    

    def getIndexPerson(self):
        indexPerson = set()
        for person in self.personPath:
            if person.attrib['class'] == "indexing_service":
                indexPerson.add(person.text)
        
        return indexPerson
    
    def getOnlinePerson(self):
        onlinePerson = set()
        for person in self.personPath:
            if person.attrib['class'] == "online_producer":
                onlinePerson.add(person.text)
    
    def getIndexOrg(self):
        indexOrg = set()
        for org in self.orgPath:
            if org.attrib['class'] == "indexing_service":
                indexOrg.add(org.text)
        
        return indexOrg
    
    def getOnlineOrg(self):
        onlineOrg = set()
        for org in self.orgPath:
            if org.attrib['class'] == "online_producer":
                onlineOrg.add(org.text)
        
        return onlineOrg

    def getIndexLoc(self):
        indexLoc = set()
        for loc in self.locPath:
            if loc.attrib['class'] == "indexing_service":
                indexLoc.add(loc.text)
        
        return indexLoc
    
    def getOnlineLoc(self):
        onlineLoc = set()
        for loc in self.locPath:
            if loc.attrib['class'] == "online_producer":
                onlineLoc.add(loc.text)
        
        return onlineLoc

    def getFullText(self):
        paraTextArr = []
        fullTextPath = self.root.findall(".//block[@class='full_text']")[0].getchildren()
        for para in fullTextPath:
            paraTextArr.append(para.text)
        
        fullTextStr = " ".join(paraTextArr).replace("''", "'")
        return fullTextStr
    
    def getAbstract(self):
        abstractArr = []
        abstractPath = self.root.findall(".//abstract")[0].getchildren()
        for p in abstractPath:
            abstractArr.append(p.text)
        
        abstractStr = " ".join(abstractArr).replace("''", "'")
        return abstractStr
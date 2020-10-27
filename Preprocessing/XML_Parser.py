"""
	@project: Keyword Extraction and Summarization of Newspaper Articles
    @program: XML_Parser.py
    @author: Bombompow
    @last updated: 22/8/2020
"""
import xml.etree.ElementTree as ET

"""
	@function: parser
	@args: file - The XML file to be processed, only accepts .xml files.
	@precond: input file is one .xml file from NYT Corpus.
	@return: None
"""
def parser(file):
	tree = ET.parse(file)
	root = tree.getroot()
	
	title = root.findall(".//title")[0].text	# title of news article; string object.
	print (title)

	# Collect respective descriptor classifiers
	indexDescArr = []	# list of text from manual classifierging
	onlineDescArr = []	# list of text from algorithmically assigned classifiers
	onlineGenDescArr = []	# list of text from algorithmically assigned classifiers with higher generality
	for classifier in root.findall(".//classifier"):
		if classifier.attrib['class'] == "indexing_service":	# indexing_service, hand-annotated
			if classifier.attrib['type'] == "descriptor":
				indexDescArr.append(classifier.text)
		
		else: 	# online_producer, algorithmically annotated
			if classifier.attrib['type'] == "descriptor":
				onlineDescArr.append(classifier.text)
			elif classifier.attrib['type'] == "general_descriptor":
				onlineGenDescArr.append(classifier.text)
	
	print(indexDescArr, "\n", onlineDescArr, "\n", onlineGenDescArr)

	#Extract organization names (who)
	indexPerson = []	# hand-annotated, contains name of author, which is not in full-text
	onlinePerson = []	# algorithmically-annotated
	for person in root.findall(".//person"):
		if person.attrib['class'] == "indexing_service":
			indexPerson.append(person.text)
		else:
			onlinePerson.append(person.text)
	
	print(onlinePerson, "\n", indexPerson)

	# Extract organization names (who)
	indexOrg = []
	onlineOrg = []
	for org in root.findall(".//org"):
		if person.attrib['class'] == "indexing_service":
			indexOrg.append(org.text)
		else:
			onlineOrg.append(org.text)
	print(onlineOrg, "\n", indexOrg)

	# Extract location (where)
	indexLoc = []
	onlineLoc = []
	for loc in root.findall(".//location"):
		if loc.attrib['class]'] == "indexing_service":
			indexLoc.append(loc.text)
		else:
			onlineLoc.append(loc.text)
	
	print (onlineLoc, "\n", indexLoc)

	# Extract full body text
	paraFullText = []	# list of paragraphs in the full text
	full_text =  root.findall(".//block[@class='full_text']")[0].getchildren()
	for para in full_text:
		#print(para.text)
		paraFullText.append(para.text)

	for i in paraFullText: print(i)	#print

	# Extract abstract text
	abstractArr = []
	abstract = root.findall(".//abstract")[0].getchildren()
	for p in abstract:
		abstractArr.append(p.text)
		
	for j in abstractArr: print(j)


import spacy
import time
import os
"""
Module that contains a class that returns the named entities from an article

Relevant Entity Categories:

PERSON:         People, including fictional.

NORP:           Nationalities or religious or political groups.

FAC:            Buildings, airports, highways, bridges, etc.

ORG:            Companies, agencies, institutions, etc.

GPE:            Countries, cities, states.

LOC:            Non-GPE locations, mountain ranges, bodies of water.

DATE:           Absolute or relative dates or periods.

TIME:           Times smaller than a day.


Aggregated into the following labels:

PERSON, ORG, NORP -> WHO

LOC, GPE, FAC -> WHERE

DATE, TIME -> WHEN
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

class Spacy_NER_Model:
    
    def __init__(self, model = None):
        # Load default model, pretrained cnn model for english entities
        # More info on the pretrained model with in the report
        if model == None:
            self.nerModel = spacy.load(resource_path("en_core_web_md-2.3.1"), disable = ["tagger", "parser"])    # only want ner in pipeline
            # self.nerModel = spacy.load(modelPath, disable = ["tagger", "ner"])

            # self.nerModel = spacy.load("en_core_web_md-2.3.1", disable = ["tagger", "parser"])    # only want ner in pipeline


        else:
            self.nerModel = spacy.load(model)   # load custom model
        self.ent = None

    def ouputSentenceEntities(self, sentences):
        """
        Process sentences and tag each entity according to the loaded model.

        Parameter
        ----------
        sentences: a list of strings, where each element is a sentence.

        Return
        ------
        An array of tuples, where each tuple is (text, label).
        Each tuple is a size of 2, with (string, string) data types.
        """
        entArr = []
        # identifying entities from each sentence is faster and more accurate
        for entDoc in self.nerModel.pipe(sentences):    # process sentences as streams
            if len(entDoc.ents) > 0:
                for ent in entDoc.ents:
                    label = None
                    # Aggregate the relevant tags into WHO, WHERE, WHEN
                    if ent.label_ in ("PERSON", "ORG", "NORP"):
                        label = "WHO"
                    elif ent.label_ in ("LOC", "GPE", "FAC"):
                        label = "WHERE"
                    elif ent.label_ in ("DATE", "TIME"):
                        label = "WHEN"

                    if label != None:
                        entArr.append((ent.text, label))   # get the entities as (text, category) tuple
        self.ent = entArr
        return entArr

    def get_NamedEntities():
        return self.ent
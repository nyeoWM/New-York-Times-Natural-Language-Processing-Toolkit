import pke
from nltk.corpus import stopwords
import os
from spacy.util import set_data_path



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

class PKE_KEA_Model:
    """

    Attributes
    ----------
    model_file : an Kea model file
    stoplist: a list of stopwords
    
    Methods
    -------
    get_keyphrases()
    gets list of keyphrases from article
        @ input: String
        @ returns: list of String


    Example
    -------
    To get keyphrases from a article saved in variable fulltext:
    pkeModel = PKE_KEA_Model()
    keyphrases = pkeModel.get_keyphrases(fullText)

    """
    def __init__(self, model = None):
        if model == None:
            self.model_file = "Kea-semeval2010.py3.pickle"
        else:
            self.model_file = model
        self.stoplist = stopwords.words('english')

    def get_keyphrases(self, fullText):
        extractor = pke.supervised.Kea()
        extractor.load_document(input=fullText, language='en', normalization = None)
        extractor.candidate_selection(stoplist=self.stoplist)
        extractor.candidate_weighting(model_file = self.model_file)
        keyphrases = extractor.get_n_best(n=5)
        return keyphrases


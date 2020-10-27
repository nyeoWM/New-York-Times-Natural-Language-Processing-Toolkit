import spacy
from Preprocessing.XParser_Module import XParser

class TextPrep:
    """
    A Class used to preprocess text or string objects using spacy's pre-trained model.

    Attributes
    ---------
    text: str
        The text to be processed.
    
    cleanText: str
        The cleaned text after processed by the text cleaning pipeline
    
    stopwords: set of strings
        The default spacy reference for stopwords

    Methods
    ------- 
    """
    def __init__(self, text, nlpModel):
        self.text = text
        self.cleanWords = None
        self.nlpModel = nlpModel
    
    ###     Main Cleaning Pipeline     ###
    def default_clean(self):
        """
        Cleans the original text with the text cleaning pipeline.
        This function performs the following in order:
        1. Punctuation removal
        2. Stopword removal
        3. Lowercasing
        
        Return:
        self.cleanWords : array of strings
            The cleaned text delimitted by words
        """
        doc = self.apply_model()
        no_punct = self.remove_punct(doc)
        no_stop = self.remove_stopword(no_punct)
        self.cleanWords = self.lower(no_stop)
        return self.cleanWords
  
    def remove_stopword(self, doc):
        """
        Removes stopword tokens based on the model's default stopword dictionary

        Parameter
        ---------
        doc : A list of tokens
        
        Return
        ------
        A list of tokens with stopwords removed
        """
        return [token for token in doc if token.is_stop == False ]

    def remove_punct(self,doc):
        """
        Removes stopword tokens based on the model's default punctuation dictionary

        Parameter
        ---------
        doc : A list of tokens
        
        Return
        ------
        A list of tokens with punctuations removed
        """
        return [token for token in doc if token.is_punct == False]

    def lower(self, doc):
        """
        Converts all tokens into lowercase

        Parameter
        ---------
        doc : A list of tokens

        Return
        ------
        A list of strings that has been converted into lowercase
        """
        return [token.lower_ for token in doc]


    def apply_model(self):
        return self.nlpModel(self.text)

    def custom_sentencizer(self, doc):
        """
        Customizes spacy's default sentencizer to indicate positions where the sentence segmentation should occur.

        Parameters
        ----------
        doc : spacy doc object
            the doc object passed from training the model from text

        Return
        ------
        doc: spacy doc object
            the altered doc object with the current sentence segmentation customizations.

        """

        for i, token in enumerate(doc[:-2]):
            # prevents breaking a token with a comma, colon, semi-colon or starts with lowercase character.
            if token.text in (",",";",":") or token.is_lower:
                doc[i].is_sent_start = False
            # prevents breaking after the start of a quotation
            elif i > 0 and token.text[0].isupper() and token.nbor(-1).text == "'":
                doc[i].is_sent_start = False
            # breaks quotation mark after a full stop followed by space, but don't break after quotation
            elif token.text == "'" and (token.nbor(-1).text == ("." or "'")) and token.nbor(-1).whitespace_:
                doc[i].is_sent_start = True
                doc[i + 1].is_sent_start = False
            
        return doc


    def sentencizer(self):
        """
        Utilize the custom sentencizer for sentence segmentation.

        Return
        ------
        sentences: array of strings
            An array containing the segmented sentences.

        """
        self.nlpModel.add_pipe(self.custom_sentencizer, before="parser")    #apply custom sentencizer before dependency parser
        doc = self.apply_model()
        sentences = [sentence.text for sentence in doc.sents]
        self.nlpModel.remove_pipe("custom_sentencizer")
        return sentences



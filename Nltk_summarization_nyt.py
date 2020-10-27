import nltk
from string import punctuation
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

"""
Module that contains a class that returns the named entities from an article
"""


punctuation = punctuation + '\n'

class Text_Summarizer:
    """
    Attributes
    ----------
    reference : abstracts of the article 

    summary: summary

    Methods
    -------
    get_Summary()
        Return summary


    Example
    -------
    To get summary:
    Text_Summarizer_Object = Text_Summarizer(obj,fullText)
    summary = Text_Summarizer_Object.get_Summary() 
    
    """

    def __init__(self, obj, inputText = None):
        text = inputText.strip().replace("\n"," ")
        tokens = word_tokenize(text)
        stop_words = stopwords.words('english')
        
        article_content = ''
        #Finding weighted frequency of Occurrence
        for p in text:
            article_content += p

        word_frequencies = {}
        for word in tokens:
            if word.lower() not in stop_words:
                if word.lower() not in punctuation:
                    if word not in word_frequencies.keys():
                        word_frequencies[word] = 1
                    else:
                        word_frequencies[word] += 1


        max_frequency = max(word_frequencies.values())
        for word in word_frequencies.keys():
            word_frequencies[word] = word_frequencies[word]/max_frequency


        # Calculating Sentence Scores
        sent_token = sent_tokenize(article_content)

        sentence_scores = {}
        for sent in sent_token:
            sentence = sent.split(" ")
            for word in sentence:
                if word.lower() in word_frequencies.keys():
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word.lower()]
                    else:
                        sentence_scores[sent] += word_frequencies[word.lower()]

        from heapq import nlargest


        reference  = obj.getAbstract().strip().replace("\n"," ")
        self.reference = reference
        summary = nlargest(4, sentence_scores, key = sentence_scores.get)
        final_summary = [word for word in summary]
        self.summary = ' '.join(final_summary)

    def get_Summary(self):
        return self.summary



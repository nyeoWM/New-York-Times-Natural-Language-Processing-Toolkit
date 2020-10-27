#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from Pke_keyphrase import PKE_KEA_Model
from Preprocessing.XParser_Module import XParser

testPath = os.path.join('tests', 'data', '1815742.xml')

class test_PKE_KEA_Model:
    def __init__(self, testPath):
        self.obj = XParser(testPath)
        self.fullText = self.obj.getFullText()
        self.pkeModel = PKE_KEA_Model()

    def test_get_keyphrases(self):
        self.actualKeyphrases = [('smilebox', 0.04721038011946404), ('online', 0.019741538672329157), ('users', 0.016916023220632924), ('photo', 0.01632993581652423), ('company', 0.015016062009211)]
        keyphrases = self.pkeModel.get_keyphrases(self.fullText)
        assert keyphrases == self.actualKeyphrases.append()

if __name__ == '__main__':
    test1 = test_PKE_KEA_Model(testPath)
    test1.test_get_keyphrases()
    print("Test Pke_keyphrase passed!")


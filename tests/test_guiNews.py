import os
import sys
import filecmp
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)


class test_guiNews:
    def __init__(self):
        # Preparing the list of paths of the output files
        self.outputFileNames = ['output_keyphrase.txt', 'output_NER.txt', 'output_summary.txt']
        self.sampleFilePaths = [os.path.join('tests', 'data', "sample_" + i) for i in self.outputFileNames]

    def test_Output(self):
        for i in range(3):
            # Checking if file exist
            if os.path.exists(filename):
                # Checking if the output files match the pre-verifies output files
                assert filecmp.cmp(self.outputFileNames[i], self.sampleFilePaths[i]) == True
            else:
                print("File " + filename + " does not exist")
            


if __name__ == "__main__":
    test1 = test_guiNews()
    test1.test_Output()
    # Removes test files from root directory
    for filename in test1.outputFileNames:
        if os.path.exists(filename):
            os.remove(filename)
        else:
            print("File " + filename + " does not exist")
    print("Gui Output Test Passed!")

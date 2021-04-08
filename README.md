# New-York-Times-Natural-Language-Processing-Toolkit
A standalone application that performs Keyword Extraction using KEA, Named Entity Recognition using Convolutional Neural Networks and
Summarization of News Articles using TextRank

Further Documentation can be found in docs.


## Installation Instructions

### Obtaining the files and dependencies

1. File can be obtained by cloning from github

```
git clone https://github.com/nyeoWM/New-York-Times-Natural-Language-Processing-Toolkit.git
```

2. Note: we use Pipenv to manage our dependencies. If you do not have Pipenv installed, install through pip by running the following command in terminal (Mac Os, Linux) or Powershell (Windows). Pip installation instructions can be found here: Installing Packages

```
pip install pipenv
```

3. Our Graphical user interface requires a python3 version installed with tkinter. If you are unsure if your python3 supports tkinter, the easiest way is to install tkinter using binaries from https://www.python.org/. You can test if tkinter is properly installed by running
python3

Activate your python interpreter, then run the following command:

```
import tkinter
```

If it proceeds without error messages, you are good to go.

4. Once you have Pipenv installed, you can install the dependencies directly from the pipfile using:
   
```
pipenv install
```
### Running the program
5. Activate the environment using 

```
pipenv shell
```

6. Run the guiUsing:

```
python3 guiNews.py
```

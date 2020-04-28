% Bert Extractive Summarizer Example
% Paige Phillips - March 2020 
% Before running this code, dependencies must be installed. 
% Follow the instructions at https://pypi.org/project/bert-extractive-summarizer/ inside a virtual environment
% Place this file in the same directory as the transformers library and with txt file you are summarizing.
% Replace FILENAME.txt with the name of the file you are summarizing
% To execture the code: $python BertExtractiveSummarizerExample.py

from summarizer import Summarizer

f = open("FILENAME.txt", "r")

body = f.read()

model = Summarizer()
result = model(body, min_length=60)
full = ''.join(result)
print(full)

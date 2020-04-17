from langdetect import detect

text = "This is a test of the detection model"
print(text)
language = detect(text)
print("The language: " +language+"\n")

text = "Ceci est un test du modèle de détection"
print(text)
language = detect(text)
print("The language: " +language)

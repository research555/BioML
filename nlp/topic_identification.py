import spacy
import scispacy
import en_core_sci_lg

# Load the spacy model
nlp = en_core_sci_lg.load()

path = r"C:\Users\imran\PycharmProjects\BioDataScience\publication_txts"

with open(rf'{path}/pub3.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Process the text with spacy
doc = nlp(text)

sentences = list(doc.sents)
for sentence in sentences:
    print(sentence.ents)
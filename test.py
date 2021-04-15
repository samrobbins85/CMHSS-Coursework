import stanza
import json
stanza.download('en') # download English model
nlp = stanza.Pipeline('en') # initialize English neural pipeline
doc = nlp("2 eastern towers and fragments of curtain wall; dates given as C12 (Pevsner and Williamson); late C13 (Boyle); 1290 (Longstaff). C14 plan of 4 towers and curtain wall forming square enclosure with no keep; (compare Ford 1338, Chillingham 1344, Raby 1378) Coursed squared sandstone with ashlar dressings. 3 storeys. Southern tower has elliptical-headed entrance in the north face, 4 lancet windows in west ground floor of late C13 type. North tower has mullioned and transomed window in first floor north face. Historical note: Ravensworth Castle was the property of the Fitz-Marmadukes; then in C14 and C15 of the Lumleys; then of the Gascoignes, from whom Thomas Liddell, a Newcastle merchant, bought it in 1607. It remained in the Liddell family until 1976. Sir Thomas Liddell, later Lord Ravensworth, demolished all but these towers of the house then standing. A scheduled ancient monument.") # run annotation over a sentence
# out = [x for x in doc.to_dict()]
# print (json.dumps(out, indent=2))

for sentence in doc.sentences:
    for word in sentence.words:
        if word.xpos == "NN" or word.xpos == "NNS":
            print(word.text)

# print(doc)
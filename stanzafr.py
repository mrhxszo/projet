import stanza

nlp = stanza.Pipeline('fr')

def lemma(phrase):
    """takes in a word and returns the 'standard'(verbs to infinitif, plurals to singulars etc) form using stanza"""
    doc = nlp(phrase)
    lemme = doc.sentences[0].words[0].lemma
    return lemme



def load_corpus () :
    corpus = []
    input_file = open ('develop.csv')
    for line in input_file :
        (ident, emot, tweet) = line.split(",")
        corpus = corpus + [[ident, emot, tweet]]
    return corpus

corpus = load_corpus ()

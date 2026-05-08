

def load_corpus () :
    corpus = []
    input_file = open ('develop.csv')
    for line in input_file :
        (ident, emot, tweet) = line.split(",")
        clean_tweet = tweet.lower().rstrip().lstrip().strip(',.!;#*&@)(')
        corpus = corpus + [[ident, emot, clean_tweet]]
    return corpus

corpus = load_corpus ()

    
    

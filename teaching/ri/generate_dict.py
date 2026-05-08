

def load_corpus () :
    corpus = []
    input_file = open ('develop.csv')
    for line in input_file :
        (ident, emot, tweet) = line.split(",")
        clean_tweet = tweet.lower().rstrip().lstrip().strip(',.!;#*&@)(')
        corpus = corpus + [[ident, emot, clean_tweet]]
    return corpus

corpus = load_corpus ()


def create_dictionary (corpus):
    total_pos =0
    total_neg = 0
    total_both = 0
    
    word_freq = {}
    for item in corpus:
        for word in item[2].split() :
            word_freq[word] =[0,0,0]
            
    for item in corpus:
        for word in item[2].split() :
            [pos, neg, both] = word_freq[word]
            if item[1] == '1':
                pos = pos + 1
                total_pos = total_pos + 1
            elif item [1] == '0':
                neg = neg + 1
                total_neg = total_neg + 1
            both = both + 1
            total_both = total_both + 1
            word_freq[word] = [pos, neg, both]
            word_freq['totals!'] = [total_pos,total_neg,total_both]
    return word_freq

word_dictionary = create_dictionary (corpus)

    
    

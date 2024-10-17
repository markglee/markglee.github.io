

def load_corpus () :
    print ("loading corpus")
    corpus = []
    input_file = open ('training.csv')
    for line in input_file :
        (ident, emot, tweet) = line.split(",")
        clean_tweet = tweet.lower().rstrip().lstrip().strip(',.!;#*&@)(')
        corpus = corpus + [[ident, emot, clean_tweet]]
    return corpus

corpus = load_corpus ()


def create_dictionary (corpus):
    print ("creating dictionary")
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


    
def classify_tweet(tweet, word_dictionary) :
    clean_tweet = tweet.lower().rstrip().lstrip().strip(',.!;#*&@)(').split()
    total_pos = 1
    total_neg = 1
    for word in clean_tweet :
        if word in word_dictionary :
            [pos, neg, total] = word_dictionary[word]
            total_pos = total_pos * pos
            total_neg = total_neg * neg

    [p_pos, p_neg, total_both] = word_dictionary['totals!']
    total_pos = total_pos * (p_pos/total_both)
    total_neg = total_neg * (p_neg/total_both)

    if total_pos > total_neg : return 1
    else : return 0


#print(classify_tweet('i am happy', word_dictionary))

def evaluate (word_dictionary) :
    print ("evaluating classifier")
    count = 0
    correct = 0
    input_file = open ('test.csv')
    for line in input_file :
        (ident, emot, tweet) = line.split(",")
        guess = classify_tweet(tweet, word_dictionary)
        if guess == int(emot) : correct = correct + 1
        count = count + 1
    score = round(correct / count * 100)
    print ("classifer is " + str(score) + "% correct")
    
evaluate (word_dictionary)


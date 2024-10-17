def evaluate (word_dictionary) :
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

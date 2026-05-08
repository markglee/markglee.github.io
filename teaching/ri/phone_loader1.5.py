
def load_phonebook () :

    phonebook_file = open ('phone_book.txt')

    phonebook = {}

    for letter in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
        phonebook[letter] = []

    
    for line in phonebook_file:
        (name, number) = line.lower().rstrip().split(" : ")
        (first, second) = name.split(" ")        
        phonebook[second[0]] = phonebook[second[0]] + [name, number]

        


    phonebook_file.close()
    return phonebook
    
tele = load_phonebook ()

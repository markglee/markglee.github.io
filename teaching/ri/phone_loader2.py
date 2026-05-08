
def load_phonebook () :

    phonebook_file = open ('phone_book.txt')

    phonebook = {}

    
    for line in phonebook_file:
        (name, number) = line.rstrip().split(" : ")

        (first, second) = name.split(" ")

        if second[0] in phonebook :
            phonebook[second[0]] = phonebook[second[0]] + [name, number]
        else :  phonebook[second[0]] = [[name, number]]
        


    phonebook_file.close()
    return phonebook
    
tele = load_phonebook ()

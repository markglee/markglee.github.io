
def load_phonebook () :

    phonebook_file = open ('phone_book.txt')

    phonebook = {}

    count = 0
    
    for line in phonebook_file:
        (name, number) = line.split(" : ")
        phonebook[name] = number.rstrip()

    phonebook_file.close()
    return phonebook
    
tele = load_phonebook ()

Input = input("Enter 'yes' for options or 'no' for exit: ").lower()
Options = [ 'press 1 for add', 'press 2 for search', 'press 3 for Display', ' Press 4 for Updates', 'Press 5 for Delete']

Words_dict = {}
Add = []
Search =[]
Display = []
Updates = []
Delete = []

#conditions
# Main program loop
while True:
    if Input == 'yes':
        print(Options)

        number = input("Enter your number (1-5): ")

        if number == '1':
            word = input("Enter the word: ")
            meaning = input("Enter the meaning of the word ")
            Words_dict[word] = meaning
            print(f"The word {word} meaning is {meaning}")

        elif number== '2':
            search = input("Enter the word: ")
            for word in Words_dict:
                if search == word:
                    print(f" meaning of the {word} is {Words_dict[word]}")
                else:
                    print(f"Word is not in dictionary")
                Search.append(search)
                print(Search)

        elif number == '3':
            for word, meaning in Words_dict.items():
                print(f"{word}: {meaning}")       

        elif number== '4':
            word = input("Enter the word: ")
            if word in Words_dict:
                new_meaning = input("Enter the new meaning: ")
                Words_dict.update({word: new_meaning})
                Updates.append({word: new_meaning})
                print(f"Meaning of '{word}' is {new_meaning} updated successfully!")
            else: 
                print(f"'{word}' not found in the dictionary.")
                
        elif number == '5':
            # Delete word 
            word = input("Enter the word: ")
            if word in Words_dict:
                Words_dict.clear(word)
                print(Words_dict)
            else: 
                print(f"'{word}' not found in the dictionary.")
                
        else:
            print("Invalid number! Please enter a number between 1 and 5.")
    else:
        print("Enter yes for Options")
'''
Program: Language Translater Dictonary
Filename: languageTranslationDictonary-tRaj-00.py
Author: Tushar Raj
Description: Translating from one language to another
Revisions: No revisions made
'''

#There is no import statement
mydict = {'red' : {'french':'rouge','spanish':'rojo','hindi':'laal'},'blue':{'french':'bleu','spanish':'azul','hindi':'nila'}}
#There are no class defined

def inputdata(number): #checks the user input is correct
    '''
    This function accepts the input from the user and checks if the value contains any special character,digits.
    Input: user input from the console which is string type
    output: returns strings data type
    '''
    special = "!@#$%^&*()+?_=,<>/"
    while True:
        if(number.isdigit() == True): #checks if the value entered in number variable is having any character or not
            print("****Entered value can not be a digit****\n") #prints the error message
            progress = input("Please enter if you want to continue with Language Translater(y/n): ") #ask users if he wants to continue with program
            if( progress.lower() == 'y'):#checks the response of the user if its yes, asks to enter the diameter again
                number = input("\nEnter the last input again: ")
            if( progress.lower() == 'n'):#exits the program if response in no
                print("Exiting...")
                exit()
            continue
        elif (any( i in special for i in number)): #picks up each character from the number variable and then checks in special variable if it is present, if present run this elif
            print("****Input cant have special character. Please Enter the valid entry****\n")
            progress = input("Please enter if you want to continue with Language Translater(y/n): ")
            if( progress.lower() == 'y'):
                number = input("\nEnter the last input again: ")
            if( progress.lower() == 'n'):
                print("Exiting...")
                exit()
            continue
        else:
            return number

print("Language Translater using Dictonary") # printing the opening line
while True: #Starting the while loop
    print("\nAvailable  English words are: ",end="")
    for key in mydict:
        print(key, end=" ") #print the available word translation we can find
    userInput=input("\nPlease Enter a word in English: ") #accepting the input from user for the word which need to be converted
    if(userInput == ""): #exit when no value was entered by user
        print("Exiting...")
        quit()
    userInput_check = inputdata(userInput) #calling the function to check valid input was provided or not
    userInput_lower = userInput_check.lower() #converting the checked data to lower format as to preserve user input format
    print("Available Language translations are: ",end="")
    n=[] #to add the newly added language in list and display
    for key,value in mydict.items():
        [n.append(id) for id in value]
    n=set(n) #remove duplicate occurance  of language
    [print(i,end=" ") for i in n]
    lang=input("\nPlease enter a language from the list: ").lower() #display all the language
    transLaguage=inputdata(lang)
    if(userInput_lower in mydict): #checking if the word is added in the dictonary or not
        print(f"The word '{userInput_lower}' in {transLaguage} is {mydict.get(userInput_lower).get(transLaguage)!r}")
    try:
        if(mydict.get(userInput_lower).get(transLaguage) == None): #check if the word for that language was added in the dictonary or it was left empty
            decision=input(f"Looks like {transLaguage} translation of word '{userInput_lower}' is not avialable would you like to add(y/n):").lower() #ask user if he wants to add the word which was left empty
            if(decision == 'y'):
                word = input(f"\n Enter the {transLaguage} word for '{userInput_lower}' : ").lower()
                mydict[userInput_lower].update({transLaguage:word}) #update the word in dictonary for which meaning was left empty
            else:
                continue
    except AttributeError: 
        if(userInput_lower not in mydict):
            mydict[userInput_lower] = {}
            french_word = input(f"\n Enter the french word for '{userInput_lower}' : ").lower() #accept the french word from user
            french_word_checked=inputdata(french_word) #check the proper french word was entered
            mydict[userInput_lower].update({'french': french_word_checked}) #add the frech word to the dictonary
            spanish_word = input(f"\n Enter the Spanish word for '{userInput_lower}' : ").lower() #accept the Spanish word from user
            spanish_word_checked=inputdata(spanish_word) #check the proper french word was entered
            mydict[userInput_lower].update({'spanish': spanish_word_checked}) #add the frech word to the dictonary
            hindi_word = input(f"\n Enter the hindi word for '{userInput_lower}' : ").lower() #accept the hindi word from user
            hindi_word_checked=inputdata(hindi_word) #check the proper hindi word was entered
            mydict[userInput_lower].update({'hindi': hindi_word_checked}) #add the hindi word to the dictonary
    else: #if it is not in the list perform below statements
        continue

# Hangman-game
Data structure hangman game proyect

#Access to different menus

def mainmenu():
    selected = int((input('Select one of the three options:\n1.Modyfy words\n2.Play\n3.Exit\n Your choice:')))
    while (selected <=0) and (selected>3):
        print('Wrong selection')
        selected=int((input('Select one of the three options:\n1.Modyfy words\n2.Play\n3.Exit\n Your choice:')))    
    if selected==1:
       modifywords()
    elif selected==2:
        playmenu()
        mainmenu()
    else:
        print('Thanks for playing\nWe hope you have liked it')
        return exit(0)
        
def modifywords():
    selected2=int((input('Select one of the four options:\n1.Add category\n2.Modify category\n3.Delete category\n4.Return to main menu\nYour choice:')))
    if selected2==1:
        addcategory()
        modifywords()
    elif selected2==2:
        modifycategory()
        modifywords()
    elif selected2==3:
        deletecategory()
        modifywords()
    elif selected2==4:
        mainmenu()


def modifycategory():
    selected3=int((input('Select one of the four options:\n1.Change a Category Name\n2.Add a new Word\n3.Remove a word\n4.Return to main menu\nYour choice:')))
    return selected3

def playmenu():
    print('TODO')
def addcategory():
    print('TODO')
def modifycategory():
    print('TODO')
def deletecategory():
    print('TODO')
    
def main():
    mainmenu()
        
if __name__=='__main__':
    main()

######################## PARTE DE JOKIN ########################

import json

with open('C:\\Users\\alumno\\Desktop\\words.json','r') as file:
    data = json.load(file)

def mainmenu():
    print("Welcome to the hangman game !!!")
    print("Select one of the three options:")
    answer = input("1 - Modify words\n2 - Play\n3 - Exit\n\nYou choose: ")
    print("\n------------------------------------------------------------------------------------------\n")
    return answer

def print_cats():
    categories = []
    for category in data:
        categories.append(category)
    print("Available categories: ",categories)

def add_cats():
    print("\n============= ADDING NEW CATEGORY =============\n")
    print_cats()
    new_cat = input("Enter the category to be introduced: ")
    while new_cat in data: 
        print("\nThe category",new_cat,"already exists. Introduce a new one")
        new_cat = input("Enter the category to be introduced: ")
    data[new_cat] = None
    print("\nThe category",new_cat,"has been created")
    
def del_cat():
    print("\n============= DELETING A CATEGORY =============\n")
    print_cats()
    x_cat = input("Which of the categories would you like to delete? ")
    while x_cat not in data:
        print("\nThe category",x_cat,"doesn't exist. Introduce an existing category")
        x_cat = input("Which of the categories would you like to delete? ")
    del data[x_cat]
    print("\nCategory",x_cat,"has been deleted")

def change_catname():
    print("\n============= CHANGING CATEGORY NAME =============")
    print_cats()
    old_name = input("The name of which category would you like to edit? ")
    while old_name not in data:
        print("\nThe category",old_name,"doesn't exist. Introduce an existing category")
        old_name = input("The name of which category would you like to edit? ")
    new_name = input("What name would you like to replace it with? ") 
    data[new_name] = data[old_name]
    del data[old_name]
    
def add_word():
    print("\n============= ADDING A NEW WORD =============\n")
    print_cats()
    category_select = input("Which category would you like to add your word to? ")
    while category_select not in data:
        print("\nThe category",category_select,"doesn't exist. Introduce an existing category")
        category_select = input("Which category would you like to add your word to? ")
    word_add = input("What word would you like to add? ")
    while word_add in data[category_select]:
        print("\nThe word",word_add,"is already in the category",category_select+". Introduce another one")
        word_add = input("What word would you like to add? ")
    data[category_select].append(word_add)
    print("\nThe word",word_add,"has been added to",category_select)

def remove_word():
    print("\n============= REMOVING A WORD =============\n")
    print_cats()
    category_select = input("The word of which category would you like to delete? ")
    while category_select not in data:
        print("\nThe category",category_select,"doesn't exist. Select an existing one")
        category_select = input("The word of which category would you like to delete? ")
        
    print("\nWords in",category_select+":",data[str(category_select)])
    
    word_x = input("Select a word to delete: ")
    while word_x not in data[str(category_select)]:
        print("\nThe word",word_x,"is not in the selected category. Introduce a correct word")
        word_x = input("Select a word to delete: ")
    data[category_select].remove(word_x)
    print("\nThe word",word_x,"has been deleted from",category_select)
    
while True:
    
    print("\n------------------------------------------------------------------------------------------\n")
    
    answer = mainmenu()
    
    #######################################################################################################

    if answer == "1": #user wants to modify the words
        print_cats()
        print("\nChoose one of the options: ")
        answer2  = input("1 - Add category\n2 - Modify category\n3 - Delete category\n4 - Return to main menu\n\nYou choose: ")

        if answer2 == "1": #user wants to add category
            add_cats()
        
        elif answer2 == "2": #user wants to modify category
            print("\nChoose one of the options: ")  
            answer3 = input("1 - Change category name\n2 - Add a new word\n3 - Remove a word\n4 - Return to main menu\n\nYou choose: ")
            
            if answer3 == "1": #user wants to change category name
                change_catname()
            
            elif answer3 == "2": #user wants to add a new word
                add_word()
            
            elif answer3 == "3": #user wants to remove a word
                remove_word()
            
            else: #user wants to return to main menu
                print("\nReturning to main menu...")
                
        elif answer2 == "3": #user wants to delete category
            del_cat()
        
        elif answer2 == "4": #user wants to return to main menu
            print("\nReturning to main menu...")
    
    
    
    #######################################################################################################    
    
    # elif answer == "2": #user wants to play
    
    #######################################################################################################    

    elif answer == "3":
        print("- Exiting game... -")
        break
    
    else:
        print("Error!")

file.close()

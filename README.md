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

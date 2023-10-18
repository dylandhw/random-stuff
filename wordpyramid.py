word = input("Enter a word no more than 10 characters long.\n")
UI = input("Enter yes to call the second function.\n")
a = 1
index = 0

#Make pyramid prints each letter of word one by one making a pyramid
def make_pyramid():
    for i in range(len(word)):
        print(word[:i])
    for l in range(len(word)):
        print(word[l:])

#Pyramid two prints each letter of word one by one, new line each
def pyramid_two():
    for k in range(len(word)):
        print("\n",word[k])

#Calls to and runs the functions
def main():
    make_pyramid()
    
    UI.lower()
    if (UI == "yes"):
        pyramid_two()
main()

import random

def story1():
    something

def story2():
    something

def story3():
    something


def story_picker():
    i = random.randint(1,3)
    if i == 1:
        story1()
    elif i == 2:
        story2()
    elif i == 3:
        story3()

def story():
    print("***********************************************")
    print("****************SOME STORY NAME****************")
    print("Would you like to hear a story? Y/N")
    resp = input()
    if resp == "Y" or resp == "y":
        story_picker()
    elif resp == "N" or resp == "n":
        print("Then why did you open this?")
        input()
        print("umm okay...")
        input()
    else:
        print("what")
        print("I guess that's a no...")
        input()
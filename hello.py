#!/usr/bin/python
def oneself():
    lastname = input("Your Lastname ?\n");
    lastname = lastname.strip();

    while lastname == "":
        lastname = input("Your Lastname ?\n");
        lastname = lastname.strip();

    firstname = input("Your Firstname ?\n");
    firstname = firstname.strip();

    while firstname == "":
        firstname = input("Your Firstname ?\n");
        firstname = firstname.strip();

    age = input("How old are you ?\n");
    age = age.strip();

    while age.isdigit() == False:
        age = input("How old are you ?\n");
        age = age.strip();

    print("Hello", lastname, firstname, "!! You're", age, "years old !!\n");
    print("Thanks you !!");
    return;
def hello_help():
    print("This script gonna ask you your Firstname, Lastname and your age\n");
    print("If you answer an empty answer, he will ask you again\n");
    print("If you answer other than an integer for your age, he will ask you again\n");
    print("Thanks you !!\n");
    check_answer();
    return;
def check_answer():
    answer = input("Welcome to Hello !!! Did you need help or did you want to present yourself ?\nTape help or present : ");
    while answer != "help" and answer != "present":
        answer = input("Welcome to Hello !!! Did you need help or did you want to present yourself ?\nTape help or present : ");
    if answer == "help":
        hello_help();
    elif answer == "present":
        oneself();
    return;
check_answer();
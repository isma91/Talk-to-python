#!/usr/bin/python
import sys
def afficher(nom, prenom, age):
	print("Hello my name is ", nom, prenom, " and i'm " , age , " years old !!");
	return
error = 0;
if len(sys.argv) == 2 and sys.argv[1] == "--help":
	print("Help to use indx.py !!\n");
	print("hello.py [--lastname] [--firstname] [--age]\n");
	print("--lastname=Foo	Your lastname\n");
	print("--firstname=Bar	Your firstname\n");
	print("--age=42	Your age\n");
elif len(sys.argv) != 4:
	error = error + 1
	print("You must write your lastname, firstname and age !!\n");
	print("Type index.py --help to have some info !!\n");
elif len(sys.argv) == 4:
	if str(sys.argv[1]) == "" or sys.argv[1][11:] == "":
		error = error + 1;
		print("Your lastname can't be empty !!");
	if str(sys.argv[2]) == "" or sys.argv[2][12:] == "":
		error = error + 1;
		print("Your firstname can't be empty !!");
	if str(sys.argv[3]) == "" or sys.argv[3][6:] == "":
		error = error + 1;
		print("Your age can't be empty !!");
if error == 0:
	afficher(sys.argv[1][11:], sys.argv[2][12:], sys.argv[3][6:]);

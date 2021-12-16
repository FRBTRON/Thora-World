#!/usr/bin/python
# Author : Kingtebe
# Date : 07-10-2021, 01.32 WIB
# Silahkan rikod, para recoder terhormat !!

import os
import sys
import time
import random
import platform
import colorama
colorama.init()
os.system("clear")
print ("""
\u001b[33;1m███████╗███████╗ ██████╗████████╗  ██████╗ ██╗  ██╗██████╗ ██╗      ██████╗ ██╗████████╗
\u001b[33;1m██╔════╝██╔════╝██╔════╝╚══██╔══╝  ╚════██╗╚██╗██╔╝██╔══██╗██║     ██╔═══██╗██║╚══██╔══╝
\u001b[33;1m███████╗███████╗██║  ███╗  ██║█████╗█████╔╝ ╚███╔╝ ██████╔╝██║     ██║   ██║██║   ██║
\u001b[37;1m╚════██║╚════██║██║   ██║  ██║╚════╝╚═══██╗ ██╔██╗ ██╔═══╝ ██║     ██║   ██║██║   ██║
\u001b[37;1m███████║███████║╚██████╔╝  ██║     ██████╔╝██╔╝ ██╗██║     ███████╗╚██████╔╝██║   ██║
\u001b[37;1m╚══════╝╚══════╝ ╚═════╝   ╚═╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚══════╝ ╚═════╝ ╚═╝   ╚═╝
 \u001b[37;1m___________________________
\u001b[37;1m| CREATOR \u001b[31;1m=> \u001b[33;1mSSGT\u001b[31;1m-\u001b[37;1m3XPLOIT   \u001b[37;1m|
 \u001b[37;1m---------------------------
 \u001b[37;1m________________________________
\u001b[37;1m|\u001b[35;1mGIT\u001b[37;1mHUB \u001b[31;1m=> \u001b[34;1mhttps://bit.ly/321yYC6\u001b[37;1m|
 \u001b[37;1m--------------------------------
 \u001b[37;1m_________________________________
\u001b[37;1m|\u001b[31mYOU\u001b[37;1mTUBE \u001b[31;1m=> \u001b[34;1mhttps://bit.ly/3dSA7P9\u001b[37;1m|
 \u001b[37;1m---------------------------------
""")
password = input ("PASSWORD => ")
if password == "ssgt%198*":
	print ("[+] Password Correct !")
	time.sleep(5)
	os.system("clear")
else :
	print ("[-] WRONG PASSWORD !")
	exit()
try:
	import requests
	from bs4 import BeautifulSoup
except:
	exit("\nModule not installed\n")

if platform.python_version().split(".")[0] != "3":
	exit("\n ~> We Dont Support python2\n    ketik: python %s "%sys.argv[0]+"\n")

url = "https://api.myip.com"

m = '\033[1;31m'
p = '\033[1;37m'
h = '\033[1;32m'
k = '\033[1;33m'
b = '\033[1;35m'
c = '\033[1;36m'
x = '\033[1;36m'
q = '\033[1;30m'

def countdown(second):
	while second:
		mins, secs = divmod(second,60)
		timer = '  \033[37m~\033[30m> \033[37mWaiting \033[30m⟨\033[33m{:02d}:{:02d}\033[30m⟩ \033[37mseconds'.format(mins,secs)
		print(timer,end="\r")
		time.sleep(1)
		second -= 1

def App(userid):
	browser = [
		"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36"
		"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
		"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
		"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9",
	]
	headers = {
		"Host":"thora.world",
		"user-agent":random.choice(browser),
	}
	count = 1
	while True:
		numeric = random.randint(1000,9999)
		verify = requests.get(f"https://thora.world/faucet.php?microwallet=ExpressCrypto&id1={userid}&currency=TRX&startclaim=Start%20claiming&key=0642f{numeric}f59aab752fe2e8f78470d62",headers=headers)
		if verify.status_code != 200:
			print(f"  {p}[{m}!{p}] {p}Failed {p}({m}{count}{p}) get reward ~~{m}> {h}0.00000200 TRX")
			count += 1
		else:
			print(f"  {p}[{h}✓{p}] Succes {p}({h}{count}{p}) Total TRX Sent ~~{m}> {h}0.00000200 TRX")
			count += 1
		countdown(60)
try:
	os.system("cls" if os.name == "nt" else "clear")
	api = requests.get(url).json(); print(f"\n {m} ___________.__\n  {m}\__    ___/|  |__   ________________\n    {m}|    |   |  |  \ /  _ \_  __ \__  \.\n    {p}|    |   |   Y  (  <_> )  | \// __ \_\n    {p}|____|   |___|  /\____/|__|  (____  /\n                  {p}\/                  \/\n {q}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n  {p}[{h}•{p}] Author {m}: {p}SSGT-3XPLOIT\n  {p}[{h}•{p}] Github {m}: {p}https://bit.ly/321yYC6\n  {p}[{h}•{p}] Youtube {m}: {p}https://bit.ly/3dSA7P9\n {q}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n  {p}[{m}•{p}] YOUR IP {m}: {h}{api['ip']}")
	dompet = input(f"  {p}[{m}•{p}] User-Id {m}: {p}")
	print(f" {q}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	if "EC" not in dompet: exit(f"  {p}~{h}> {p}User-ID, Don't Exist Or Empty ! {m}!!\n")
	else: App(dompet)

except KeyboardInterrupt:
	exit()

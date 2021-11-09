#coding=utf-8
#!/usr/bin/python2
#coding=utf-8
try:
    import os,re,time
except IOError:
    os.system("pip2 install requests")
    os.system("pip2 install mechanize")
    os.system("python2 Awais.py")

try:
    os.mkdir("/sdcard/infect-tool")
except OSError:
    pass

abm = """
\033[1;97m             ___           ___           ___                       ___     
     /\  \         /\  \         /\  \                     /\__\    
    /::\  \       _\:\  \       /::\  \       ___         /:/ _/_   
   /:/\:\  \     /\ \:\  \     /:/\:\  \     /\__\       /:/ /\  \  
  /:/ /::\  \   _\:\ \:\  \   /:/ /::\  \   /:/__/      /:/ /::\  \ 
 /:/_/:/\:\__\ /\ \:\ \:\__\ /:/_/:/\:\__\ /::\  \     /:/_/:/\:\__\
 \:\/:/  \/__/ \:\ \:\/:/  / \:\/:/  \/__/ \/\:\  \__  \:\/:/ /:/  /
  \::/__/       \:\ \::/  /   \::/__/       ~~\:\/\__\  \::/ /:/  / 
   \:\  \        \:\/:/  /     \:\  \          \::/  /   \/_/:/  /  
    \:\__\        \::/  /       \:\__\         /:/  /      /:/  /   
     \/__/         \/__/         \/__/         \/__/       \/__/    
\033[1;97m------------------------------------------------- 
\033[1;97m(~) Author  : AWAIS_KHAN
\033[1;97m(~) Github  : https://github.com/awaismoman
\033[1;97m(~) Fb Page : https://facebook.com/Termux-commands-free
\033[1;97m-------------------------------------------------
"""

def main():
    os.system("clear")
    print(abm)
    os.system("cd load && python2 __loading__")
    os.system("clear")
    print(abm)
    print("\033[1;97m[\033[1;93m1\033[1;97m] Install infect tool for cloning")
    time.sleep(0.05)
    print("\033[1;97m[\033[1;93m2\033[1;97m] Install infect extracting tool")
    time.sleep(0.05)
    print("\033[1;97m[\033[1;93m0\033[1;97m] Tool Logout")
    time.sleep(0.05)
    print("\033[1;97m-------------------------------------------------")
    mx()
def mx():
    AWAIS = raw_input("\n[!] Select a valid option : ")
    if MOMAND TRICKS =="1":
        os.system("cd data && python2 data")
    if MOMAND TRICKS =="2":
        os.system("cd exts && python2 exts")
    if MOMAND TRICKS =="0":
        print("")
        print("\033[1;92mTool Logout Successfull").center(50)
        print("")
        os.system("exit")
    else:
        print("")
        print("\033[1;91mPlease select a valid option").center(50)
        print("")
        time.sleep(1)
        main()
if __name__ == '__main__':
    main()

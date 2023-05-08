#library for control the keyboard and mouse
import pyautogui
#library for open the browser
import webbrowser
#library use it to delay
import time

#first step control the browser
webbrowser.register('chrome',
                     None,
					 webbrowser.BackgroundBrowser('C:\Program Files\Google\Chrome\Application\chrome.exe')) #the path of the chrome in the myPC
#link of my profile				 
link = 'https://www.facebook.com/mohamed.Marzok.1907/'
webbrowser.get('chrome').open_new(link)	
time.sleep(7)	#delay 7 secs for lag of internet
pyautogui.hotkey('ctrl','f') #for search in the profile			 
pyautogui.typewrite("what's on your mind?")		#search for this syntax
pyautogui.press('enter')			 #to start the search
pyautogui.press('escape')
pyautogui.press('enter')   #to write the post
time.sleep(4)
pyautogui.typewrite("يقول النبي ﷺ :أقربكم منى مجلساً يوم القيامة أكثركم صلاة عليّ.  اللَّهُــمَّ صـَلِّ وَسَـــلِّمْ علـى نَبِيِّنَـــا مُحمَّد ﷺ") #the post
#now control on the mouse to click in the post
pyautogui.click(650,700)
					 
					 
					 
					 
					 
import pyautogui
import time
#Sap setting calss
class SaplogonBOT (object): #creating a class to create bot object
# Defining the functions, user ID , passwrord , instances in sap
 	def __init__(self,userid,paswd,instance): #preinvoke
         self.user=userid
         self.password=paswd
         self.inst=instance

        def activate_preinvoke(self):
		pyautogui.hotkey('win','d') #to minimaxize all the windows
	def activate_saplogon(self):
		pyautogui.hotkey('win','r') #to invoke the run bar in window
		pyautogui.typewrite('saplogon') #to type saplogon on screenbar
		pyautogui.press('enter') #to press enter on saplogon 
            #return True #try the code and notify the user as True else false
        #except:
            #return False
	def activate_postinvoke(self):
        #try:
		pyautogui.hotkey('win','up') #to maximize the window of saplogon (this enables to fix the window on resultion)
	def open_instance(self,inst):
        #try:
		pyautogui.hotkey('ctrl','F')
	        pyautogui.typewrite(self.instance)
		pyautogui.press('enter')
            #return True
        #except:
            #return False
	def saplogin(self):
		pyautogui.typewrite(self.userid)
		pyautogui.press('tab')
		pyautogui.typewrite(self.paswd)
		pyautogui.press('enter')

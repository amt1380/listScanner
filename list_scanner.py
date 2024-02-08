import os 
import sys 
import colorama
from colorama import init,Fore
init(convert=True)
class my_lists():
     global ref_list,input_list
     ref_list =  [i for i in range(1,301)]
     input_list=[] # test example 
     def __init__(self) -> None:
          self.list=list 
          self.app_name = "list scanner"
 
     def scan(): 
         
         os.system('cls')
         print("\n")
         print(""" █████╗ ███╗   ███╗████████╗
██╔══██╗████╗ ████║╚══██╔══╝
███████║██╔████╔██║   ██║   
██╔══██║██║╚██╔╝██║   ██║   
██║  ██║██║ ╚═╝ ██║   ██║   
╚═╝  ╚═╝╚═╝     ╚═╝   ╚═╝   """)
         print('\n')
        
         condition=True
         while condition:
             
            user_input=input(Fore.LIGHTCYAN_EX+"[]>>"+Fore.RESET)
            
             
            if str(user_input)=="skip":
                
                condition=False
            elif (str(user_input)=='' or str(user_input)==' '):
                pass
            
            else: 
             try:       
              input_list.append(int(user_input))
             except:
                pass
         try:    
            for  i in input_list :
             if i in ref_list:
                 print(Fore.LIGHTGREEN_EX+f'{i} founded in list ...')
                 ref_list.remove(i)
             elif (i not in ref_list) : 
                print(Fore.LIGHTRED_EX+f"{i} not found in list ..."+Fore.RESET)
            
         except:
            pass
         return  ref_list 
         

object = my_lists.scan()
object
print(Fore.LIGHTYELLOW_EX+"updated list ... \n"+Fore.RESET+str(object))
input("...")

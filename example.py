#importing practice.py as a module to access all atttributes

import practise as pc

vara=open("example.txt","w")
vara.close()

phrase = input("enter phrase ")
pc.translate(phrase)



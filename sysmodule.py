import cowsay

import sys

a=len(sys.argv)

if a<2:
    sys.exit("too less arguments")
elif a==2:
    cowsay.cow("my name is "+sys.argv[1])
    cowsay.trex("my name is "+sys.argv[1])                
elif a==3: 
    print("my name is",sys.argv[1],sys.argv[2]+" and arguments passed =",a-1)
elif a>2:
    print("arguments passed =",a-1)           
    for name in sys.argv[1:]:
        print("my name is",name)


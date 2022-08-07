import random
def draw():
    #random numbers
    number=[]
    for i  in range(0,5):
             if  len( number )  < 5:
                     number.append(random.randint(1,91))
    return number

code=input('enter code : ')
if  code == '*959#':
    #menu one
    print('(1) monday speciall\n(2) Draw result\n(3)Terms and condition')
    option=input('enter choice : ')
    # menu two for monday speciiall
    if  option=="1":
        print('(1) Direct-1 \n (2)  2 sure\n (3) Direct-3')
        option=input('enter choice : ')
        
        #menu three for direct -1
        if  option=='1':
            entry=int(input('Enter a number(1-90) : '))
            #entry range input
            if entry  in range(0,91):
                print( "you have selected ", entry)
                #amout sector direct -1
                entry = float(input('Enter a amout (1-200) : '))
                if entry in range(1, 201):
                    print('your amout is %.2f  ' % entry)
                    confirmation = int(input('Enter  (1) to comfirm \n (2) to cancel '))
                    if confirmation == '1':
                        print('Thanks  for using our online platform,\n wait for your a momo massage')
                    elif option == '2':
                        print('Try again next time')
            else:
                print('wrong input \n Try again ')
                #two sure menu
        elif option=='2':
            entry=int(input('Enter a two sure number ( jxt two nummbers ) : '))
            if entry  in range(0,91):
               entry = float(input('Enter a amout (1-200) : '))
               if entry in range(1, 201):
                    print('your amout is %.2f  ' % entry)
                    confirmation=int(input('Enter  (1) to comfirm \n (2) to cancel '))
                    if confirmation=='1':
                        print('Thanks  for using our online platform,\n wait for your a momo massage')
                    elif option=='2':
                        print('Try again next time')
            else:
                print('wrong input \n Try again ')
 #direct-3 menu
        elif option == '3':
            entry = int(input('Enter a Direct-3 number ( jxt three numbers ) : '))
            if entry in range(0, 91):
                print("you have selected ", entry)
                entry = float(input('Enter a amount (1-200) : '))
                if entry in range(1, 201):
                     print('your amount is %.2f  ' % entry)
                confirmation = int(input('Enter  (1) to comfirm \n (2) to cancel '))
                if confirmation == '1':
                    print('Thanks  for using our online platform,\n wait for your a momo massage')
                elif option == '2':
                    print('Try again next time')
            else:
                print('wrong input \n Try again ')
                #draw results from
    elif option=='2':
        print('enter your draw results ' )
        results=input("enter your draw results here : ")
        if results==draw():
            print(draw())
        else:
            print('Sorry uve lost \n  try again later' , draw())
    elif option=='3':
        print('enter your draw results ' )
else:
    print('unknow application')

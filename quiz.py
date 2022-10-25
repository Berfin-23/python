print("\nWelcome to my Python quiz\n")

sta=str(input("Are you ready?\n>")).lower()
p=0
crt=0
wrg=0
inv=0
if sta == "yes" or sta == "y":
    
    print('''\nRules:\n1)Type the correct option for the answer i.e a , b , c or d.\n2)Each correct answer gives 10 points.\n3)Each wrong answer deduces 5 points.\n4)Invalid answers also deducts 5 points.\n5)Score 80% to pass\n6)Have fun\n''')

    #question 1
    print('''Q1:What is the correct syntax to output \"Hello world\" in Python?\n\na)print(\"Hello World\")\nb)printf(\"Hello World\")\nc)prt(\"Hello World\")\nd)dis(\"Hello World\")\n''')
    ans=str(input("Enter the answer:")).lower()
    if ans == "a":
        print("+10 points")
        p+=10
        crt+=1
    elif ans == "b" or ans == "c" or ans == "d":
        print("-5 points")
        p+=5
        wrg+=1

    else:
        print("Give valid answer!!\n-5 points")
        p-=5
        inv+=1

    #question 2
    print("\nQ2:How to insert a comment in python code?\n\na)//This is a comment\nb)/*This is a comment*/\nc)#This is a comment\n")
    ans=str(input("Enter the answer:")).lower()
    if ans == "c":
        print("+10 points")
        p+=10
        crt+=1
    elif ans == "b" or ans == "a":
        print("-5 points")
        p-=5
        wrg+=1

    else:
        print("Give valid answer!!\n-5 points")
        p-=5
        inv+=1

    #question 3
    print("\nQ3:Whic one is not a legal variable name in python?\na)_quiz\nb)Quiz\nc)my_quiz\nd)my-quiz\n")
    ans=str(input("Enter the answer:")).lower()
    if ans == "d":
        print("+10 points")
        p+=10
        crt+=1
    elif ans == "b" or ans == "c" or ans == "a":
        print("-5 points")
        p-=5
        wrg+=1
    else:
        print("Give valid answer!!\n-5 points")
        p-=5
        inv+=1

    #question 4
    print("\nQ4:What is the correct file extension for python files?\na).python\nb).pn\nc).py\nd).pt\n")
    ans=str(input("Enter the answer:")).lower()
    if ans == "c":
        print("+10 points")
        p+=10
        crt+=1
    elif ans == "b" or ans == "d" or ans == "a":
        print("-5 points")
        p-=5
        wrg+=1
    else:
        print("Give valid answer!!\n-5 points")
        p-=5
        inv+=1

    #question 5
    print("\nQ5:What is the correct syntax of function in python?\na)def quiz():\nb)create quiz():\nc)func quiz():\nd)function quiz():\n")
    ans=str(input("Enter the answer:")).lower()
    if ans == "a":
        print("+10 points")
        p+=10
        crt+=1
    elif ans == "b" or ans == "d" or ans == "c":
        print("-5 points")
        p-=5
        wrg+=1
    else:
        print("Give valid answer!!\n-5 points")
        p-=5
        inv+=1

    
    #question 6
    print("\nQ6:Which method can be used to remove any whitespace from both the beginning and end of a string?\na)trim()\nb)len()\nc)strip()\nd)rem()\n")
    ans=str(input("Enter the answer:")).lower()
    if ans == "c":
        print("+10 points")
        p+=10
        crt+=1
    elif ans == "b" or ans == "d" or ans == "a":
        print("-5 points")
        p-=5
        wrg+=1
    else:
        print("Give valid answer!!\n-5 points")
        p-=5
        inv+=1

    #question 7
    print("\nQ7:Which operator is used to concatenate two or more strings?\na)x\nb)*\nc)&\nd)+\n")
    ans=str(input("Enter the answer:")).lower()
    if ans == "d":
        print("+10 points")
        p+=10
        crt+=1
    elif ans == "b" or ans == "a" or ans == "c":
        print("-5 points")
        p-=5
        wrg+=1
    else:
        print("Give valid answer!!\n-5 points")
        p-=5
        inv+=1

    #question 8
    print("\nQ8:Which operator is used to multiply two numbers?\na)/\nb)*\nc)x\nd)&\n")
    ans=str(input("Enter the answer:")).lower()
    if ans == "b":
        print("+10 points")
        p+=10
        crt+=1
    elif ans == "d" or ans == "a" or ans == "c":
        print("-5 points")
        p-=5
        wrg+=1
    else:
        print("Give valid answer!!\n-5 points")
        p-=5
        inv+=1
    
    #question 9
    print("\nQ9:Which statement is used to stop a loop?\na)exit\nb)return\nc)stop\nd)break\n")
    ans=str(input("Enter the answer:")).lower()
    if ans == "d":
        print("+10 points")
        p+=10
        crt+=1
    elif ans == "b" or ans == "a" or ans == "c":
        print("-5 points")
        p-=5
        wrg+=1
    else:
        print("Give valid answer!!\n-5 points")
        p-=5
        inv+=1

    #question 10
    print("\nQ10:How do you start a while loop in Python?\na)while x > y{}\nb)while(x > y)\nc)while x > y:\nd)x > y while{}\n")
    ans=str(input("Enter the answer:")).lower()
    if ans == "c":
        print("+10 points")
        p+=10
        crt+=1
    elif ans == "b" or ans == "a" or ans == "d":
        print("-5 points")
        p-=5
        wrg+=1
    else:
        print("Give valid answer!!\n-5 points")
        p-=5
        inv+=1


    print("\nYou have answered ",crt," questions correctly")

    if wrg == 0:
        pass
    else :
        print("You have answered ",wrg," questions wrongly")
        
    print("Your score is ",p,"%")

    if inv == 0:
        pass
    else:
        print("You gave invalid answer for ",inv," questions\nTry to give correct answer")

    if p >= 60:
        print("You have passed in the quiz:)")
    else:
        print("You have failed the exam:(\nTry again")    

elif sta == "no" or sta == "no":
    print("\nOk bye:\n)")

else :
    print("\nPlease enter Yes/No\n")
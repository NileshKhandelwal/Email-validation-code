email=input("Enter your email:") #g@g.in
k,j,d=0,0,0
if len(email)>=6:
    if email[0].isalpha():
        if ("@"in email) and (email.count("@")==1):
            if (email[-4]==".")^(email[-3]=="."):
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1
                if k==1 or j==1 or d==1:
                    print("wrong email.remove spaces Capital letter and special symbols except @  _  . ") 
                else:
                    print("right email")  
            else:
                print("wrong email. Put (.) at its correct positon")
        else:
            print("wrong email,@ must be present in emailid one time only")
    else:
        print("wrong email,Start emailid from alphabets")
else:
    print("wrong emailid because email id is very Short")
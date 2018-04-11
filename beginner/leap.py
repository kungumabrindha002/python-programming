a=int(input())
if(a%4==0):
    if(a%100==0):
        if(a%400==0):
            print("leap year")
        else:
            print("no")
    else:
        print("noo")
else:
    print("nah")

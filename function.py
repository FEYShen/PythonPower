##def Main():
##    names=['shen','wang','wu','chen']
##    names[0]='shenyu'
##    for name in names:
##        print(name)


##def Main():
##    words=["cat","bat","sat"]
##    with open("words.txt","w") as f:
##        for word in words:
##            f.write(word+"\n")


##import math
##
##def Main():
##    try:
##        radius=float(input("Please enter a radious: "))
##        area=math.pi*radius**2
##        print("area={}".format(area))
##    except:
##        print("your did not enter a number!")

def Reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

def Main():
    rev=Reverse('Drapsicle')
    for char in rev:
        print(char,end='')


if __name__=='__main__':
    Main()


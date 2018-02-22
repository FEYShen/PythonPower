import cs50

##f=cs50.get_float()
##c=5/9*(f-32)
###print("{:.1f}".format(c))
##print(c)

##print("s: ", end="")
##s=cs50.get_string()
##
##print("t: ", end="")
##t=cs50.get_string()
##
##if s !=None and t!=None:
##    if s==t:
##        print("same")
##    else:
##        print("different")
        

print("s: ", end="")
s=cs50.get_string()
if s==None:
    exit(1)

t=s.capitalize()

print("s: {}".format(s))
print("t: {}".format(t))

exit(0)

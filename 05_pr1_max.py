# def maximum(n1,n2,n3):
#     if n1>n2 and n1>n3:
#         print("n1 is big")
#     elif n2>n1 and n2>n3:
#         print("n2 is big")
#     elif n3>n1 and n3>n2:
#         print("n3 is big")

# m = maximum(13,16,55)
# print("The value of maximum is:"+str(m))

def maximum(num1,num2,num3):
    if(num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    else:
        if(num2>num3):
            return num2
        else:
            return num3

m = maximum(12,43,22)
print("The value of maximum is "+ str(m))    
def remove_and_splite(string,word):
    newStr = string.replace(word,"")
    return newStr.strip()

this="     Chaitanya is good   "
n= remove_and_splite(this,"Chaitanya")
print(n)
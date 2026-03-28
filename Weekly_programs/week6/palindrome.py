#24331A05D8
#tO fIND a wORD wHETHER iT iS a pALINDROME or nOT
text=input("Enter a word")
rev=text[::-1]
if text==rev:
    print("{} is a palindrome".format(text))
else:
    print("{} is not a palindrome".format(text))

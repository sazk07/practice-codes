text = "X-DSPAM-Confidence:    0.8475";

atpos = text.find('.')


findnumber = text [atpos-1:]
#to convert to float
floatconvert = float (findnumber)
print (floatconvert)
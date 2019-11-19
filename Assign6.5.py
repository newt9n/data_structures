#Write code using find() and string slicing
#(see section 6.10) to extract the number at
#the end of the line below. Convert the extracted
#value to a floating point number and print it out.
#Desired Output
#---------------
#0.8475
#--------------

#define 'txt' as the string to search
txt = ("X-DSPAM-Confidence:    0.8475")
#extract the index number starting! at the '0'
strtpoint = txt.find('0')
#slice er up
fnd2end = txt[strtpoint:]
#convert to float
fnd2end = float(fnd2end)
#and print it out!
print(fnd2end)
#simpler (-;
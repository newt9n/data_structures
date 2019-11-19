data = 'From pete.johnson@ab.ca.za Sat Mar  5 10:10:16 2019'
atposition = data.find('@')
print(atposition)
sppos = data.find(' ', atposition)
print(sppos)
hostname = data[atposition+1 : sppos]
print(hostname)
#data find the 1st position seems to be the last in the string


def unique(l):
    ulist = []
    [ulist.append(x) for x in l if x not in ulist]
    return ulist


string = input('Enter the string:')

string = ' '.join(unique(string.split()))

print("After removing Duplicate values the strinig is : "+string)


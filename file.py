''' def count(word):
    if word.isupper() == True:
        global cCap
        cCap += 1
    elif word.islower() == True:
       global cSma
       cSma += 1
    elif word == " ":
        global cSpa
        cSpa += 1
    elif word == "\n":
        global cNew
        cNew += 1
    try:
        global lst
        i = lst.index(word)
        global lsts
        lsts[i] += 1
    except:
        pass
    try:
        global lst1
        i = lst1.index(word)
        global lstb
        lstb[i] += 1
    except:
        pass

cCap = 0
cSma = 0
cSpa = 0
cNew = 0
lst = list("abcdefghijklmnopqrstuvwxyz \n")
lst1 = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ \n")
lsts = [0]*28
lstb = [0]*28

if __name__ == '__main__':

    f = open('blog.txt', 'r')

    for word in f.read():
        count(word)

    f.close()

    print("No of Capital Letters : ", cCap)
    print("No of Small Letters : ", cSma)
    print("No of NEWLINE used : ", cNew)
    print("No of Words : ", cSpa+1)
    print("List of Alphabets:")
    for i in range(26):
        print("{} : {}".format(lst[i], lsts[i]))
        print("{} : {}".format(lst1[i], lstb[i]))
        print("\n")
'''


if __name__ == '__main__':
    f = open('blog.txt', 'r')
    lst = []
    for word in f.read():
        lst.append(word)
    f.close()
    dict = {}
    for i in lst:
        if i in dict.keys():
            pass
        else:
            freq = list(map(lambda x: x == i, lst))
            count = freq.count(True)
            dict[i] = count
    print(dict)
    dict1 = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1], reverse = True)}
    for i in dict1:
        print(f'({i}  :  {dict[i]})')
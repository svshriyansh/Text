#The function will create a new file and write the given data
def new_file(n):
    with open("n","a+") as N:
        for key, value in n.items():
            N.write('%s -> %s \n'%(key,value))
    #N.write(str(dict(n)))
    #N.read()
    N.close()
#The function will check the repeated words
def repeated(n):
    count = {}  #Making the dictionary  
    for i in n:
        if i in count:
            count[i] +=1
        else:
            count[i]=1 
    '''for key in count:
        if count[key]>1:
          print(key,count[key])'''
    Max(count)  #calling max function
#The function will ale to sort the data in decending order
def Max(n):    
    data = list(n.items())
    data.sort(key=lambda elem: elem[1])
    data.reverse()
    #print("data",data)
    listdata1= [i[0] for i in data]
    #print("string is",listdata1)
    listdata2=[i[1] for i in data]
    #print("2nd",listdata2)
    #converting list into dict
    new_dict=dict(zip(listdata1,listdata2))
    #new_dict ={listdata1[i] : listdata2[1] for i in range(len(listdata1))}
    #print("new dict is",new_dict)
    #print(type(new_dict))
    TOP_10 = dict(list(new_dict.items())[0:10])
    #print("Top 10 are : \n")
    for key in list(TOP_10.keys()):
        print(key,"->",TOP_10[key])   
    new_file(TOP_10)
#The function will able to calculate the character in data
def character(n):
    character =0
   
    for i in n:
        character +=len(i)
    print("Number of charactes are {}".format(character))
    words = list(n)
    with open("n","a+") as N:
        N.write("Frequency of top 10 repeated character are :\n")
    N.close()
    print("Frequency of top 10 repeated character are :\n")
    repeated(words)
#The function will ale to clculate the number of words
def nwords(n):
    word = list(n.split(" "))
    #print("\nwords are ",word)
    #print("\nLength of word is",len(word))
    with open("n","a+") as N:
        N.write("\nFrequency of top 10 repeated words are :\n")
    N.close()
    print("\nFrequency of top 10 repeated words are :\n")
    repeated(word)
#The function is taking input of the file to open it
def File (n):
    F= open(n) 
    k = F.read()
    print("\n")
    #print(k)
    character(k)
    nwords(k)
    print(end="\nThank you \n")
    F.close()

print("Enter the file name :")
File_name = input()
File(File_name)

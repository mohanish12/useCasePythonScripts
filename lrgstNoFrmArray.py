def lrgstNoFrmArray(Narray):
    Narray.sort(reverse=True)
    num = Narray[0]
    print (num)
    for i in range(1,len(Narray)):
        num = num * 10 + Narray[i]
    print(num)




lrgstNoFrmArray([1, 34, 3, 98, 9, 76, 45, 4])
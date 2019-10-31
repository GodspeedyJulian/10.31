def 1 ():
    PCode=[]
    PDescription=[]
    PRetialprice=[]
    FileHandle=open("Product.txt", "r")
    i = 1
    lines =file.readlines()
    for i in range(0,len(a)-2,3):
        PCode.append(a[i][:-2])
        PDescription.append(a[i+1][:-2])
        PRetialprice.append(float(a[i+2][:-2]))
    file.close()
    Print("Product File contents written to arrays")
    return PCode, PDescription, Pretialprice

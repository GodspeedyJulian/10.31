PCode  =['1','2','3','4','5','6']
def ProductCodeSearch(PCode):
    Found = False
    SearchCode=input("input your searchcode")
    for i in range(len(PCode)):
        if PCode[i]==SearchCode:
            return i
            Found = True
    if Found ==False:
        return -1
print(ProductCodeSearch(PCode))

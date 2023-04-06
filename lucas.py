#lucas list
print("podaj pierwszy wyraz ciągu Lucasa")
Luc1 = input()
LucA = (int(Luc1))

print("podaj drugi wyraz ciągu Lucasa")
LucB = int(input())
print(LucA, LucB, LucA+LucB)
LucC = LucA + LucB

Lucas = [LucA, LucB, LucC]
print(Lucas)

print(type(len(Lucas)))

while len(Lucas) < 10:
    Ilast = len(Lucas) -1
    last = Lucas[Ilast] 
    Iprevious = len(Lucas) -2
    previous = Lucas[Iprevious]
    nextelement = last + previous
    Lucas.append(nextelement)
    print(Lucas)
 
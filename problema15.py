Elevii clasei a V-a se repartizează în clase câte 25 în ordinea mediilor clasei a IV-a. Radu este pe locul x în ordinea mediilor. În
ce clasa va fi repartizat (A, B, C, D sau E)?. Exemplu : date de intrare : x=73 date de ieşire : C.
x=int(input("dati locul lui radu: "))
if(x // 25 == 0):
    print("Radu va fi in clasa A")
elif(x // 25 == 1):
    print("Radu va fi in clasa B")
elif(x // 25 == 2):
     print("Radu va fi in clasa C")
elif(x // 25 == 3):
     print("Radu va fi in clasa D")
elif(x // 25 == 4):
     print("Radu va fi in clasa E")
     else:
         print("Radu nu intra in primii 125 elevi")




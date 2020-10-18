La un concurs se dau ca premii primilor 100 de concurenţi, tricouri de culoare albă, roşie, albastră şi neagră, în această
secvenţă. Ionel este pe locul x. Ce culoare va avea tricoul pe care-l va primi? Exemplu : date de intrare : x=38 date de ieşire :
rosie. 

x= int(input("dati locul lui Ionel: "))
if(x <= 100):
    if(x % 4 == 0):
        print("va primi un tricou negru")
        elif(x % 4 == 1):
            print("va primi un tricou alb")
            elif(x % 4 == 2):
                print("va primi un tricou rosu")
                            elif(x % 4 == 3):
                 print("va primi un tricou albastru")
                 else:
                     print("Ionel e intre primii 100 si nu va primi un premiu")




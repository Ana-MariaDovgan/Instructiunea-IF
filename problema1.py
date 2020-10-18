n1=int(input("numarul primului elev"))
n2=int(input("numarul al doilea elev"))
n3=int(input("numarul al treilea elev"))
p1=int(input("punctajul prinului elev"))
p2=int(input("punctajul al doilea elev"))
p3=int(input("punctajul al treilea elev"))
if ((p1>p2)and(p1>p3)):
    print("punctajul maxim are elevul cu numarul",n1)
elif ((p2>p1)and(p2>p3)):
    print("punctajul maxim are elevul cu numarul",n2)
elif ((p3>p1)and(p3>p2)):
     print("punctajul maxim are elevul cu numarul",n3)
elif((p1==p2)and(p1>p3)and(p2>p3)):
     print(n1,n2,"au punctaj egal")
elif((p2==p3)and(p2>p1)and(p3>p1)):
     print(n2,n3,"au punctaj egal")
elif((p1==p3)and(p1>p2)and(p3>p2)):
     print(n1,n3,"au punctaj egal")
else:
    print("toti au acelasi punctaj")









                    





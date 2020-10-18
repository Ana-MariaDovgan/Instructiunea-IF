Pe o masă de biliard sunt bile albe, roşii şi verzi. Din fiecare culoare sunt bile de două dimensiuni: mari şi mici. Să se afişeze
câte bile sunt în total pe masa de biliard. Un jucător vrea să-i spuneţi care bile sunt mai multe , cele mici sau cele mari, afişând
numărul lor. De ce culoare sunt bilele cele mai numeroase? Precizaţi numărul lor. Exemplu: Date de intrare Nr. bile albe mici: 2
Nr. bile albe mari: 3 Nr. bile rosii mici: 1 Nr. bile rosii mari: 4 Nr. bile verzi mici: 3 Nr. bile verzi mari: 4 Date de ieşire Totalul
bilelor: 17 Mari: 11 bile Verzi: 7 bile .
amari=int(input("Numarul bilelor albe mari: "))
rmari=int(input("Numarul bilelor rosii mari: "))
vmari=int(input("Numarul bilelor verzi mari: "))
amici=int(input("Numarul bilelor albe mici: "))
rmici=int(input("Numarul bilelor rosii mici: "))
vmici=int(input("Numarul bilelor verzi mici: "))
bmari=amari+rmari+vmari
bmici=amici+rmici+vmici
print("Sunt",bmari+bmici,"bile in total")
if(bmari>bmici):
    print("Bile mari: " ,bmari)
elif(bmici>bmari):
    print("Bile mici:",bmici)
else:
    print("Numarul de bile mari si mici e egal",bmici)
if((amari+amici)>(rmari+rmici))and((amari+amici)>(vmari+vmici)):
     print("Bilele albe sunt cele mai multe: ",amari + amici)
elif((rmari+rmici)>(amari+amici))and((rmari+rmici)>(vmari+vmici)):
    print("Bilele rosii sunt cele mai multe: ",rmari + rmici)
elif((vmari+vmici)>(rmari+rmici))and((vmari+vmici)>(amari+amici)):
    print("Bilele verzi sunt cele mai multe: ",vmari + vmici)
elif((amari+amici)==(rmari+rmici))and((amari+amici)>(vmari+vmici)):
    print("Bilele albe si rosii sunt cele mai multe: ",amari+amici)
elif((amari+amici)>(rmari+rmici))and((amari+amici)==(vmari+vmici)):
    print("Bilele albe si verzi sunt cele mai multe: ",amari+amici)
elif((vmari+vmici)==(rmari+rmici))and((amari+amici)<(vmari+vmici)):
    print("Bilele rosii si verzi sunt cele mai multe: ",rmari+rmici)
elif((amari+amici)==(rmari+rmici))and((amari+amici)==(vmari+vmici)):
    print("Numar egal de bile",amari+amici)
























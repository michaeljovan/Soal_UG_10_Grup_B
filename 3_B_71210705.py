a = float(input("Masukan bilangan pertama : ")) 
b = float(input("Masukan bilangan kedua : ")) 
c = input("Masukan kalimat : ")

if "tambah" in c : 
    print("Hasil tambah",a,"dengan",b,"adalah",a+b ) 
elif "kurang" in c : 
    print("Hasil Pengurangan",a, "dengan",b,"adalah", a-b )
elif "bagi" in c : 
    print("hasil pembangian",a,"dengan", b,"adalah",a/b)
elif "kali" in c : 
    print("Hasil perkalian",a ,"dengan",b ,"adalah", a*b) 

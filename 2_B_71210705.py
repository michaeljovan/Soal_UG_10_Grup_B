a = int(input("Masukkan besar RSI : "))  
b = (input("Masukkan kondisi MACD : "))

if (a >= 70) and (b == "golden-cross" ) : 
    print("RSI lebih dari sama dengan 70 dan MACD golden-cross, tunggu MACD sampai death-cross")
elif (a <= 30) and (b == "death-cross") : 
    print("RSI kurang dari sama dengan 30 dan MACD death-cross, tunggu MACD sampai golden-cross") 
elif (a <= 30) and (b == "golden-cross") : 
    print("RSI kurang dari sama dengan 30 dan MACD golden-cross, saatnya beli")
elif (a >= 70) and (b == "death-cross") : 
    print ("RSI lebih dari sama dengna 70 dan MACD death-cross, saatnya jual") 
else : 
    print("RSI berada di area 31-69, bukan saatnya membeli maupun menjual")
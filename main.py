modern_sozluk = {"cringe":"Garip ya da utandırıcı bir şey","afk":"bilgisayarı veya başka bir teknolojik cihazı kullanırken birden açık bırakıp bekletmek",
            "lol":"komik bir eye verilen cevap","rofl":"yerde yuvarlanarak gülmek","sheesh":"onaylamamak",
            "creepy":"korkunç","aggro":"agresifleşmek/sinirlenmek","tgif":"Thank god it's Friday/Tanrıya şükür bugün Cuma"}
word = input("anlamadığınızz bir kelime yazın: ")
if word in modern_sozluk.keys():
    print(modern_sozluk[word])
else:
        print("maalesef kelime sozlukte bulunmadi ")

---------
1. Kod
---------

meme_dict = {
    "CRINGE": "Garip ya da utandırıcı bir şey",
    "LOL": "Komik bir şeye verilen cevap",
    "ROFL": "Bir şakaya karşılık cevap",
    "SHEESH": "Onaylamamak",
    "CREEPY": "Korkunç",
    "AGGRO": "Agresifleşmek/sinirlenmek"
}

print("Merhaba! Meme Sözlüğüne hoş geldiniz.")
print("Aşağıda bazı meme kelimeleri ve anlamları bulunmaktadır.")

for _ in range(5):
    word = input("\nAnlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

    if word in meme_dict:
        print(f"{word} - {meme_dict[word]}")
    else:
        print(f"{word} sözlükte bulunamadı.")

print("\nTeşekkür ederiz! Meme Sözlüğü'nu kullandığınız için umarız eğlenceli olmuştur.")







---------
2. Kod
---------
meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            }
            
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Bu kelime henüz yok")


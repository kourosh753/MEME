

meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "SHEESH": "cok rahatlatici bir sey gorunce denilir",
            "MUSICALLY": "2017 zamaninin tiktoku" 
            }




word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dict.keys():
    # Kelime eşleşiyorsa ne yapmalıyız?

    print(meme_dict[word])
else:
    # Kelime eşleşmiyorsa ne yapmalıyız?

    print("maalesef bu kelimeyi bilmiyorum")

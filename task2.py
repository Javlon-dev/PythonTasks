# 2-masala:
# Shunday funksiya tuzingki, funksiya chaqiriilib unga biror so'z kiritilsa, oxirgi harfini olib, matnning boshiga qo'ysin
# Misol uchun: funksiya2("mohirdev") — vmohirde

def replaceLastToFirst(text):
    text = text.replace(" ", "")
    leng = len(text)
    if leng > 1:
        return f"{text[leng - 1]}{text[0:leng - 1]}"
    else:
        return text


print("Matn kiriting: ")

print("{}".format(replaceLastToFirst(input())))

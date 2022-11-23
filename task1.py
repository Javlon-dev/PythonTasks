# 1-masala
# Shunday funksiya tuzingki, funksiya chaqirilib unga matn kiritilsa o'sha matnning uzunligini hisoblab bersin
# misol uchun: funksiya1("mening ismim xon") — matn uzunligi 16 ta harfdan iborat

def printTextLength(text):
    return len(text.replace(" ", ""))


print("Matn kiriting: ")

print("Matn uzunligi {} ta harfdan iborat".format(printTextLength(input())))

# CamelCase'ga o'rganib qolganman, Pythonda bu narsa problem ekan :)

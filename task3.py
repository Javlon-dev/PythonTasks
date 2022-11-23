# 3-masala:
# Shunday funksiya tuzingki, funksiya chaqiriilib unga biror matn kiritilsa,
# agar matn kichik harflarda bo'lsa katta harflarga,
# katta harflarda bo'lsa kichik harflarga o'g'irib bersin
# Misol uchun:
# 1) funksiya3("Mening ismim xon") — mENING ISMIM XON
# 2) funksiya3("MEN MOHIRDEVDa Oqiyman") — men mohirdevda oQIYMAN

def swapcaseText(text):
    return text.swapcase()


print("Matn kiriting: ")

print("{}".format(swapcaseText(input())))

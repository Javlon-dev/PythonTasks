# 4-masala:
# Shunday dastur tuzingki, U foydalanuvchidan restoranga necha kishiga tushlik qilmoqchi ekanini so'rasin.
# Agar ular 8 kishidan ko'p bo'lsa, stol uchun kutib turishini.
# Agar 8 dan kam bo'lsa stol tayyor ekani haqida xabar chiqarsin
#
# misol uchun:
# 1-holat
# — Nechi kishi tushlik qilmoqchisizlar: 12
# — Stol hozir band edi, biroz kutib turishingizni so'raymiz
# 2-holat
# — Nechi kishi tushlik qilmoqchisizlar: 5
# — Stol tayyor tushlik qilishingiz mumkin

maxPeopleCount = 8


def isReserved(numberOfPeople):
    if numberOfPeople > maxPeopleCount:
        return True
    else:
        return False


print("Nechi kishi tushlik qilmoqchisizlar? ")
numberOfPeople = input()

try:
    numberOfPeople = int(numberOfPeople)
    if numberOfPeople <= 0:
        raise SyntaxError()
except:
    print("Uzr siz xato kiritdingiz!!!")
    exit(-1)

if isReserved(numberOfPeople):
    print("Stol hozir band edi, biroz kutib turishingizni so'raymiz")
else:
    print("Stol tayyor tushlik qilishingiz mumkin")

# 5-masala
# Foydalanuvchidan 4 ism kiritishini so'rang va u ismlarni bitta yangi listga joylashtiring.
# Ismlar uzunligi 5 tadan ko'p bo'lgan ismlarnigina for takrorlanish operatori orqali ekranga chiqaring.
#
# hint: foydalanuvchidan 4 ta ism kiritishini so'rash uchun 4 marta inputdan foydalanamiz,
# listga yangi element qo'shishni darsda o'rganganmiz.
#
# misol uchun:
# 1-ismni kiriting: Farida
# 2-ismni kiriting: Shoxista
# 3-ismni kiriting: Aziz
# 4-ismni kiriting: Malika
# Ismlar: Farida, Shoxista, Aziz, Malika
# Ekranga chiqadi:
# —Farida
# —Shoxista
# —Malika

maxNames = 4
maxLength = 5
nameList = []

for i in range(1, 5):
    print(f"{i} - ismni kiriting:")
    nameList.append(input().replace(" ", ""))

for name in nameList:
    if len(name) > maxLength:
        print(name)

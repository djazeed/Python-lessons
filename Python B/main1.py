# a = 5
# print(type(a))


# a =15
# b = 10.0
# c = a+b
# print(c)


# hozirgi_yil = 2023
# ism = str(input("Ism "))
# familiya= str(input("familiya "))
# yil = int(input("Yilim "))
# overal = hozirgi_yil - yil
# print(f"Mening ismim {ism} {familiya} yoshim {overal}")



# moshinalar = ['nexia','damas','kaptiva','malibu']
# # for index, mashina in enumerate(moshinalar):
# #     print("Mening moshinam",index, mashina)

# cars = []
# print("5 ta moshina nomini kiriting")
# for car in range(5):
#     cars.append(str(input(f"{car+1} ci moshinani nomini kiriting ")))
# print(cars)


# list1 = []
# # list1.append(str(input("Ismingizni kiriting ")))
# for ism in range(1,6):
#     list1.append(str(input(f"{ism}ismingizni kiriting ")))
# # a_z = list1
# if 'nozima' and 'salom' and 'begzod' in list1:
#     for item in list1:
#      print(F'salom {item}')
# else:
#     print("yoq")

# # if list1[0].lower() == "nozima":
# #     print('bor')
# # else:
# #     print("yoq")



# ismlar =  ['Aziz','Nozima','Asror','Begzod','Qaxorjon']
# for ism in ismlar:
#     print(f"Salom {ism}") 
# print(f"Kod {len(ismlar)} marta takrorlanadi")

# for son in range(11,101,2):
#     print(son)
#     print(son**3)


# kinolar = []
# print("5 ta kinoni nomini kiriting")
# for kino in range(1,6):
#     kinolar.append(str(input(f"{kino} chi kinoni nomini kiriting ")))
# print(kinolar)


# odamlar = int(input("Bugun nechi kishi bilan suhbatlashdingiz\n"))
# ismlar = []
# for ism in range(odamlar):
#     ismlar.append(str(input(f"{ism+1} chi odamning ismi")))
# print(f'bugun siz {ismlar} bialn suhbatlashgansiz')

# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car != 'gm':
#         print(car.title())
#     else:
#         print(car.upper())

# ism = str(input("Ismingizni kiriting "))
# if ism.lower() == 'admin':
#     print('Xush kelibsiz, Admin foydalanuvchilar royhatini korasizmi')
# else:
#     print(f'uzur {ism.title()} sizga kirirsh mumkin emas')

# # a = int(input("son "))
# # b = int(input('son '))
# # if a==b:
# #     print("SonlaR teng")

# # sonn = int(input("son kiriting "))
# # if sonn<0:
# #     print("Manfiy son")
# # else:
# #     print("musbat son")

# # son = float(input("Son kiriting "))
# # if son>0:
# #     print(f"{son**(0.5)}")
# # else:
# #     print("Musbat son kiriting")

# # menu = ['osh','qazonkabob','shashlik','norin','somsa']
# # 'manti' in menu 


# # son = int(input("Juft son kiriritng "))
# # if son%2:
# #     print("Bu toq son juft son kiriritng")
# # else:
# #     print("Rahmat")


# # yosh = int(input("Yoshingizni kiriting "))
# # if yosh<=4 or yosh>=60:
# #     price = 0
# # elif yosh<18:
# #     price = 10000
# # else:
# #     price = 20000
# # print(f"Xurmatli mijoz sizga chipta narxi {price}")


# # a = int(input("Son kiriting "))
# # b = int(input("Son kiriting "))

# # if a == b:
# #     print(f"{a} va {b} sonlari teng")
# # elif a<b:
# #     print(f"{a} soni {b} sonidan kichik")
# # elif a>b:
# #     print(f"{a} soni {b} sonidan katta")




# mahsulotlar = ['osh','manti','shashlik','shorva','non','manti','moshxorda','salat','mastava','pirashki']
# savat = []

# for ovqat in range(5):
#     savat.append(str(input(f"{ovqat+1} chi mahsulotni kiriritng ")))
# dokon_bor = []
# dokon_yoq = []
# for mahsulot in savat:
#     print(mahsulot)
#     if mahsulot in mahsulotlar:
#         dokon_bor.append(mahsulot)
#     else:
#         dokon_yoq.append(mahsulot)

# if dokon_yoq:
#     print("Siz soragan ushbu narsalar yoq")
#     for mahsulot in dokon_yoq:
#         print(mahsulot)
# else:
#     print("siz soragan barcha mahsulotlar dokonimizda bor")


# foydalanuvchilar = []
# for foydalanuvchi in range(1,6):
#     foydalanuvchilar.append(input(f"{foydalanuvchi} chi logini kiriting "))

# print(f"A arteriyasidagi oqim {oqim_a} ml/daqiqa")
# print(f"Y arteriyasidagi oqim {oqim_y} ml/daqiqa")
# print(f"X arteriyasidagi oqim {oqim_x} ml/daqiqa")


# user = str(input("Login kiriting "))

# if user.lower() in foydalanuvchilar:
#     print(f"Bunaqa login mavjud {user.title()}")
# else:
#     print(f"Xush kelibsiz {user.title()}")


# son = int(input("Butun son kiriting "))
# for s in range(1,11):
#     if son%s:
#         print(f"{son} soni {s} ga bo'linmaydi")
#     else:
#         print(f"{son} soni {s} ga qoldiqsiz bo'linadi")




# tromb_a = float(input("A arteriyasidagi tromb qiymati "))
# tromb_y = float(input("Y arteriyasidagi tromb qiymati "))
# tromb_x = float(input("X arteriyasidagi tromb qiymati "))

# oqim_a = 180

# oqim_y = oqim_a *  tromb_y
# oqim_x = oqim_a *  tromb_x

# bosim_a = 120
# bosim_y = bosim_a * (tromb_y * 0.01)
# bosim_x = bosim_a * (tromb_x * 0.01)


# print(f"Umumiy bosim: {bosim_a} mmHg")
# print(f"Y arteriyasidagi yangi bosim {bosim_y} mmHg")
# print(f"X arteriyasidagi yangi bosim {bosim_x} mmHg")



# son = float(input("Juft son kiriting: "))
# if son%2==1:
#     print("Bu son juft emas.")
# else:
#     print("Rahmat!")



# yosh = int((input("Yoshingiz nechida?")))

# if yosh<=4 or yosh>=60:
#     narh = 0
# elif yosh < 18:
#     narh = 10000
# else:
#     narh = 20000
# print(f"Chipta {narh} so'm")


# x = int(input("Birinchi sonni kiriting: "))
# y = int(input("Ikkinchi sonni kiriting: "))
# if x==y:
#     print(f"{x}={y}")
# elif x<y:
#     print(f"{x}<{y}")
# else:
#     print(f"{x}>{y}")


# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
# savat = []

# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# if savat:
#     for mahsulot in savat:
#         if mahsulot in mahsulotlar:
#             print(f"Do'konimizda {mahsulot} bor")
#         else:
#             print(f"Do'konimizda {mahsulot} yo'q")
# else: 
#     print("Savatingiz bo'sh")            


# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)

# if mavjud_emas:
#   print("Do'konimizda quyidagi mahsulotlar yo'q:")
# for mahsulot in mavjud_emas:
#   print(mahsulot)
# else:
#   print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
    




# users = ['alisher1983','aziza','yasina' 'umar']

# login = input("Yangi login tanlang: ")

# if login in users:
#     print('Login band, yangi login tanalng!')
# else:
#     print("Xush kelibsiz!")




# ukam = {
#     "ismi":"Qaxxor",
#     "yosh":"18",
#     "manzil":"Toshkent"
#     }
# print(f"Ukamning ismi {ukam["ismi"].title()} yoshi {ukam["yosh"]} da yashash manzili esa {ukam['manzil'].title()}")


# oilam ={
#     "ukam":"osh",
#     "singlim":"shashlik",
#     "onam":"somsa",
#     "otam":"jizbiz",
#     "man":"dimlama"
# }
# ukam = oilam["ukam"].title()
# singlim = oilam["singlim"].title()
# onam = oilam["onam"].title()
# print(f"Onamning sevimli taomlari {onam}")

# print(f"Ukamning sevimli taomi {oilam['ukam'].title()}, \nOnamning sevmli taomlari {oilam['onam'].title()}, \nMening sevimli taomim esa {oilam['man'].title()}")



# lugat = {
#     "string":"Matn va so'zlar",
#     "int":"Sonlar",
#     "float":"Butun sonlar",
#     "if":"agar :",
#     "elif":"agar yoki",
#     "else":"yoki",
#     "for":"sikl takrorlanuvchi",
#     "range":"sonlarni sikl qberadi",
#     "dict":"lug'at",
#     "list":"list",
#     "title":"Gapdagi har bir so'zning birinchi harfini katalashtirib beradi",
#     "lower":"Gapdagi hama so'zlarni kichina harfga o'girib beradi",
#     "upper":"matndagi har bir so'zni katta harfga o'girib beradi",
#     "capitalize":"matndagi faqat birinchi so'zning birinchi harfini katta harfga ogirb beradi",
#     "tuple":"o'zgarmas ro'yhat",
#     "get":"lugat ichidan kalitni qidirib beradi",

# }
# # print(lugat.items())
# kalit = input("Kalit so'z kiriting ").lower()
# # tajrima = lugat.get(kalit)
# # if tajrima == None:
# #     print("Bunday so'z mavjud emas")
# # else:
# #     print(f"{kalit.capitalize()} so'zi {tajrima} deb ataladi")

# print(lugat.get(kalit,"bunaqa metod mavjud emas"))








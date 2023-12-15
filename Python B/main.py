import random as r
    
def oyin(x = 10):
    print("Son o'yini ")
    son = r.randint(1,x)
    tahmin = 0
    while True:
        tahmin += 1
        o_son = int(input("1 dan 10 gacham o'ylagan soningizni kiriting\n>>"))
        if o_son > son:
            print(f"Yo'q men o'ylagan son {o_son} dan kichikroq")
        elif o_son < son:
            print(f"Yo'q men oylagan son {o_son} dan kattaroq")
        else:
            break
    print(f"tabriklayman siz {tahmin} ta urinish bilan toptingiz")
    return tahmin


def oyin_pc(x =10):
    print("Keling siz oylagan sonni topaman! ")
    min=(1)
    max=(x)
    tahmilar = 0
    flag = True
    while flag:
        tahmilar +=1
        if min != max:
            ta_son = r.randint(min,max)
        else:
            ta_son = min
        # tahmilar +=1
        javob = input(f"Siz {ta_son} sonini o'yladingiz. To'g'ri(T), kattaroq(+), kichikroq(-)").lower()
        if javob == "-":
            max = ta_son - 1
        elif javob == "+":
            min = ta_son + 1 
        else:
            break
    print(f"Siz o'ylagan soni {tahmilar} ta urinish bilan toptim!")
    return tahmilar




def sorov():
    javob = int(input(f"Assalomu aleykum siz kampyuter bilan o'ynaysizmi yoki kampyuter siz bilan o'ynasinmi\n (1) bosamgiz kampyuter siz bilan o'ynaydi\n (0) bosangiz siz kampyuter bilan o'ynaysiz\n>>>"))
    if javob == 1:
        oyin()
    else:
        oyin_pc()

sorov()

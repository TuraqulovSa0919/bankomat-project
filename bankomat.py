from random import randint
import random


hisobdagi_sum = randint(0, 120000000)

name_card = ["HUMO", "UZCARD", "VISA"]


while True: 
    
    hisobdagi_sum = randint(0, 120000000)
    check_pin = randint(0,1)
    pin_code = int(input("Pin kiriting: "))
    choice_card = random.choice(name_card)

    if len(str(pin_code)) == 4 and check_pin == 1:
            while True:

                    tanlov = int(input("""Tilni tanlang: 
                        1.РУСКИЙ
                        2.O'ZBEKCHA
                        3.ENGLISH
                        >>  """))
            
                    if tanlov == 2:
                        tanlov2 = int(input("""BO'LIMNI TANLANG: 
                            1.SMS XABARNOMA
                            2.KARTA BALANSI
                            3.PIN O'ZGARTIRISH
                            4.NAQD PUL OLISH
                            5.KARTA MA'LUMOTI
                            6.KARTANI TO'LDIRISH
                            7.KARTANI CHIQARISH
                            >> """))
                    
                        if tanlov2 == 1:
                            while True:
                                sms = int(input("""Sms xabarnomani yoqmoqchimisiz? 
                                                1.YOQISH
                                                2.O'CHIRISH
                                                >>  """))
                                if sms == 1:
                                    while True:
                                        javob_sms = int(input("""Iltimos kartangizga ulangan telefon ramaqingizni kiriting:
                                                            MISOL UCHUN +998901234567
                                                            +998   """))
                                        if len(str((javob_sms))) == 9:
                                            print("tabriklaymiz sms xabarnoma muvoffaqiyatli kiritildi!")
                                            suroq = input("""Chiqish >>""")
                                            if suroq:
                                                exit()                
                                        else:
                                            print("Telefon raqam xato\nQaytadan kiriting...")
                                            False

                                if sms == 2:
                                    while True:
                                        javob_sms = int(input("""Iltimos kartangizga ulangan telefon ramaqingizni kiriting:
                                                            MISOL UCHUN +998901234567
                                                            +998   """))
                                        if len(str((javob_sms))) == 9:
                                            print("tabriklaymiz sms xabarnoma muvoffaqiyatli o'chirildi!")
                                            suroq = input("""Chiqish >>""")
                                            if suroq:
                                                exit()                
                                        else:
                                            print("Telefon raqam xato\nQaytadan kiriting...")
                                            False
                        elif tanlov2 == 2: 
                                print(f"Balance: {hisobdagi_sum} so'm")
                                suroq = input("""Chiqish >>""")
                                if suroq:
                                    exit() 
                        
                        elif tanlov2 == 3:
                            while True:
                                tanlov = int(input("""Pin kodni o'zgartirmoqchimisiz?
                                      1.HA
                                      2.YO'Q"""))
                                if tanlov == 1:
                                    check_pin = int(input("PIN codingizni kiriting: "))
                                    if check_pin:
                                        print("Pin kod muvoffaqiyatli o'zgartirildi!!")
                                        backe = input("Ortga qaytish uchun istalgan tugmani bosing!\n🔙Ortga>> ")
                                    if backe:
                                        break  
                                if tanlov == 2:
                                        break
                        elif tanlov2 == 4:
                            
                            while True:

                                get_sum = int(input("""Chiqariladigan so'mmani tanlang: 
                                                    1.50 000
                                                    2.100 000
                                                    3.200 000
                                                    4.250 000
                                                    5.500 000
                                                    6.Boshqa so'mma
                                                    >> """))
                            
                                el, yu, ikki, ike, be = 50000, 100000, 200000, 250000, 500000 
                                if get_sum  ==  1 and  hisobdagi_sum >= el:
                                    print(f"Sizdan {el} som pul yechib olindi \nSizda {hisobdagi_sum - el} som pul qoldi")
                                    backe = input("Ortga qaytish uchun istalgan tugmani bosing!\n🔙Ortga>> ")
                                    if backe:
                                        break
                                elif get_sum  ==  2 and  hisobdagi_sum >= yu:
                                    print(f"Sizdan {yu} som pul yechib olindi \nSizda {hisobdagi_sum - yu} som pul qoldi")
                                    backe = input("Ortga qaytish uchun istalgan tugmani bosing!\n🔙Ortga>> ")
                                    if backe:
                                        break
                                elif get_sum  ==  3 and  hisobdagi_sum >= ikki:
                                    print(f"Sizdan {ikki} som pul yechib olindi \nSizda {hisobdagi_sum - ikki} som pul qoldi")
                                    backe = input("Ortga qaytish uchun istalgan tugmani bosing!\n🔙Ortga>> ")
                                    if backe:
                                        break   
                                elif get_sum  ==  4 and  hisobdagi_sum >= ike:
                                    print(f"Sizdan {ike} som pul yechib olindi \nSizda {hisobdagi_sum - ike} som pul qoldi") 
                                    backe = input("Ortga qaytish uchun istalgan tugmani bosing!\n🔙Ortga>> ")
                                    if backe:
                                        break 
                                elif get_sum  ==  5 and  hisobdagi_sum >= be:
                                    print(f"Sizdan {be} som pul yechib olindi \nSizda {hisobdagi_sum - be} som pul qoldi")
                                    backe = input("Ortga qaytish uchun istalgan tugmani bosing!\n🔙Ortga>> ")
                                    if backe:
                                        break
                                elif get_sum == 6:
                                    set_sum = int(input("Pul kiriting: "))
                                    if hisobdagi_sum >=set_sum:
                                        print(f"Sizdan {set_sum} som pul yechib olindi \nSizda {hisobdagi_sum - set_sum} som pul qoldi")
                                        backe = input("Ortga qaytish uchun istalgan tugmani bosing!\n🔙Ortga>> ")
                                        if backe:
                                            break
                                    
                                    else:
                                        print(f"Siz {set_sum} yechib olishingiz uchun sizda pul yetarli emas \nHisobingizdagi: {hisobdagi_sum} som mavjud")
                                        backe = input("Ortga qaytish uchun istalgan tugmani bosing!\n🔙Ortga>> ")
                                        if backe:
                                            break

                                else:
                                    print(f"Siz notug'ri raqam kiritdingiz!!!")
                                    backe = input("Ortga qaytish uchun istalgan tugmani bosing!\n🔙Ortga>> ")
                                    break
                        elif tanlov2 == 5:
                            print(f"Sizning Kartangiz: {choice_card} kartasi")
                            backe = input("Ortga qaytish uchun istalgan tugmani bosing!\n🔙Ortga>> ")
                            if backe:
                                break

                        elif tanlov2 == 6:
                            get_pul = int(input("Pul kiriting: "))
                            if get_pul > 0:
                                print(f"Sizda {hisobdagi_sum} mavjud")
                                hisobdagi_sum += get_pul
                                print(f"Siz hisobingizga {get_pul} so'm pul kiritdingiz!\nHisobingizda {hisobdagi_sum} mavjud")
                                backe = input("Ortga qaytish uchun istalgan tugmani bosing!\n🔙Ortga>> ")
                            if backe:
                                break
                        elif tanlov2 == 7:
                            print("Kartangizni qabul qiling")
                            exit()
                        
                    elif tanlov == 1 or tanlov==3:
                        print("Coming son!")
                        break
                    else:
                        print("Siz noto'g'ri raqam kiritdingiz")
                        continue
                            
    else:
        print("PIN kod noto'g'ri. Iltimos, qayta kiriting.")
        # False
                      
                                                 

                                
                                
                                
                            

                                    
                                

                    


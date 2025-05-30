import random
kom = random.randint(1,10)
kesempatan = 3
while kesempatan > 0 :
     user = int(input(f"ini adalah game tebak angka\nKESEMPATAN {kesempatan}x tebaklah angka (1-10): "))
     if user > kom : print(f"kom lebih kecil dari {user}")
     elif user < kom : print(f"kom lebih besar dari {user}")
     elif user > 10 and user < 1 : print("hanya 1-10")
     else : 
          print("anda benar")
          kesempatan = 0
     kesempatan -= 1
     if kesempatan == 0 : 
          m = input("mau main lagi (y/n) : ")
          if m == "y" : kesempatan = 3
     

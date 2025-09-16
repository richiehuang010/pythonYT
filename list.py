# ? MATERI INI BISA KALIAN BUKA DI 
# 
aktivitas = ["bermain","makan","tidur","belajar"]
print(aktivitas)
# KODE UNTUK MENAMBAHKAN
x = input("menambahkan aktivitas : ")
if x in aktivitas :
    print(f"{x} sudah ada")
else : 
    aktivitas.append(x)
    print(f"{x} berhasil ditambahkan")
    print(aktivitas)

# KODE UNTUK MENGHAPUS
# x = input("menambahkan aktivitas : ")
# if x not in aktivitas :
#     print(f"{x} tidak ditemukan")
# else : 
#     aktivitas.append(x)
#     print(f"{x} berhasil ditambahkan")
#     print(aktivitas)
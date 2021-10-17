import numpy as np

def menu_admin():
  p = input('\nSelamat Datang di Aplikasi penyewaan kendaraan \n1. Tambah Data \n2. List data \n3. Keluar \ninput : ')
  if p == "1":
      tambah_data()
  elif p == "2":
     print("Status pinjaman kendaraan")
     for x in arr_B:
       for i in x:
         print(i, end = " ")
     menu_admin()
  elif p == '3':
    login()

def menu_user():
  p = input('\nSelamat Datang di Aplikasi penyewaan kendaraan \n1. Peminjaman \n2. Pengembalian \n3. List Kendaraan \n4. Keluar \ninput : ')
  if p == '1':
      peminjaman()
  elif p == '2':
    pengembalian()
  elif p == '3':
     print("Status pinjaman kendaraan")
     for x in arr_B:
       for i in x:
         print(i, end = " ")
       print("\n")
     menu_user()
  elif p == '4':
    login()

def tambah_data():
  kendaraan = input('masukkan nama kendaraan : ')
  arr_B.insert(-1,[kendaraan, 'tidakdisewa', " "])
  print("data sudah masuk\n")
  print("Status pinjaman kendaraan")
  for x in arr_B:
    for i in x:
      print(i, end = " ")
    print("\n")
  menu_admin()
  
def peminjaman():
  i = input('Silahkan pinjam kendaraan dari menu kendaraan : ')

  while True:

    for c in arr_B:
      if i == c[0] and c[1] == "tidakdisewa":
        print("Kendaraan:" + c[0] + "disewa")
        c[1] = "disewa"
        menu_user()
        break
      elif i == c[0] and c[1] == "disewa":
        print("kendaraan : "+ c[0] + "telah disewa, lihat kendaraan lain")
        menu_user()
        break
    print("kendaraan tidak ada")
    menu_user()
    break
    
def pengembalian():
  i = input('Silahkan kembalikan kendaraan yang disewa : ')
  while True:
    for c in arr_B:
      if i == c[0]:
        print("Kendaraan" + c[0] + "dikembalikan")
        c[1] = "tidakdisewa"
        menu_user()
        break
    print("kendaraan tidak ada")
    menu_user()
    break
    
def login():
  arr_A = np.array = ([["Ubay","123","Admin"],["Hakim","123","User"],["Arrafiq","123","User"]])

  print("Login")
  username = input("masukkan username : ")
  password = input("masukkan password : ")

  while True:
    for x in arr_A:
      if username==x[0] and password==x[1] and x[2]=="Admin":
        print("\n\n"+ "Selamat datang admin " + x[0])
        menu_admin()
        break
      elif username==x[0] and password==x[1] and x[2]=="User":
        print("\n\n"+ "Selamat datang User " + x[0])
        menu_user()
        break
    print("Salah Akun. \n\n")
    break

arr_B = np.array = ([[]])
login()

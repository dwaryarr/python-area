def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Pembagian dengan angka nol tidak valid."

def kalkulator():
    print("Pilih operasi kalkulasi:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    choice = input("Masukkan pilihan (1/2/3/4): ")

    num1 = float(input("Masukkan angka pertama: "))
    num2 = float(input("Masukkan angka kedua: "))

    if choice == '1':
        print("Hasil:", tambah(num1, num2))
    elif choice == '2':
        print("Hasil:", kurang(num1, num2))
    elif choice == '3':
        print("Hasil:", kali(num1, num2))
    elif choice == '4':
        print("Hasil:", bagi(num1, num2))
    else:
        print("Pilihan tidak valid.")

kalkulator()

import requests

def get_current_ip():
    response = requests.get('https://ipinfo.io')
    data = response.json()
    return data['ip']

def get_ip_info(ip_address, api_key):
    api_url = f'https://ipinfo.io/{ip_address}?token={api_key}'

    response = requests.get(api_url)
    data = response.json()

# Menampilkan informasi IP Address
    print('IP Address:', data['ip'])
    print('Negara:', data['country'])
    print('Provinsi:', data['region'])
    print('Kota:', data['city'])
    print('Koordinat:', data['loc'])
    print('ISP:', data['org'])
    print('Zona Waktu:', data['timezone'])

# Check apakah API key telah diatur
api_key = input("Masukkan API Key IPinfo.io: ")
if not api_key:
    print("API Key tidak boleh kosong. Silakan coba lagi.")
else:
    # Menu utama
    print("Menu:")
    print("1. Ambil IP saat ini")
    print("2. Input IP Address")
    menu_choice = input("Pilih menu (1/2): ")

    if menu_choice == '1':
        # Mengambil IP saat ini
        ip_address = get_current_ip()
        print("IP saat ini:", ip_address)
        get_ip_info(ip_address, api_key)
    elif menu_choice == '2':
        # Memasukkan IP Address
        ip_address = input("Masukkan IP Address: ")
        get_ip_info(ip_address, api_key)
    else:
        print("Pilihan tidak valid.")

from PIL import Image
import os

# Fungsi untuk mengompresi gambar PNG
def compress_png(input_file, output_folder, target_size):
    try:
        # Buka gambar
        img = Image.open(input_file)

        # Menentukan dimensi baru untuk gambar dengan aspek rasio yang tetap
        max_size = (1024, 1024)  # Ubah ke ukuran yang sesuai
        img.thumbnail(max_size, Image.LANCZOS)

        # Simpan gambar yang sudah dikompresi
        img.save(output_folder, optimize=True)

        # Mengecek ukuran gambar yang sudah diompres
        img_size = os.path.getsize(output_folder)

        # Periksa apakah ukuran gambar lebih kecil dari target_size
        while img_size > target_size:
            # Perkecil dimensi gambar lagi
            max_size = (max_size[0] - 100, max_size[1] - 100)
            img.thumbnail(max_size, Image.LANCZOS)

            # Simpan gambar yang sudah dikompresi
            img.save(output_folder, optimize=True)
            img_size = os.path.getsize(output_folder)

        print(f'{input_file} telah diompresi dan disimpan di {output_folder}')

    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    input_file = input('Masukkan nama file gambar yang akan diompres: ')
    target_size = 500 * 1024  # 500 KB dalam byte
    output_folder = 'compressed/' + input_file  # Menyimpan dalam folder "compressed"

    # Memeriksa apakah folder "compressed" sudah ada atau belum
    if not os.path.exists('compressed'):
        os.makedirs('compressed')

    compress_png(input_file, output_folder, target_size)

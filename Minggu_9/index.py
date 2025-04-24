import random
from collections import deque

#Fungsi Tambah Antrian
def tambah_antrian(antrian):
    plat_nomor = random.randint(1000, 4000)
    plat_belakang = (random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=2))
    plat = str(f'KB {plat_nomor} {''.join(plat_belakang)}')
    antrian.append(plat)
    print(f'Mobil dengan plat {plat} berhasil di tambahkan ke antrian.')
    return antrian

#Fungsi Cetak Daftar Antrian
def cetak_antrian(antrian):
    if len(antrian) == 0:
        print('Antrian masih kosong')
        return
    print('Daftar antrian : ')
    for i, plat in enumerate(antrian):
        print(f'Antrian {i+1}. {plat}')
    print('Semua antrian telah di cetak')
        
#Fungsi Mobil paling belakang keluar
def batal_antri(antrian):
    if len(antrian) == 0:
        print('Antrian kosong.')
        return
    keluar = antrian.pop()
    print(f'Mobil dengan plat {keluar} keluar.')
    return antrian
    
#Fungsi Penetuan Paket
def paket_cuci():
    paket = random.randint(1,4)
    if paket == 1:
        nama_paket = 'Cuci Kilat'
        harga_paket = 20000
    elif paket == 2:
        nama_paket = 'Cuci Standart'
        harga_paket = 30000
    elif paket == 3:
        nama_paket = 'Cuci Premium'
        harga_paket = 50000
    elif paket == 4:
        nama_paket = 'Cuci Sultan'
        harga_paket = 75000

    return nama_paket,harga_paket

#Fungsi Cetak Invoice
def cetak_invoice(mobil, nama_paket, harga_paket):
    print('Invoice pembayaran cuci Mobil Fli Carwash')
    print(f'Plat Mobil : {mobil}')
    print(f'Nama Paket : {nama_paket}')
    print(f'Harga Paket : Rp{harga_paket}')
    print('Terima kasih, datang kembali')

#Fungsi Cuci Mobil
def cuci_mobil(antrian):
    if len(antrian) == 0:
        print('Antrian kosong.')
        return
    mobil = antrian.popleft()
    nama_paket, harga_paket = paket_cuci()
    print(f'Mobil dengan plat {mobil} dicuci dengan paket "{nama_paket}."')
    print()
    cetak_invoice(mobil, nama_paket, harga_paket)
    return mobil, nama_paket, harga_paket

def main() :
    print('Halo Selamat Data di Fli Carwash')
    print('Silahkan pilih menu-menu berikut : ')
    print('1. Masukkan antrian.')
    print('2. Cetak daftar antrian.')
    print('3. Proses cuci mobil. ')
    print('4. Cancel antrian cuci mobil. ')
    print('5. Keluar Program') 
    
    while True : 
        operasi = int(input('Silahkan pilih operasi yang anda inginkan : '))
        if operasi == 1 :
            tambah_antrian(antrian)
            print()
        elif operasi == 2:
            cetak_antrian(antrian)
            print()
        elif operasi == 3:
            cuci_mobil(antrian)
            print()
        elif operasi == 4:
            batal_antri(antrian)
            print()
        elif operasi == 5:
            print('Anda memilih keluar.')
            break
    
antrian = deque()
main()
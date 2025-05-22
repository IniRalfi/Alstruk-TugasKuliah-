from datetime import datetime
from tabulate import tabulate

from database.transaksi import load_transaksi, simpan_transaksi

def lihat_riwayat(username):
    print("\n" + "="*40 + " 📜 RIWAYAT TRANSAKSI " + "="*40)

    all_transaksi = load_transaksi()

    transaksi_user = [t for t in all_transaksi if t['username'] == username]

    if not transaksi_user:
        print('Anda belum memiliki riwayat transaksi')
        return
    
    transaksi_user.sort(key = lambda x : x['tanggal'], reverse=True)

    data_tampilan = []
    for idx, trans in enumerate (transaksi_user,1):
        data_tampilan.append([
            idx,
            trans['tanggal'],
            trans['kendaraan'],
            trans['jenis_bbm'],
            f'{trans['liter']} L',
            f'Rp{trans['total']:,}'.replace(',', '.'),
            f'{trans['poin']} Poin'
        ])

    headers = [
        'No',
        'Tanggal',
        'Kendaraan',
        'Jenis BBM',
        'Jumlah',
        'Total',
        'Poin'
    ]

    print(tabulate(data_tampilan, headers=headers, tablefmt='grid'))
    print(f'\nTotal transaksi : {len(transaksi_user)}')
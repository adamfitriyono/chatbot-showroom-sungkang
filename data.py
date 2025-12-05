"""
data.py - Menyimpan semua data Showroom Mobil Sungkang
"""

def get_showroom_data():
    """Mengembalikan dictionary berisi semua data showroom"""
    
    showroom = {
        "nama": "Showroom Mobil Sungkang",
        "alamat": "Jl. Gatot Subroto No. 45, Semarang, Jawa Tengah 50123",
        "kota": "Semarang",
        "provinsi": "Jawa Tengah",
        "whatsapp": "+62 812-3456-7890",
        "instagram": "@sungkangmobil",
        "email": "info@sungkangmobil.com",
        "website": "www.sungkangmobil.com",
        "tahun_berdiri": 2010,
        
        "jam_operasional": {
            "Senin-Jumat": "08:00 - 18:00",
            "Sabtu": "08:00 - 14:00",
            "Minggu": "Libur",
            "Hari Libur Nasional": "Libur"
        },
        
        "daftar_mobil": [
            {
                "id": 1,
                "merek": "Toyota",
                "model": "Avanza 1.3 MT",
                "tahun": 2024,
                "kategori": "MPV",
                "harga": 181000000,
                "cicilan": 5800000,
                "spesifikasi": "7 seater, Manual, AC, Power steering"
            },
            {
                "id": 2,
                "merek": "Daihatsu",
                "model": "Xenia 1.3 MT",
                "tahun": 2024,
                "kategori": "MPV",
                "harga": 165000000,
                "cicilan": 5200000,
                "spesifikasi": "7 seater, Manual, AC, Power Window"
            },
            {
                "id": 3,
                "merek": "Honda",
                "model": "CR-V 1.5 Turbo",
                "tahun": 2024,
                "kategori": "SUV",
                "harga": 425000000,
                "cicilan": 13500000,
                "spesifikasi": "SUV Premium, Turbo, Automatic, CVT"
            },
            {
                "id": 4,
                "merek": "Toyota",
                "model": "Rush 1.5 MT",
                "tahun": 2024,
                "kategori": "SUV",
                "harga": 245000000,
                "cicilan": 7800000,
                "spesifikasi": "SUV Compact, Manual, AC, Power Window"
            },
            {
                "id": 5,
                "merek": "Honda",
                "model": "City 1.5 MT",
                "tahun": 2024,
                "kategori": "Sedan",
                "harga": 290000000,
                "cicilan": 9200000,
                "spesifikasi": "Sedan Compact, Manual, AC, ABS"
            },
            {
                "id": 6,
                "merek": "Toyota",
                "model": "Corolla 1.6 Manual",
                "tahun": 2024,
                "kategori": "Sedan",
                "harga": 312000000,
                "cicilan": 9900000,
                "spesifikasi": "Sedan Mid-size, Manual, AC, Power steering"
            },
            {
                "id": 7,
                "merek": "Isuzu",
                "model": "D-Max 2.5 Single Cabin",
                "tahun": 2024,
                "kategori": "Pickup",
                "harga": 285000000,
                "cicilan": 9100000,
                "spesifikasi": "Pickup, Diesel, Manual, AC"
            },
            {
                "id": 8,
                "merek": "Datsun",
                "model": "GO 1.2 MT",
                "tahun": 2024,
                "kategori": "Hatchback",
                "harga": 139000000,
                "cicilan": 4400000,
                "spesifikasi": "Hatchback, Manual, AC, Power Window"
            },
            {
                "id": 9,
                "merek": "Toyota",
                "model": "Innova 2.4 Diesel",
                "tahun": 2019,
                "kategori": "MPV Bekas",
                "harga": 285000000,
                "cicilan": 9100000,
                "spesifikasi": "Sangat Baik, Kilometer rendah, Full Service Record"
            },
            {
                "id": 10,
                "merek": "Honda",
                "model": "Jazz 1.5 Automatic",
                "tahun": 2018,
                "kategori": "Hatchback Bekas",
                "harga": 175000000,
                "cicilan": 5600000,
                "spesifikasi": "Baik, Terawat, Kilometer 75.000 km"
            },
            {
                "id": 11,
                "merek": "Mitsubishi",
                "model": "Pajero Sport 2.4 AT",
                "tahun": 2024,
                "kategori": "SUV",
                "harga": 480000000,
                "cicilan": 15200000,
                "spesifikasi": "SUV Premium, Automatic, 4x4, All Power"
            },
            {
                "id": 12,
                "merek": "Suzuki",
                "model": "Ertiga 1.5 MT",
                "tahun": 2024,
                "kategori": "MPV",
                "harga": 195000000,
                "cicilan": 6200000,
                "spesifikasi": "7 seater, Manual, AC, Power Window"
            },
            {
                "id": 13,
                "merek": "Hyundai",
                "model": "Creta 1.5 AT",
                "tahun": 2024,
                "kategori": "SUV",
                "harga": 320000000,
                "cicilan": 10200000,
                "spesifikasi": "SUV Modern, Automatic, Warranty"
            },
            {
                "id": 14,
                "merek": "Kia",
                "model": "Sonet 1.5 MT",
                "tahun": 2024,
                "kategori": "SUV",
                "harga": 280000000,
                "cicilan": 8900000,
                "spesifikasi": "SUV Compact, Manual, Modern Design"
            },
            {
                "id": 15,
                "merek": "Nissan",
                "model": "Grand Livina 1.5 MT",
                "tahun": 2024,
                "kategori": "MPV",
                "harga": 210000000,
                "cicilan": 6700000,
                "spesifikasi": "MPV Spacious, 7 seater, Terpercaya"
            },
            {
                "id": 16,
                "merek": "Toyota",
                "model": "Fortuner 2.8 Diesel AT",
                "tahun": 2024,
                "kategori": "SUV",
                "harga": 530000000,
                "cicilan": 16800000,
                "spesifikasi": "SUV Tangguh, Diesel, 7 seater, Premium"
            },
            {
                "id": 17,
                "merek": "Honda",
                "model": "Civic 1.5 Turbo AT",
                "tahun": 2024,
                "kategori": "Sedan",
                "harga": 450000000,
                "cicilan": 14300000,
                "spesifikasi": "Sedan Sporty, Turbo, Full Power"
            },
            {
                "id": 18,
                "merek": "Mazda",
                "model": "CX-5 2.5 AT",
                "tahun": 2024,
                "kategori": "SUV",
                "harga": 420000000,
                "cicilan": 13400000,
                "spesifikasi": "SUV Stylish, Automatic, Premium Interior"
            },
            {
                "id": 19,
                "merek": "Chevrolet",
                "model": "Trailblazer 2.0 AT",
                "tahun": 2024,
                "kategori": "SUV",
                "harga": 390000000,
                "cicilan": 12400000,
                "spesifikasi": "SUV Powerful, Automatic, Turbo"
            },
            {
                "id": 20,
                "merek": "Wuling",
                "model": "Cortez 1.5 MT",
                "tahun": 2024,
                "kategori": "MPV",
                "harga": 165000000,
                "cicilan": 5300000,
                "spesifikasi": "MPV Ekonomis, 7 seater, Terjangkau"
            }
        ],
        
        "promosi": [
            {
                "id": 1,
                "judul": "Diskon Langsung",
                "deskripsi": "Diskon Rp 10.000.000 untuk Avanza, Xenia, Rush"
            },
            {
                "id": 2,
                "judul": "Asuransi Gratis",
                "deskripsi": "Gratis Asuransi 1 Tahun untuk semua mobil baru"
            },
            {
                "id": 3,
                "judul": "DP 0%",
                "deskripsi": "DP 0% untuk tenor 24 bulan (kredit minimal Rp 150 juta)"
            },
            {
                "id": 4,
                "judul": "Trade-in Terbaik",
                "deskripsi": "Trade-in dengan nilai tukar tertinggi + Rp 5.000.000"
            },
            {
                "id": 5,
                "judul": "Cicilan Spesial",
                "deskripsi": "Cicilan Spesial Rp 3.999.000 untuk Datsun GO (60 bulan)"
            }
        ],
        
        "paket_pembiayaan": [
            {
                "tenor": "12 Bulan",
                "bunga": "3.5%",
                "dp_minimum": "20%",
                "catatan": "Mobil baru"
            },
            {
                "tenor": "24 Bulan",
                "bunga": "4.2%",
                "dp_minimum": "15%",
                "catatan": "Mobil baru & bekas"
            },
            {
                "tenor": "36 Bulan",
                "bunga": "4.8%",
                "dp_minimum": "10%",
                "catatan": "Mobil baru & bekas"
            },
            {
                "tenor": "48 Bulan",
                "bunga": "5.5%",
                "dp_minimum": "10%",
                "catatan": "Mobil baru saja"
            },
            {
                "tenor": "60 Bulan",
                "bunga": "6.2%",
                "dp_minimum": "15%",
                "catatan": "Mobil baru saja"
            }
        ],
        
        "layanan": [
            "Penjualan Mobil Baru",
            "Penjualan Mobil Bekas",
            "Layanan Test Drive (Gratis)",
            "Financing/Kredit",
            "Trade-in",
            "Konsultasi Gratis",
            "Layanan Purna Jual",
            "Asuransi"
        ],
        
        "fasilitas": [
            "Ruang tunggu ber-AC dengan WiFi gratis",
            "Ruang konsultasi privat",
            "Toilet bersih & fasilitas wudhu",
            "Mushola",
            "Kantin/Kafe kecil",
            "Area display mobil indoor & outdoor",
            "Test drive track khusus",
            "Mesin ATM & transfer bank nearby",
            "Tempat bermain anak-anak"
        ],
        
        "kontak_departemen": [
            {
                "departemen": "Sales Manager",
                "nama": "Bambang Sutrisno",
                "whatsapp": "+62 812-9876-5432"
            },
            {
                "departemen": "Sales Executive",
                "nama": "Siti Nurhaliza",
                "whatsapp": "+62 813-5678-9012"
            },
            {
                "departemen": "Finance/Kredit",
                "nama": "Ahmad Wijaya",
                "whatsapp": "+62 814-3456-7890"
            },
            {
                "departemen": "After Sales",
                "nama": "Hendra Kusuma",
                "whatsapp": "+62 815-2345-6789"
            }
        ]
    }
    
    return showroom
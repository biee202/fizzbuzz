#adli farabi (251011701039)

data_mahasiswa = {
    "22034567": "Fajar",
    "22039812": "Faldy",
    "22037654": "Aziiz"
}

data_nilai = {
    "22034567": [50, 70, 40, 80],
    "22039812": [78, 78, 80, 65],
    "22037654": [87, 88, 67, 69]
}

# Mencari mahasiswa dengan rata-rata tertinggi
nilai_tertinggi = 0
mahasiswa_unggul = ""

for nim in data_nilai:
    daftar_nilai = data_nilai[nim]
    rata2 = sum(daftar_nilai) / len(daftar_nilai)

    if rata2 > nilai_tertinggi:
        nilai_tertinggi = rata2
        mahasiswa_unggul = data_mahasiswa[nim]

# Menghitung rata-rata tiap mata kuliah
jumlah_mk = len(next(iter(data_nilai.values())))
akumulasi_nilai = [0] * jumlah_mk

for daftar_nilai in data_nilai.values():
    for index, nilai in enumerate(daftar_nilai):
        akumulasi_nilai[index] += nilai

# Mencari mata kuliah dengan rata-rata terendah
rata_terendah = float("inf")
mk_terlemah = ""

for i, total in enumerate(akumulasi_nilai):
    rata_mk = total / len(data_nilai)

    if rata_mk < rata_terendah:
        rata_terendah = rata_mk
        mk_terlemah = f"Mata Kuliah {i+1}"

# Output hasil
print("\n=== HASIL ANALISIS NILAI ===")
print(f"Mahasiswa Terbaik : {mahasiswa_unggul} dengan rata-rata {nilai_tertinggi:.2f}")
print(f"Nilai Rata-rata Terendah ada pada {mk_terlemah} yaitu {rata_terendah:.2f}")

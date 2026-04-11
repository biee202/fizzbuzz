#Adli farabi (251011701039)

while True:
    print("\n===== PROGRAM OPERASI MATRIKS =====")
    print("1. Tambah Matriks")
    print("2. Kurang Matriks")
    print("3. Kali Matriks")
    print("0. Keluar Program")

    menu = input("Masukkan pilihan: ")

    if menu == "0":
        print("Program dihentikan.")
        break

    r = int(input("Jumlah baris: "))
    c = int(input("Jumlah kolom: "))

    print("\nMasukkan Matriks A")
    matriks_A = []
    for i in range(r):
        row = []
        for j in range(c):
            nilai = int(input(f"A[{i}][{j}] = "))
            row.append(nilai)
        matriks_A.append(row)

    print("\nMasukkan Matriks B")
    matriks_B = []
    for i in range(r):
        row = []
        for j in range(c):
            nilai = int(input(f"B[{i}][{j}] = "))
            row.append(nilai)
        matriks_B.append(row)

    hasil = []

    if menu == "1":
        print("\n>>> Proses Penjumlahan")
        for i in range(r):
            row = []
            for j in range(c):
                nilai = matriks_A[i][j] + matriks_B[i][j]
                print(f"A[{i}][{j}] + B[{i}][{j}] = {nilai}")
                row.append(nilai)
            hasil.append(row)

    elif menu == "2":
        print("\n>>> Proses Pengurangan")
        for i in range(r):
            row = []
            for j in range(c):
                nilai = matriks_A[i][j] - matriks_B[i][j]
                print(f"A[{i}][{j}] - B[{i}][{j}] = {nilai}")
                row.append(nilai)
            hasil.append(row)

    elif menu == "3":
        print("\n>>> Proses Perkalian")
        for i in range(r):
            row = []
            for j in range(c):
                jumlah = 0
                for k in range(c):
                    kali = matriks_A[i][k] * matriks_B[k][j]
                    print(f"A[{i}][{k}] x B[{k}][{j}] = {kali}")
                    jumlah += kali
                print(f"Hasil C[{i}][{j}] = {jumlah}")
                row.append(jumlah)
            hasil.append(row)

    print("\n=== HASIL AKHIR ===")
    for row in hasil:
        print(row)

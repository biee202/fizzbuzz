def main():
    while True:
        print("\n--- MENU NIM GANJIL ---")
        print("1. A pangkat B")
        print("2. Hitung Pecahan (12/35 + 8/13 + 21)")
        print("8. Keluar")
        
        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == '1':
           
            bilangan = int(input("Masukkan suatu bilangan bulat: "))
            pangkat_target = int(input("Masukkan pangkat yang diinginkan: "))
            
            for i in range(1, pangkat_target + 1):
                hasil = bilangan ** i
                print(f"Hasil {bilangan} pangkat {i} adalah {hasil}")

        elif pilihan == '2':
         
            hasil_pecahan = (12/35) + (8/13) + 21
            print(f"Hasil perhitungan adalah: {hasil_pecahan}")

        elif pilihan == '8':
            print("Keluar dari program...")
            break
        
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()

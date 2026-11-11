
# Program Penilaian Mahasiswa

print("=== PROGRAM NILAI UJIAN ===")

# Input nama mahasiswa
nama = input("Masukkan nama mahasiswa: ")

# Menentukan target nilai
if nama.lower() == "rudi":
    target = 80
elif nama.lower() == "ani":
    target = 75
elif nama.lower() == "dina":
    target = 85
else:
    print("Nama tidak terdaftar!")
    target = None

if target != None:
    print("Nama Mahasiswa:", nama)
    print("Target Nilai:", target)

    kesempatan = 1
    status = False

    while kesempatan <= 3:
        nilai = int(input("Masukkan nilai ujian: "))

        if nilai >= target:
            print("Nilai berhasil mencapai target!")
            status = True
            break
        else:
            print("Nilai masih kurang dari target.")
            print("Silakan mencoba lagi.")

        kesempatan += 1

    if status == True:
        print("SELAMAT, ANDA LULUS!")
    else:
        print("MAAF, ANDA TIDAK LULUS.")

print("=== PROGRAM SELESAI ===")

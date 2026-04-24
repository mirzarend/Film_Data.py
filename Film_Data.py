#pertanyaan pakai dictionary
pertanyaan = ["2 × 5 =", "4 × 8 =","7 × 9 ="]

#dictionary jawaban
jawaban = ["10","32","63"]

def semuaPertanyaan(pertanyaan) : #sebenarnya ga pakai def juga gapapa saya rasa
  print("="*30)
  print("Semua pertanyaan :")
  print(pertanyaan[0])
  print(pertanyaan[1])
  print(pertanyaan[2])
  print("="*30)

semuaPertanyaan(pertanyaan)

#input dan validasi
while True :
  try :
   pilihPertanyaan = int(input("Pilih pertanyaan 1-3 :"))
   if 1 <= pilihPertanyaan <= 3 :
     break
   else :
     print("harus angka 1-3")
  except :
    print("harus angka dan angka 1-3")

print("anda memilih pertanyaan ke -", pilihPertanyaan)

def tanyapertanyaan(pilihPertanyaan) :
  jawabanPertanyaan = input(pertanyaan[pilihPertanyaan -1] + ':')
  while True :
    if jawabanPertanyaan == jawaban[pilihPertanyaan - 1] :
      print("Benar!")
      break
    else :
      jawabanPertanyaan = input("Kurang tepat!, coba lagi :")

tanyapertanyaan(pilihPertanyaan)
  

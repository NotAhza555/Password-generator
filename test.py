import random
chars = "<>+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
print("Selamat datang di password generator, kamu bisa menggenerate password sesuai keinginanmu")
password = ""

pertanyaan = int(input("Berapa panjang kata sandi yang ingin kamu generate: "))

for i in range(pertanyaan):
     password = password + random.choice(chars)

print(password)
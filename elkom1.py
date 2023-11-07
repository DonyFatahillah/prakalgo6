print("\n \n")

print("@@@@   @@@@@   @@  @  @   @")
print("@   @  @   @   @ @ @   @ @")
print("@   @  @   @   @  @@    @")
print("@@@@   @@@@@   @   @    @")

print("\n \n")

print("GENAP ->  Perpindahan (diketahui v0 konstan)\n")

def hitung(v0, a, s):
    
    vt2 = v0 + 2 * a * s
    return vt2

v0 = float(input("Masukkan kecepatan awal (m/s) / v0 : "))
a = float(input("Masukkan percepatan (m/s^2) / a : "))
s = float(input("Masukkan jarak yang ditempuh (m) / s : "))

vt2 = hitung(v0, a, s)
print(f"Kecepatan akhir adalah {vt2} m/s")

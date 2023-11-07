

import os
import math


def banner():
    print("\n \n")

    print("@@@@   @@@@@   @@  @  @   @")
    print("@   @  @   @   @ @ @   @ @")
    print("@   @  @   @   @  @@    @")
    print("@@@@   @@@@@   @   @    @")

    print("\n \n")

def clear():
    os.system('cls' if os.name == "nt" else "clear")

def main():
    while True:
        banner()
        print("===KALKULATOR MENCARI LUAS===")
        print("1.) Kubus")
        print("2.) Balok")
        print("3.) Tabung")
        print("4.) Kerucut")
        print("5.) Bola")
        print("6.) Keluar")

        opsi = input(">>> ")
        if opsi.isdigit():
            if opsi == "1":
                clear()
                kubus()
                return exit, clear()
            elif opsi == "2":
                clear()
                balok()
                return exit, clear()
            elif opsi == "3":
                clear()
                tabung()
                return exit, clear()
            elif opsi == "4":
                clear()
                kerucut()
                return exit, clear()
            elif opsi == "5":
                clear()
                bola()
                return exit, clear()
            elif opsi == "6":
                return exit, clear()
            else:
                clear()
                continue
        elif opsi == "exit":
            return exit
        else:
            clear()
            continue

def kubus():
    while True:
        banner()
        print("===Menghitung Luas Kubus===")
        panjangSisi = input("Masukan panjang sisi >> ")
        if panjangSisi.isdigit():
            panjangSisi = int(panjangSisi)
            luasKubus = 6 * panjangSisi**2
            print(f"Luas Kubus adalah : {luasKubus}")
            opsi = input("lanjut menghitung?? (y/n) >> ").lower()
            if opsi == "y":
                clear()
                continue
            else:
                clear()
                return main()
        elif panjangSisi == "exit":
            clear()
            return main()
        else:
            clear()
            print("Masukan angka yang benar!")
            continue

def balok():
    while True:
        banner()
        print("===Menghitung Luas Balok===")
        panjang = input("Masukan Sisi Panjang >> ")
        if panjang.lower() == "exit":
            clear()
            return main()
        lebar = input("Masukan Sisi Lebar >> ")
        tinggi = input("Masukan Sisi Tinggi >> ")
        if (panjang and lebar and tinggi).isdigit():
            panjang, lebar, tinggi = (int(panjang), int(lebar), int(tinggi))
            if lebar < panjang:               
                luasBalok = ((2*panjang*lebar) + (2*lebar*tinggi) + (2*panjang*tinggi))
                print(f"Luas Balok adalah : {luasBalok}")
                opsi = input("Lanjut Menghitung? (y/n) : ").lower()
                if opsi == "y":
                    clear()
                    continue
                else:
                    clear()
                    return main()
            else:
                clear()
                print("Sisi Panjang harus lebih besar dari Sisi Lebar!")
                continue
        else:
            clear()
            print("Masukan angka yang benar!")
            continue

def tabung():
    while True:
        banner()
        print("===Menghitung Luas Tabung===")
        
        jariJari = input("Masukan Jari-Jari >> ")
        if jariJari == "exit":
            clear()
            return main()
        tinggi = input("Masukan Tinggi Tabung >> ")
        if (jariJari and tinggi).isdigit():
            jariJari, tinggi = int(jariJari), int(tinggi)
            luasTabung = (math.pi * jariJari**2) + ((2*math.pi*jariJari) * tinggi)
            print(f"Luas Tabung adalah : {luasTabung}")
            opsi = input("Lanjut Menghitung? (y/n) : ").lower()
            if opsi == "y":
                clear()
                continue
            else:
                clear()
                return main()
        else:
            clear()
            print("Masukan angka yang benar!")
            continue

def kerucut():
    while True:
        banner()
        print("===Menghitung Luas Kerucut===")
        
        jariJari = input("Masukan Jari Jari >> ")
        if jariJari == "exit":
            clear()
            return main()
        s = input("Masukan Garis Pelukis >> ")
        if (jariJari and s).isdigit():
            jariJari, s = int(jariJari), int(s)
            luasKerucut = (math.pi*jariJari*s) + (math.pi*jariJari*2)
            print(f"Luas Kerucut Adalah : {luasKerucut}")
            opsi = input("Lanjut Menghitung? (y/n) : ").lower()
            if opsi == "y":
                clear()
                continue
            else:
                clear()
                return main()
        else:
            clear()
            print("Masukan angka yang benar!")
            continue

def bola():
    while True:
        banner()
        print("===Menghitung Luas Bola===")
        
        jariJari = input("Masukan Jari Jari >> ")
        if jariJari == "exit":
            clear()
            return main()
        if jariJari.isdigit():
            jariJari = int(jariJari)
            luasBola = 4*math.pi*jariJari**2
            print(f"Luas Bola adalah : {luasBola}")
            opsi = input("Lanjut Menghitung? (y/n) : ").lower()
            if opsi == "y":
                clear()
                continue
            else:
                clear()
                return main()
        else:
            clear()
            print("Masukan angka yang benar!")
            continue
    
if __name__ == "__main__":
    clear()
    main()

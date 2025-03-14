import time
import json
import random
import queue
from datetime import datetime
from threading import Thread

# Inisialisasi antrian untuk komunikasi antar proses
absensi_queue = queue.Queue()
database_absensi = {}

# ANSI escape code untuk warna teks
BLUE = '\033[94m'
RESET = '\033[0m'

# Fungsi untuk mempublikasikan data absensi
def publish_absensi(employee_name, status, complexity):
    start_time = time.time()
    if status == "Masuk":
        if employee_name in database_absensi:
            print(f"{BLUE}{employee_name}{RESET} sudah absen masuk hari ini!")
            execution_time = time.time() - start_time
        else:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            database_absensi[employee_name] = {"Masuk": timestamp, "Keluar": None}
            print(f"{BLUE}{employee_name}{RESET} telah absen masuk pada {timestamp}")
            execution_time = time.time() - start_time
    elif status == "Keluar":
        if employee_name not in database_absensi:
            print(f"{BLUE}{employee_name}{RESET} belum absen masuk, silakan absen masuk terlebih dahulu!")
            execution_time = time.time() - start_time
        elif database_absensi[employee_name]["Keluar"] is not None:
            print(f"{BLUE}{employee_name}{RESET} sudah absen keluar hari ini!")
            execution_time = time.time() - start_time
        else:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            database_absensi[employee_name]["Keluar"] = timestamp
            print(f"{BLUE}{employee_name}{RESET} telah absen keluar pada {timestamp}")
            execution_time = time.time() - start_time
    
    print(f"Waktu eksekusi: {execution_time:.6f} detik\n")

# Fungsi untuk melihat data absensi
def lihat_data_absensi():
    if not database_absensi:
        print("Belum ada data absensi.")
    else:
        print("Data Absensi Karyawan:")
        for name, timestamps in database_absensi.items():
            masuk = timestamps["Masuk"]
            keluar = timestamps["Keluar"] if timestamps["Keluar"] else "Belum absen keluar"
            print(f"- {name}: Masuk {masuk}, Keluar {keluar}")
    print()

# Implementasi O(n^2)
def absen_on2(status):
    employee_name = input("Masukkan nama: ")
    publish_absensi(employee_name, status, "O(n^2)")

# Implementasi O(n log n)
def absen_onlogn(status):
    employee_name = input("Masukkan nama: ")
    publish_absensi(employee_name, status, "O(n log n)")

# Main Menu
if __name__ == "__main__":
    while True:
        print("Sistem Absensi Karyawan")
        print("1. Absen Masuk (O(n²))")
        print("2. Absen Masuk (O(n log n))")
        print("3. Absen Keluar")
        print("4. Lihat Data Absensi")
        print("5. Keluar")
        pilihan = input("Pilih menu: ")
        print()
        
        if pilihan == "1":
            absen_on2("Masuk")
        elif pilihan == "2":
            absen_onlogn("Masuk")
        elif pilihan == "3":
            absen_on2("Keluar")
        elif pilihan == "4":
            lihat_data_absensi()
        elif pilihan == "5":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid!\n")

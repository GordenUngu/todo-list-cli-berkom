import os
import time

list_tugas = []
list_deadline = []
list_status = [] 

def clear_terminal():
    time.sleep(0.25)
    os.system('cls' if os.name == 'nt' else 'clear')

def lanjut():
    input("[ENTER] untuk lanjut.")

def print_line(n):
    print("-"*n)

def pecah_format_tanggal(tanggal):
    pecahan_format = tanggal.split("-")

    return pecahan_format

def order_tasks():
    jumlah_tugas = len(list_tugas)

    for i in range(jumlah_tugas):
        for j in range(0, jumlah_tugas - i - 1):
            pecahan_deadline1 = pecah_format_tanggal(list_deadline[j])
            tanggal1 = pecahan_deadline1[0]
            bulan1 = pecahan_deadline1[1]
            tahun1 = pecahan_deadline1[2]
            deadline1 = tahun1 + bulan1 + tanggal1

            pecahan_deadline2 = pecah_format_tanggal(list_deadline[j+1])
            tanggal2 = pecahan_deadline2[0]
            bulan2 = pecahan_deadline2[1]
            tahun2 = pecahan_deadline2[2]
            deadline2 = tahun2 + bulan2 + tanggal2

            if (deadline1 > deadline2):
                temp_tanggal = list_deadline[j]
                list_deadline[j] = list_deadline[j+1]
                list_deadline[j+1] = temp_tanggal

                temp_tugas = list_tugas[j]
                list_tugas[j] = list_tugas[j+1]
                list_tugas[j+1] = temp_tugas

                temp_status = list_status[j]
                list_status[j] = list_status[j+1]
                list_status[j+1] = temp_status

def add_task():
    clear_terminal()

    print("-----MENU TAMBAH TUGAS-----")

    while(1):
        tugas = input("Masukkan nama tugas [EXIT = 0]: ")
        if (tugas == '0'):
            break
        deadline = input("Masukkan deadline tugas [DD-MM-YYYY]: ")

        list_tugas.append(tugas)
        list_deadline.append(deadline)
        list_status.append("ACTIVE")

    order_tasks()

    lanjut()

def output_tasks():
    clear_terminal()

    print("-----MENU DAFTAR TUGAS-----")

    jumlah_tugas = len(list_tugas)

    print("NOMOR | NAMA - DEADLINE - STATUS")
    print_line(25)

    for i in range(jumlah_tugas):
        print(f"{i+1}. {list_tugas[i]} - {list_deadline[i]} - {list_status[i]}")
    
    print_line(25)

def delete_task(cat):    
    if (cat == -1):
        clear_terminal()
        output_tasks()

        print("-----MENU HAPUS TUGAS-----")

        if (len(list_tugas) ==  0):
            print("Belum ada tugas untuk dihapus.")
            return
        id_hapus = int(input("Masukkan ID tugas yang akan dihapus: "))
    else:
        id_hapus = cat

    tugas_terhapus = list_tugas.pop(id_hapus)
    list_deadline.pop(id_hapus)
    list_status.pop(id_hapus)

    print(f"Sukses! tugas '{tugas_terhapus}' berhasil dihapus.")

    lanjut()

def edit_nama(idx):
    new_nama = input("Masukkan nama baru: ")
    nama_lama = list_tugas[idx]

    list_tugas[idx] = new_nama

    print(f"Berhasil update nama tugas: {nama_lama} -> {new_nama}")


def edit_deadline(idx):
    new_deadline = input("Masukkan deadline baru [DD-MM-YYYY]: ")
    deadline_lama = list_deadline[idx]

    list_deadline[idx] = new_deadline
    order_tasks()

    print(f"Berhasil update deadline tugas: {deadline_lama} -> {new_deadline}")

def edit_status(idx):
    new_status = input("Apakah tugas sudah selesai? [Y/N]: ")
    if(new_status.lower() == "y"):
        list_status[idx] = "INACTIVE"

    opsi_hapus_otomatis = input("Apakah tugas ingin dihapus otomatis? [Y/N]: ")

    if (opsi_hapus_otomatis.lower() == 'y'):
        delete_task(idx)

def edit_task():
    clear_terminal()
    output_tasks()

    print("-----MENU EDIT TUGAS-----")

    id_task = int(input("Masukkan nomor tugas yang ingin diedit: "))
    index_task = id_task - 1
    clear_terminal()

    properti_tugas = [list_tugas[index_task], list_deadline[index_task], list_status[index_task]]

    print("Properti tugas:")
    print(f"Nomor: {id_task}")
    print(f"Nama Tugas: {properti_tugas[0]}")
    print(f"Deadline Tugas: {properti_tugas[1]}")
    print(f"Status tugas: {properti_tugas[2]}")
    
    print_line(25)

    print("Opsi edit:")
    print("[1] Nama")
    print("[2] Deadline")
    print("[3] Status")
    print("[0] Exit")

    while (True):
        opsi_edit = int(input("Masukkan opsi edit: "))

        if (opsi_edit == 0):
            return
        elif (opsi_edit == 1):
            edit_nama(index_task)
        elif (opsi_edit == 2):
            edit_deadline(index_task)
        elif (opsi_edit == 3):
            edit_status(index_task)

def main_menu():
    print("Opsi Pilihan:")
    print("[1] Tambah Tugas")
    print("[2] Hapus Tugas")
    print("[3] Edit Tugas")
    print("[4] Cek Daftar Tugas")
    print("[0] exit")

def main_process():
    active = True

    while (active):
        clear_terminal()

        main_menu()

        choice = int(input("Masukkan opsi fitur: "))
        if (choice == 0):
            active = False
        elif (choice == 1):
            add_task()
        elif (choice == 2):
            delete_task(-1)
        elif (choice == 3):
            edit_task()
        elif (choice == 4):
            output_tasks()
            lanjut()


if __name__ == "__main__":
    main_process()
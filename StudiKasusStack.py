def cek_kurung_seimbang(ekspresi):
    stack = []
    
# Membuat kamus (dictionary) pasangan kurung tutup dan buka
    pasangan = {')': '(', ']': '[', '}': '{'}
    
    for karakter in ekspresi:
# Jika karakter adalah kurung buka, masukkan (push) ke stack
        if karakter in pasangan.values():
            stack.append(karakter)
            
# Jika karakter adalah kurung tutup
        elif karakter in pasangan.keys():

# 1. Cek apakah stack kosong (kurung tutup kelebihan)
            if not stack:
                print(f"[{ekspresi}] Error: Kurung tutup '{karakter}' tidak memiliki pembuka.")
                return False
                
# 2. Ambil (pop) kurung terakhir dan cocokkan jenisnya
            kurung_terakhir = stack.pop()
            if pasangan[karakter] != kurung_terakhir:
                print(f"[{ekspresi}] Error: Diharapkan '{pasangan[karakter]}', tapi mendapat '{kurung_terakhir}'.")
                return False

# Jika setelah dicek semua ternyata stack masih bersisa, berarti ada kurung yang belum ditutup
    if stack:
        print(f"[{ekspresi}] Error: Ada kurung buka yang belum ditutup.")
        return False
        
    print(f"[{ekspresi}] Valid: Tanda kurung seimbang.")
    return True

# --- UJI COBA STUDI KASUS ---

# 1. Kasus Valid (Seimbang)
cek_kurung_seimbang("{[()]}")

# 2. Kasus Beda Jenis (Bentuk penutup tidak cocok)
cek_kurung_seimbang("{ ( ] }")

# 3. Kasus Bersilang (Urutan penutupan salah)
cek_kurung_seimbang("{ [ } ]")

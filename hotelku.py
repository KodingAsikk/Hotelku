import streamlit as st

# Simpan data booking dalam list
bookings = []
MAX_KAMAR = 10

st.title("🏨 Aplikasi Hotelku")

menu = st.sidebar.selectbox("Menu", ["Lihat Booking", "Tambah Booking", "Ubah Booking", "Hapus Booking"])

# Validasi Nomor HP
def valid_nomor_hp(hp):
    return hp.isdigit() and 10 <= len(hp) <= 13

# Cek apakah tanggal sudah dipesan
def tanggal_sudah_dipesan(tanggal):
    return any(b["tanggal"] == tanggal for b in bookings)

# Lihat Booking
if menu == "Lihat Booking":
    st.subheader("📋 Daftar Booking Hotel")
    if not bookings:
        st.info("Belum ada booking.")
    for i, b in enumerate(bookings):
        st.write(
            f"{i}. 🛏️ Kamar {b['nomor_kamar']} | Nama: {b['nama']} | HP: {b['hp']} | Tanggal: {b['tanggal']} | Jam: {b['jam']}"
        )

# Tambah Booking
elif menu == "Tambah Booking":
    st.subheader("📝 Tambah Booking Baru")
    nama = st.text_input("Nama")
    hp = st.text_input("Nomor HP (10–13 digit)")
    tanggal = st.date_input("Tanggal")
    jam = st.time_input("Jam")

    if st.button("Tambah"):
        if len(bookings) >= MAX_KAMAR:
            st.error("Maaf Kamar Sudah Penuh!")
        elif tanggal_sudah_dipesan(str(tanggal)):
            st.error("Tanggal sudah tidak tersedia.")
        elif not valid_nomor_hp(hp):
            st.error("Nomor HP tidak valid!")
        elif not nama:
            st.warning("Nama harus diisi.")
        else:
            nomor_kamar = len(bookings) + 1
            bookings.append({
                "nama": nama,
                "hp": hp,
                "tanggal": str(tanggal),
                "jam": str(jam),
                "nomor_kamar": nomor_kamar
            })
            st.success(f"Booking berhasil. Nomor Kamar: {nomor_kamar}")

# Ubah Booking
elif menu == "Ubah Booking":
    st.subheader("✏️ Ubah Booking")
    index = st.number_input("Index booking", min_value=0, max_value=max(len(bookings)-1, 0), step=1)
    if bookings:
        nama = st.text_input("Nama baru")
        hp = st.text_input("Nomor HP baru")
        tanggal = st.date_input("Tanggal baru")
        jam = st.time_input("Jam baru")

        if st.button("Ubah"):
            if index < len(bookings):
                if str(tanggal) != bookings[index]["tanggal"] and tanggal_sudah_dipesan(str(tanggal)):
                    st.error("Tanggal sudah tidak tersedia.")
                elif not valid_nomor_hp(hp):
                    st.error("Nomor HP tidak valid!")
                else:
                    bookings[index] = {
                        "nama": nama,
                        "hp": hp,
                        "tanggal": str(tanggal),
                        "jam": str(jam),
                        "nomor_kamar": bookings[index]["nomor_kamar"]
                    }
                    st.success("Booking berhasil diubah.")
            else:
                st.error("Index booking tidak valid.")

# Hapus Booking
elif menu == "Hapus Booking":
    st.subheader("🗑️ Hapus Booking")
    index = st.number_input("Index booking", min_value=0, max_value=max(len(bookings)-1, 0), step=1)
    if st.button("Hapus"):
        if index < len(bookings):
            bookings.pop(index)
            st.success("Booking berhasil dihapus.")
        else:
            st.error("Index booking tidak valid.")

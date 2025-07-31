import streamlit as st

# Inisialisasi daftar booking di session_state
if "bookings" not in st.session_state:
    st.session_state.bookings = []

st.title("Aplikasi Booking Hotel")

menu = st.sidebar.selectbox("Pilih Menu", ["Tambah Booking", "Lihat Booking"])

if menu == "Tambah Booking":
    st.header("Tambah Booking Kamar")

    nama = st.text_input("Nama Lengkap")
    tanggal = st.date_input("Tanggal Menginap")
    kamar = st.selectbox("Pilih Kamar", [1, 2, 3, 4, 5])

    if st.button("Booking Sekarang"):
        # Simpan data booking ke session_state
        booking_baru = {
            "nama": nama,
            "tanggal": tanggal,
            "kamar": kamar
        }
        st.session_state.bookings.append(booking_baru)
        st.success(f"Booking berhasil! Kamu dapat kamar nomor {kamar}.")

elif menu == "Lihat Booking":
    st.header("Daftar Booking Hotel")

    if st.session_state.bookings:
        for i, b in enumerate(st.session_state.bookings, start=1):
            st.write(f"### Booking {i}")
            st.write(f"- Nama: {b['nama']}")
            st.write(f"- Tanggal: {b['tanggal']}")
            st.write(f"- Kamar: {b['kamar']}")
    else:
        st.info("Belum ada data booking.")

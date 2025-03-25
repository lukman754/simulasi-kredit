import streamlit as st

# Judul Aplikasi
st.title("Simulasi Kredit Pinjaman")

# Form Input
jumlah_pinjaman = st.number_input("Jumlah Dana yang Ingin Dipinjam (Rp)", min_value=0, value=1000000, step=100000)
tenor_bulan = st.number_input("Jumlah Tenor (bulan)", min_value=1, value=12, step=1)
bunga_persen = st.number_input("Bunga per Bulan (%)", min_value=0.0, value=2.0, step=0.1)

if st.button("Hitung Simulasi Kredit"):
    # Perhitungan
    jumlah_bunga_per_bulan = jumlah_pinjaman * (bunga_persen / 100)
    total_bunga = jumlah_bunga_per_bulan * tenor_bulan
    total_pembayaran = jumlah_pinjaman + total_bunga
    angsuran_per_bulan = total_pembayaran / tenor_bulan
    angsuran_per_hari = angsuran_per_bulan / 30
    angsuran_per_minggu = angsuran_per_bulan / 4

    # Menampilkan Hasil
    st.subheader("Hasil Simulasi Kredit")
    st.write(f"**Jumlah Pinjaman:** Rp {jumlah_pinjaman:,.0f}")
    st.write(f"**Total Bunga:** Rp {total_bunga:,.0f}")
    st.write(f"**Total Pembayaran:** Rp {total_pembayaran:,.0f}")
    st.write(f"**Angsuran per Bulan:** Rp {angsuran_per_bulan:,.0f}")
    st.write(f"**Angsuran per Minggu:** Rp {angsuran_per_minggu:,.0f}")
    st.write(f"**Angsuran per Hari:** Rp {angsuran_per_hari:,.0f}")

import streamlit as st
import locale

# Set locale to Indonesian for Rupiah formatting
locale.setlocale(locale.LC_ALL, 'id_ID.UTF-8')

def format_rupiah(amount):
    """Format angka ke dalam mata uang Rupiah"""
    try:
        return locale.currency(amount, grouping=True, symbol=True)
    except:
        # Fallback formatting if locale fails
        return f"Rp {amount:,.0f}"

def calculate_loan(principal, tenor, interest_rate):
    """Hitung simulasi kredit pinjaman"""
    # Hitung bunga
    monthly_interest = principal * (interest_rate / 100)
    total_interest = monthly_interest * tenor
    
    # Hitung total pinjaman
    total_amount = principal + total_interest
    
    # Hitung angsuran
    monthly_installment = total_amount / tenor
    weekly_installment = monthly_installment / 4
    daily_installment = monthly_installment / 30
    
    return {
        'monthly_interest': monthly_interest,
        'total_interest': total_interest,
        'total_amount': total_amount,
        'monthly_installment': monthly_installment,
        'weekly_installment': weekly_installment,
        'daily_installment': daily_installment
    }

def main():
    # Judul dan styling
    st.set_page_config(page_title="Kalkulator Simulasi Kredit", page_icon="💰", layout="wide")
    
    st.title("🏦 Kalkulator Simulasi Kredit Pinjaman")
    
    # Kolom input dengan styling
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # Input jumlah dana dengan format Rupiah
        principal = st.number_input(
            "Jumlah Dana yang Ingin Dipinjam", 
            min_value=1000000, 
            step=100000, 
            format="%d",
            help="Masukkan jumlah dana dalam Rupiah"
        )
    
    with col2:
        # Input tenor bulan
        tenor = st.number_input(
            "Tenor (Bulan)", 
            min_value=1, 
            max_value=60, 
            value=12,
            help="Pilih jangka waktu pinjaman dalam bulan"
        )
    
    with col3:
        # Input bunga
        interest_rate = st.number_input(
            "Bunga (%)", 
            min_value=0.1, 
            max_value=50.0, 
            value=5.0, 
            step=0.1,
            help="Masukkan tingkat bunga per tahun"
        )
    
    # Tombol hitung
    if st.button("Hitung Simulasi Kredit", type="primary"):
        # Lakukan perhitungan
        result = calculate_loan(principal, tenor, interest_rate)
        
        # Tampilkan hasil dengan kartu
        st.subheader("Hasil Simulasi Kredit")
        
        cols = st.columns(3)
        
        with cols[0]:
            st.info(f"**Bunga Bulanan**\n{format_rupiah(result['monthly_interest'])}")
        
        with cols[1]:
            st.info(f"**Total Bunga**\n{format_rupiah(result['total_interest'])}")
        
        with cols[2]:
            st.info(f"**Total Pinjaman**\n{format_rupiah(result['total_amount'])}")
        
        # Tabel rincian angsuran
        st.subheader("Rincian Angsuran")
        
        angsuran_data = {
            "Jenis Angsuran": ["Bulanan", "Mingguan", "Harian"],
            "Nominal": [
                format_rupiah(result['monthly_installment']),
                format_rupiah(result['weekly_installment']),
                format_rupiah(result['daily_installment'])
            ]
        }
        
        st.table(angsuran_data)
        
        # Grafik sederhana
        st.subheader("Grafik Perbandingan")
        st.bar_chart({
            'Pokok Pinjaman': principal, 
            'Total Bunga': result['total_interest'], 
            'Total Pembayaran': result['total_amount']
        })

if __name__ == "__main__":
    main()

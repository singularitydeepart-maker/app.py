import streamlit as st

st.set_page_config(page_title="Reklam Karar Paneli", layout="wide")

st.title("Trendyol Reklam Karar Paneli")

# INPUTLAR
col1, col2, col3 = st.columns(3)

with col1:
    satis = st.number_input("Satış Fiyatı", value=1000.0)
    maliyet = st.number_input("Maliyet", value=400.0)
    komisyon = st.number_input("Komisyon (%)", value=20.0)

with col2:
    kargo = st.number_input("Kargo", value=50.0)
    vergi = st.number_input("Vergi (%)", value=20.0)
    iade = st.number_input("İade Oranı (%)", value=5.0)

with col3:
    reklam = st.number_input("Toplam Reklam Harcaması", value=1000.0)
    reklam_ciro = st.number_input("Reklam Cirosu", value=3000.0)
    adet = st.number_input("Satış Adedi", value=10.0)

# HESAPLAMA
if st.button("HESAPLA"):

    komisyon_tutar = satis * komisyon / 100
    vergi_tutar = satis * vergi / 100
    iade_kargo = (iade / 100) * (kargo / 2)

    rek_adet = reklam_ciro / satis if satis > 0 else 0
    rek_basi = reklam / rek_adet if rek_adet > 0 else 0

    birim_kar = satis - maliyet - komisyon_tutar - kargo - vergi_tutar - iade_kargo
    birim_kar_reklamli = birim_kar - rek_basi

    toplam_kar = (birim_kar * adet) - reklam
    roas = reklam_ciro / reklam if reklam > 0 else 0

    # KARAR
    if birim_kar_reklamli > 0:
        karar = "AÇIK TUT"
        renk = "green"
    elif birim_kar_reklamli > -5:
        karar = "AZALT"
        renk = "orange"
    else:
        karar = "KAPAT"
        renk = "red"

    # SONUÇLAR
    st.subheader("Sonuçlar")

    colA, colB, colC = st.columns(3)

    colA.metric("Birim Kar (Reklamsız)", f"{birim_kar:.2f} TL")
    colB.metric("Birim Kar (Reklamlı)", f"{birim_kar_reklamli:.2f} TL")
    colC.metric("ROAS", f"{roas:.2f}x")

    st.metric("Toplam Kar", f"{toplam_kar:.2f} TL")

    st.markdown(f"### Karar: <span style='color:{renk}'>{karar}</span>", unsafe_allow_html=True)

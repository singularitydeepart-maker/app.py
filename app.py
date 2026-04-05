import streamlit as st
import json
import os

DOSYA = "data.json"

def veri_yukle():
    if not os.path.exists(DOSYA):
        return []
    with open(DOSYA, "r") as f:
        return json.load(f)

def veri_kaydet(data):
    with open(DOSYA, "w") as f:
        json.dump(data, f)

def hesapla(u):
    satis = float(u["satis"])
    maliyet = float(u["maliyet"])
    kom = float(u["kom"]) / 100
    kargo = float(u["kargo"])
    reklam = float(u["reklam"])
    ciro = float(u["ciro"])

    komisyon = satis * kom
    rek_adet = ciro / satis if satis > 0 else 0
    rek_basi = reklam / rek_adet if rek_adet > 0 else 0

    kar = satis - maliyet - komisyon - kargo
    kar_rekli = kar - rek_basi

    if kar_rekli > 0:
        return kar_rekli, "AÇIK TUT"
    elif kar_rekli > -5:
        return kar_rekli, "AZALT"
    else:
        return kar_rekli, "KAPAT"

# DATA
if "urunler" not in st.session_state:
    st.session_state.urunler = veri_yukle()

st.title("URRENN Maliye Paneli")

# ÜRÜN EKLE
with st.expander("Ürün Ekle"):
    urun = st.text_input("Ürün Adı")
    set_adi = st.text_input("Set Adı")
    satis = st.number_input("Satış", value=1000.0)
    maliyet = st.number_input("Maliyet", value=400.0)
    kom = st.number_input("Komisyon %", value=20.0)
    kargo = st.number_input("Kargo", value=50.0)
    reklam = st.number_input("Reklam", value=1000.0)
    ciro = st.number_input("Reklam Ciro", value=3000.0)

    if st.button("Ekle"):
        st.session_state.urunler.append({
            "urun": urun,
            "set": set_adi,
            "satis": satis,
            "maliyet": maliyet,
            "kom": kom,
            "kargo": kargo,
            "reklam": reklam,
            "ciro": ciro
        })
        veri_kaydet(st.session_state.urunler)
        st.success("Eklendi")

# TABLO
st.subheader("Ürünler")

toplam_kar = 0
ac = 0
kapat = 0

for u in st.session_state.urunler:
    kar, karar = hesapla(u)

    toplam_kar += kar

    if karar == "AÇIK TUT":
        ac += 1
        renk = "green"
    elif karar == "KAPAT":
        kapat += 1
        renk = "red"
    else:
        renk = "orange"

    st.markdown(f"""
    **{u['urun']} ({u['set']})**  
    Kar: {kar:.2f} TL  
    Karar: <span style='color:{renk}'>{karar}</span>
    """, unsafe_allow_html=True)

# DASHBOARD
st.divider()

col1, col2, col3 = st.columns(3)

col1.metric("Toplam Kar", f"{toplam_kar:.2f} TL")
col2.metric("Açık", ac)
col3.metric("Kapat", kapat)

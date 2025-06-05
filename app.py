import streamlit as st
import pandas as pd
from utils.email_sender import send_announcement
from utils.task_manager import display_tasks
from utils.ai_agent import get_answer

st.set_page_config(page_title="Akademik Asistan", layout="wide")

st.title("📚 Akademik İletişim Asistanı")

# 1. Öğrenci listesi yükleme
st.sidebar.header("👥 Öğrenci Listesi Yükle")
uploaded_file = st.sidebar.file_uploader("CSV Dosyası Seç", type=["csv"])

if uploaded_file:
    df_students = pd.read_csv(uploaded_file)
    st.success("✅ Öğrenci listesi yüklendi.")
    st.dataframe(df_students)

    # 2. Duyuru gönderme
    st.subheader("📢 Duyuru Gönder")
    subject = st.text_input("Konu")
    message = st.text_area("Mesaj")
    if st.button("Duyuruyu Gönder"):
        send_announcement(df_students, subject, message)
        st.success("📨 Duyuru başarıyla gönderildi.")

    # 3. Görev takibi
    st.subheader("📝 Görev Takibi")
    display_tasks(df_students)

    # 4. AI Asistan
    st.subheader("🤖 AI Soru-Cevap Asistanı")
    user_question = st.text_input("Sorunuzu yazın:")
    if user_question:
        answer = get_answer(user_question)
        st.info(f"Cevap: {answer}")
else:
    st.warning("Lütfen önce bir öğrenci listesi yükleyin (CSV).")

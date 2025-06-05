import streamlit as st
import pandas as pd

def display_tasks(df_students):
    st.write("📋 Öğrenci Görev Listesi")

    for index, row in df_students.iterrows():
        st.markdown(f"**👤 {row['name']} ({row['email']})**")
        
        # Öğrenciye özel görevler (şu anlık örnek sabit)
        tasks = [
            {"görev": "1. Ödev teslimi", "tarih": "2025-06-15"},
            {"görev": "Ara sınav", "t

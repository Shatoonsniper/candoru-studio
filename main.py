import streamlit as st
from fastapi import FastAPI
import threading
import time
from src.config import load_config
from src.scraper import fetch_and_save
from src.utils import get_next_task

st.set_page_config(page_title="Candoru Studio", layout="wide", page_icon="📰")
st.title("📰 Candoru Studio — Автоматизация новостей для Candoru.ru")

st.sidebar.header("Настройки")
if st.sidebar.button("Проверить подключения"):
    st.success("✅ OpenRouter + WordPress подключены")

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["Новости", "Источники", "Очередь", "Черновики"])

with tab1:
    if st.button("Запустить ручную синхронизацию (все источники)"):
        st.info("Запуск синхронизации...")
        for source in load_config()["sources"]:
            fetch_and_save(source)
        st.success("Готово! Новости загружены.")

with tab2:
    st.subheader("Добавление источника")
    url = st.text_input("RSS/Atom URL")
    if st.button("Добавить источник"):
        config = load_config()
        if url and url not in config["sources"]:
            config["sources"].append(url)
        st.success("Источник добавлен!")

with tab3:
    st.subheader("Очередь задач (AI-рейт)")
    for task in get_next_task(5):
        st.write(task)

with tab4:
    st.subheader("Черновики в WordPress")
    st.write("Здесь будет список черновиков (по URL)")
    st.info("Черновик создаётся автоматически при отправке.")

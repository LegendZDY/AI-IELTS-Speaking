import streamlit as st
import time
import uuid
from utils.tools import wav_to_pcm
from utils.tts import tts_wav_get
from utils.iat import iat_message_get
from utils.Chat import get_chat_anwser

st.set_page_config(
    page_title="AI-IELTS-Speaking",
    page_icon=":material/chat:",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "About": "# AI-IELTS-Speaking",
    },
)

col1, col2 = st.columns([0.65, 0.35])
with col1:
    with st.container(height=380):
        # List of image file paths
        image_files = [
            'static/1.png',
            'static/2.png',
            'static/3.png',
            'static/4.png',
            'static/5.png',
            'static/6.png',
        ]
        st.image(image_files[st.session_state.images_count], width=550)
        
    with st.container(height=103):
        from audiorecorder import audiorecorder
        audio = audiorecorder("Start", "Stop")

with col2:
    with st.container(height=500):
        st.title("💬 Chatbot")
        st.caption("🚀 A AI-IELTS-Speaking chatbot")
        if 'message_count' not in st.session_state:
            st.session_state.message_count = 0
        if "messages" not in st.session_state:
            st.session_state["messages"] = [{"role": "assistant", "content": ["first", "./data/start.wav"]}]
            time.sleep(1)
            
        for msg in st.session_state.messages:
            if msg["content"][0] == "first":
                st.chat_message(msg["role"]).audio(msg["content"][1], autoplay=True)
                st.write("Hello, I am your English speaking assistant. Nice to meet you here. Today, we will discuss the topic according to the card content. First, please briefly introduce yourself?")
            elif msg["content"][0] == "audio":
                st.chat_message(msg["role"]).audio(msg["content"][1], autoplay=False)
            elif msg["content"][0] == "message":
                st.chat_message(msg["role"]).write(msg["content"][1])
            elif msg["content"][0] == "image":
                st.chat_message(msg["role"]).image(msg["content"][1])
            else:
                exit 
            
        if len(audio) > 0:
            id = uuid.uuid4().hex
            wav_name_q = "q" + id + ".wav"
            pcm_name = "q" + id + ".pcm"
            wav_path_q = "./data/" + wav_name_q
            pcm_path = "./data/" + pcm_name
            audio.export(wav_path_q, format="wav")
            wav_to_pcm(wav_path_q, pcm_path)
            iat_message = iat_message_get(pcm_name)
            st.session_state.messages.append({"role": "user", "content": ["audio", wav_path_q]})
            st.chat_message("user").audio(wav_path_q, autoplay=True)
            st.write(iat_message)
            anwser=get_chat_anwser(iat_message, st.session_state.message_count)
            wav_name_a = "a" + id + ".wav"
            tts_wav_get(anwser, wav_name_a)
            wav_path_a="./data/" + wav_name_a
            st.session_state.messages.append({"role": "assistant", "content": ["audio", wav_path_a]})
            st.chat_message("assistant").audio(wav_path_a, autoplay=True)
            st.write(anwser)     
            st.session_state.message_count += 1
            
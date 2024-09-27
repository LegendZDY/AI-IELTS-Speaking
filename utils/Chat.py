import streamlit as st
from sparkai.frameworks.autogen import SparkAI
import autogen
import types
from tools import model_message_get


model_messages=model_message_get("./config/model_messages.json")

spark_config = autogen.config_list_from_json(
    "./config/sparkai_autogen.json",
    filter_dict={"model_client_cls": ["SparkAI"]},
)

llm_config = {
    "timeout": 600,
    "cache_seed": None,  # change the seed for different trials
    "config_list": spark_config,
    "temperature": 0.8,
}

EnglishTeacher = autogen.AssistantAgent(
    "EnglishTeacher",
    system_message=model_messages[st.session_state.images_count],
    llm_config=llm_config,
    human_input_mode="NEVER",
)
EnglishTeacher.register_model_client(model_client_cls=SparkAI)

user_proxy = autogen.UserProxyAgent(
    "user_proxy",
    code_execution_config=False
)

def st_get_human_input(self, prompt: str) -> str:
    # iostream = IOStream.get_default()
    global user_msg2send
    reply = user_msg2send
    self._human_input.append(reply)
    return reply
user_proxy.get_human_input = types.MethodType(st_get_human_input, user_proxy)

def get_chat_anwser(message, counter):
    global user_msg2send
    user_msg2send=message
    if counter == 0:
        msg2send = user_proxy.generate_init_message(message=message)
        user_proxy.send(msg2send, EnglishTeacher, request_reply=True, silent=False)
        bot_message = EnglishTeacher.chat_messages[user_proxy][-1]['content']
        counter += 1
    else:
        msg2send = user_proxy.generate_reply(messages=user_proxy.chat_messages[EnglishTeacher], sender=EnglishTeacher)
        user_proxy.send(msg2send, EnglishTeacher, request_reply=True, silent=False)
        bot_message = EnglishTeacher.chat_messages[user_proxy][-1]['content']
        counter += 1
    return bot_message
import streamlit as st
import SparkApi
from sparkai.llm.llm import ChatSparkLLM, ChunkPrintHandler
from sparkai.core.messages import ChatMessage

st.set_page_config(
    page_title="AI-IELTS-Speaking",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "About": "# AI-IELTS-Speaking",
    },
)


#以下密钥信息从控制台获取
appid = "8ee35cb8"     #填写控制台中获取的 APPID 信息
api_secret = "ZThlMjg5ZDZlZTQwNWIxYjFlOTU2MDI2"   #填写控制台中获取的 APISecret 信息
api_key ="e9eae764ffcc3835f4a893d5b91b3da5"    #填写控制台中获取的 APIKey 信息

#调用微调大模型时，设置为“patch”
domain = "patch"

#云端环境的服务地址
Spark_url = "wss://spark-api-n.xf-yun.com/v1.1/chat"  # 微调v1.5环境的地址
# Spark_url = "wss://spark-api-n.xf-yun.com/v3.1/chat"  # 微调v3.0环境的地址


st.title("💬 Chatbot")
st.caption("🚀 A AI-IELTS-Speaking chatbot")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Hello, I am your IELTS speaking chatbot. Can you briefly introduce yourself??"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# spark = ChatSparkLLM(
#     spark_api_url=SPARKAI_URL,
#     spark_app_id=SPARKAI_APP_ID,
#     spark_api_key=SPARKAI_API_KEY,
#     spark_api_secret=SPARKAI_API_SECRET,
#     spark_llm_domain=SPARKAI_DOMAIN,
#     streaming=False,
#     )

# handler = ChunkPrintHandler()



def getText(role,content):
    jsoncon = {}
    jsoncon["role"] = role
    jsoncon["content"] = content
    text.append(jsoncon)
    return text
def getlength(text):
    length = 0
    for content in text:
        temp = content["content"]
        leng = len(temp)
        length += leng
    return length

def checklen(text):
    while (getlength(text) > 8000):
        del text[0]
    return text

if prompt := st.chat_input():
    text =[]
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    # spark_messages = [ChatMessage(
    #     role="user",
    #     content=prompt
    #     )]
    question = checklen(getText("user",prompt))
    response = SparkApi.main(appid,api_key,api_secret,Spark_url,domain,question)
    msg = getText("assistant",SparkApi.answer)[1].get("content")
    # print(msg)
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
    # text =[]
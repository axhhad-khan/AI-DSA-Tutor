import streamlit as st
from collections import deque
import datetime
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "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")

st.set_page_config(
    page_title="DSA Disco DSA Tutor | Premium Edition",
    page_icon="🎓",
    layout="wide",
)

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        color: #ffffff;
    }
    .stChatMessage {
        background-color: rgba(255, 255, 255, 0.05) !important;
        border-radius: 12px !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
    }
    .complexity-badge {
        background: linear-gradient(90deg, #ff4b1f, #ff9068);
        padding: 2px 8px;
        border-radius: 5px;
        font-size: 0.8rem;
        font-weight: bold;
    }
    .stButton>button {
        border-radius: 10px;
        background: linear-gradient(135deg, #00c6ff, #0072ff);
    }
</style>
""", unsafe_allow_html=True)

class Node:
    def __init__(self, data, sender, timestamp):
        self.data = data
        self.sender = sender
        self.timestamp = timestamp
        self.next = None

class ChatLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def add_message(self, data, sender, timestamp):
        new_node = Node(data, sender, timestamp)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        self.count += 1

    def delete_last(self):
        if self.head is None: return None
        if self.head.next is None:
            msg = self.head; self.head = None
            self.count -= 1; return msg
        temp = self.head
        while temp.next.next: temp = temp.next
        msg = temp.next; temp.next = None
        self.count -= 1; return msg

    def get_all_messages(self):
        messages = []
        temp = self.head
        while temp:
            messages.append({"data": temp.data, "sender": temp.sender, "timestamp": temp.timestamp})
            temp = temp.next
        return messages

if "chat_list" not in st.session_state: st.session_state.chat_list = ChatLinkedList()
if "message_queue" not in st.session_state: st.session_state.message_queue = deque()
if "username" not in st.session_state: st.session_state.username = "Student"

def get_dsa_tutor_response(user_query):
    try:
        client = Groq(api_key=GROQ_API_KEY)
        system_prompt = """
        You are 'DSA Disco DSA Tutor', an world-class expert in Data Structures and Algorithms.
        Your goal is to help students learn DSA in a simple, smart, and accurate way.
        Guidelines:
        1. Always explain 'Time' and 'Space' complexity (Big O).
        2. Use clear analogies for difficult concepts.
        3. Provide optimized Python code snippets if requested.
        4. Be encouraging and concise.
        5. Structure your answer with clear headings.
        """
        
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_query}
            ],
            temperature=0.7,
            max_tokens=1024,
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}. Please check the internal API configuration."

with st.sidebar:
    st.title("🎓 DSA Disco DSA Tutor")
    st.success("🤖 AI Engine: Active")
    st.info("System optimized for DSA Learning.")
    
    st.markdown("---")
    st.subheader("🛠 Controls")
    if st.button("🗑 Clear Chat History"):
        st.session_state.chat_list = ChatLinkedList()
        st.rerun()

    st.markdown("---")
    st.subheader("📊 Live DSA Metrics")
    st.info(f"Nodes in History (Linked List): {st.session_state.chat_list.count}")

st.title("📚 Intelligent DSA Learning Hub")
st.markdown("Ask any DSA question! *Powered by Llama 3.3 70B*")

messages = st.session_state.chat_list.get_all_messages()
for msg in messages:
    is_user = msg["sender"] == st.session_state.username
    with st.chat_message("user" if is_user else "assistant", avatar="👨‍🎓" if is_user else "🤖"):
        st.markdown(f"**{msg['sender']}**")
        st.write(msg["data"])

prompt = st.chat_input("Ex: Explain QuickSort vs MergeSort with Complexity")

if prompt:
    ts = datetime.datetime.now().strftime("%H:%M")
    st.session_state.chat_list.add_message(prompt, st.session_state.username, ts)
    
    with st.spinner("Analyzing with DSA Disco Engine..."):
        ai_resp = get_dsa_tutor_response(prompt)
        st.session_state.chat_list.add_message(ai_resp, "DSA Disco Tutor", ts)
    
    st.rerun()

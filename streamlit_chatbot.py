import streamlit as st
from chatbot_backend import gph
from langchain.messages import HumanMessage


CONFIG={"configurable":{'thread_id':'thread-1'}}

if "messages_history" not in st.session_state:
    st.session_state['messages_history']=[]

for message in st.session_state['messages_history']:
    with st.chat_message(message['role']):
        st.text(message['value'])




input=st.chat_input('TYPE HERE......')

if input:
    st.session_state['messages_history'].append({'role':'user','value':input})
    with st.chat_message('user'):
        st.text(input)
    
    ai_answer=gph.invoke({'messages':[HumanMessage(content=input)]},config=CONFIG)
    
    res=ai_answer['messages'][-1].content
    

    st.session_state['messages_history'].append({'role':'assistant','value':res})
    with st.chat_message('assistant'):
        st.text(res)
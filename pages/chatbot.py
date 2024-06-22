import json
import time
import os
from services import bedrock_agent_runtime
from dotenv import load_dotenv
import streamlit as st
import uuid

hide_sidebar_style = """
    <style>
        [data-testid="stSidebar"] {
            display: none;
        }
        [data-testid="stSidebarNav"] {
            display: none;
        }
        [data-testid="collapsedControl"] {
            display: none;
        }
    </style>
"""
st.markdown(hide_sidebar_style, unsafe_allow_html=True)

# Get config from environment variables
load_dotenv('.env')
agent_id = os.getenv('agent_id')
agent_alias_id = os.getenv('agentAliasId')
ui_title = os.environ.get("BEDROCK_AGENT_TEST_UI_TITLE", "NIRVITA, AI Dermatologist Assistant")
ui_icon = os.environ.get("BEDROCK_AGENT_TEST_UI_ICON")

def init_state():
    st.session_state.session_id = str(uuid.uuid4())
    st.session_state.messages = []
    st.session_state.citations = []
    st.session_state.trace = {}
    st.session_state.input_disabled = False
    st.session_state.processing = False

def show_chatbot():
    st.title(ui_title)
    if 'session_id' not in st.session_state:
        init_state()
  
    columns = st.columns((1, 2, 1))
    home_button = columns[0].button('Back to Main Page')
    end_button = columns[2].button('Reset Session')

    if home_button:
        st.switch_page("app.py")

    if end_button:
        init_state()

    # Messages in the conversation
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"], unsafe_allow_html=True)

    # Chat input that invokes the agent
    chat_input = st.chat_input(disabled=st.session_state.input_disabled or st.session_state.processing)
    
    if chat_input:
        st.session_state.messages.append({"role": "user", "content": chat_input})
        with st.chat_message("user"):
            st.write(chat_input)

        st.session_state.processing = True  # Disable the input
        st.session_state.input_disabled = True
        st.experimental_rerun()

    if st.session_state.processing:
        with st.chat_message("assistant"):
            placeholder = st.empty()
            placeholder.markdown("...")

            response = bedrock_agent_runtime.invoke_agent(
                agent_id,
                agent_alias_id,
                st.session_state.session_id,
                st.session_state.messages[-1]['content']
            )

            output_text = response["output_text"]

            # Add citations
            if len(response["citations"]) > 0:
                citation_num = 1
                num_citation_chars = 0
                citation_locs = ""
                for citation in response["citations"]:
                    end_span = citation["generatedResponsePart"]["textResponsePart"]["span"]["end"] + 1
                    for retrieved_ref in citation["retrievedReferences"]:
                        citation_marker = f"[{citation_num}]"
                        output_text = output_text[:end_span + num_citation_chars] + citation_marker + output_text[end_span + num_citation_chars:]
                        citation_locs = citation_locs + "\n<br>" + citation_marker + " " + retrieved_ref["location"]["s3Location"]["uri"]
                        citation_num = citation_num + 1
                        num_citation_chars = num_citation_chars + len(citation_marker)
                    output_text = output_text[:end_span + num_citation_chars] + "\n" + output_text[end_span + num_citation_chars:]
                    num_citation_chars = num_citation_chars + 1
                output_text = output_text + "\n" + citation_locs

            placeholder.markdown(output_text, unsafe_allow_html=True)
            st.session_state.messages.append({"role": "assistant", "content": output_text})
            st.session_state.citations = response["citations"]
            st.session_state.trace = response["trace"]

            st.session_state.processing = False  # Re-enable the input
            st.session_state.input_disabled = False
            st.experimental_rerun()

show_chatbot()

import streamlit as st
import replicate
import os
from pdfminer.high_level import extract_text
import pytesseract
from pdf2image import convert_from_bytes
import openai

from io import BytesIO

#PDF Reader Code:
def extract_text_with_fallback():
    file_bytes = uploaded_file.read()
    # Versuchen Sie zuerst, Text mit PDFMiner zu extrahieren
    try:
        # Erstellen Sie ein BytesIO-Objekt aus Ihren PDF-Bytes
        pdf_data = BytesIO(file_bytes)
        text = extract_text(pdf_data)
        if text.strip():  # Wenn der extrahierte Text nicht leer ist
            return text
    except:
        pass
    
    # Wenn das obige fehlschlägt oder keinen Text extrahiert, dann wird OCR geutzt (Bild KI)
    images = convert_from_bytes(file_bytes)
    extracted_texts = []
    with st.spinner('Lädt...'):
        for image in images:
            extracted_text = pytesseract.image_to_string(image)
            extracted_texts.append(extracted_text)
    return " ".join(extracted_texts)




# App Titel
st.set_page_config(page_title="📁💬 PDF Chatbot")

# Funktion für LLaMA2-Antwort
def generate_llama2_response(prompt_input):
    string_dialogue = "You are a helpful assistant. You do not respond as 'User' or pretend to be 'User'. You only respond once as 'Assistant'."
    for dict_message in st.session_state.messages:
        if dict_message["role"] == "user":
            string_dialogue += "User: " + dict_message["content"] + "\n\n"
        else:
            string_dialogue += "Assistant: " + dict_message["content"] + "\n\n"
    output = replicate.run(llm, 
                           input={"prompt": f"{string_dialogue} {prompt_input} Assistant: ",
                                  "temperature":temperature, "top_p":top_p, "max_length":max_length, "repetition_penalty":1})
    return output

# API Token
with st.sidebar:
    st.title('📁💬 PDF Chatbot')
    if 'REPLICATE_API_TOKEN' in st.secrets:
        st.success('API key already provided!', icon='✅')
        replicate_api = st.secrets['REPLICATE_API_TOKEN']['my_api_token']
    else:
        replicate_api = st.text_input('Enter Replicate API token:', type='password')
        if not (replicate_api.startswith('r8_') and len(replicate_api)==40):
            st.warning('Please enter your credentials!', icon='⚠️')
        else:
            st.success('Proceed to entering your prompt message!', icon='👉')

    # Midellauswahl
    st.subheader('Models and parameters')
    selected_model = st.sidebar.selectbox('Choose a Llama2 model', ['Llama2-7B', 'Llama2-13B', 'Llama2-70B'], key='selected_model')
    if selected_model == 'Llama2-7B':
        llm = 'a16z-infra/llama7b-v2-chat:4f0a4744c7295c024a1de15e1a63c880d3da035fa1f49bfd344fe076074c8eea'
    elif selected_model == 'Llama2-13B':
        llm = 'a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5'
    else:
        llm = 'replicate/llama70b-v2-chat:e951f18578850b652510200860fc4ea62b3b16fac280f83ff32282f87bbd2e48'
    
    temperature = st.sidebar.slider('temperature', min_value=0.01, max_value=5.0, value=0.1, step=0.01)
    top_p = st.sidebar.slider('top_p', min_value=0.01, max_value=1.0, value=0.9, step=0.01)
    max_length = st.sidebar.slider('max_length', min_value=64, max_value=4096, value=512, step=8)

    # PDF
    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

    if uploaded_file:
        text = extract_text_with_fallback()
        st.write("File uploaded successfully!")

        compexity = st.sidebar.selectbox('Zusammenfassung Komplexität', ['Wirtschaftlich', 'Technisch', 'Stark zusammengefasst'], key='compexity')
        if compexity == 'Wirtschaftlich':
            complex_text= 'a\n Summerize for a economic person'
        elif compexity == 'Technisch':
            complex_text = '\n Summerize in a technical way'
        else:
            complex_text = "\n Summerize this very short"
    
        if st.button('Summerize PDF'):
            prompt = text+complex_text
            st.session_state.messages.append({"role": "user", "content": prompt})
        
        if st.button('Text Anzeigen'):
            st.write(text)



os.environ['REPLICATE_API_TOKEN'] = replicate_api

# Speichern der LLM-generierten Antworten
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

# Chatnachrichten anzeigen oder löschen
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]
st.sidebar.button('Clear Chat History', on_click=clear_chat_history)



# Benutzer prompt
if prompt := st.chat_input(disabled=not replicate_api):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)



# Generieren einer neue Antwort, wenn die letzte Nachricht nicht vom Assistenten stammt
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = generate_llama2_response(prompt)
            placeholder = st.empty()
            full_response = ''
            for item in response:
                full_response += item
                placeholder.markdown(full_response)
            placeholder.markdown(full_response)
    message = {"role": "assistant", "content": full_response}
    st.session_state.messages.append(message)


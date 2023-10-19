import streamlit as st
import replicate
import os
from pdfminer.high_level import extract_text
import pytesseract
from pdf2image import convert_from_bytes
import openai
from io import BytesIO
import requests
from bs4 import BeautifulSoup
import re
import time
import tiktoken

# Cost Calculator
def num_tokens_from_string(string: str, encoding_name: str) -> int:
    encoding = tiktoken.encoding_for_model(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

def cost_calculator(elapsed_times,res):
    if 'gpt' in llm:
        input = ''.join(f"{key}{value}" for d in st.session_state.messages for key, value in d.items())
        anzahl_input = num_tokens_from_string(input, llm)
        print(anzahl_input)
        output = res["choices"][0]["message"]["content"]
        anzahl_output = num_tokens_from_string(output, llm)
        if llm == 'gpt-4':
            cost = ((0.03/1000)*anzahl_input)+((0.06/1000)*anzahl_output)
        elif llm == 'gpt-3.5-turbo':
            cost = ((0.0015/1000)*anzahl_input)+((0.002/1000)*anzahl_output)
        elif llm == 'gpt-3.5-turbo-16k':
            cost = ((0.003/1000)*anzahl_input)+((0.004/1000)*anzahl_output)
        else:
            cost = ((0.06/1000)*anzahl_input)+((0.12/1000)*anzahl_output)
    else:
        if llm == 'a16z-infra/llama7b-v2-chat:4f0a4744c7295c024a1de15e1a63c880d3da035fa1f49bfd344fe076074c8eea':        
            cost = elapsed_times*(0.000725)
        elif llm == 'a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5':        
            cost = elapsed_times*(0.000725)
        else:        
            cost = elapsed_times*(0.001400)
    return cost

#PDF Reader Code:
def extract_text_with_fallback():
    file_bytes = uploaded_file.read()
    try:
        pdf_data = BytesIO(file_bytes)
        text = extract_text(pdf_data)
        if text.strip():
            return text
    except:
        pass
    
    # If the above fails or does not extract text, then OCR is used (Image AI)
    images = convert_from_bytes(file_bytes)
    extracted_texts = []
    with st.spinner('Lädt...'):
        for image in images:
            extracted_text = pytesseract.image_to_string(image)
            extracted_texts.append(extracted_text)
    return " ".join(extracted_texts)

#Webscraper Code
def website(site):
    response = requests.get(site)
    soup = BeautifulSoup(response.text, 'html.parser')

    paragraphs = soup.find_all('p')

    extracted_text = ""


    for p in paragraphs:
        extracted_text += p.text + "\n"
    return extracted_text

def dropdown_complexity():
    compexity = st.sidebar.selectbox('Extraction features', ['Economically', 'Technically', 'Summarized Llama', 'Information page Llama','Bullet points Llama'], key='compexity')
    if compexity == 'Economically':
        complex_text= 'a\n Instruction: Summarize for a economic person'
    elif compexity == 'Technically':
        complex_text = '\n Instruction: Summarize in a technical way'
    elif compexity == 'Bullet points Llama':
        complex_text = '\n Instruction: Please transform this content distill the essential ideas into brief bullet points. Prioritize clarity and conciseness, omitting extras.'
    elif compexity == 'Information page Llama':
        complex_text = '\n Instruction: Please transform this content into a concise summerized information sheet to provide my colleagues with key information about the topic. Ensure the information is accurate and reliable by performing additional checks or validations with the content itself. Structure the information in clear sections and include headings for each topic. Answer long and detailed. And don\'t stop the output until you\'re finished with the information sheet.'
    elif compexity == 'Summarized Llama':
        complex_text = "\n Instruction: Please transform this content  to a concise summary that captures the main ideas and presents them in a clear and understandable manner. Ensure that the summary is free from jargon and is suitable for a general audience."
    return complex_text

# App Titel
st.set_page_config(page_title="📁💬 PDF Chatbot")



# API Token
with st.sidebar:
    # Bild
    col1, col2, col3 = st.columns([1,1.5,1])
    with col2:
    
        st.image('./Data/Logo_trans.png', use_column_width=True)
    #st.title('📁💬 PDF Chatbot')
    if 'API_TOKEN' in st.secrets:
        st.success('API key already provided!', icon='✅')
        replicate_api = st.secrets['API_TOKEN']['replicate_api_token']
        open_api = st.secrets['API_TOKEN']['openai_api']
    else:
        replicate_api = st.text_input('Enter Replicate API token:', type='password')
        if not (replicate_api.startswith('r8_') and len(replicate_api)==40):
            st.warning('Please enter your credentials!', icon='⚠️')
        open_api = st.text_input('Enter OpenAI API token:', type='password')
        if not (open_api.startswith('sk-')):
            st.warning('Please enter your credentials!', icon='⚠️')
        else:
            st.success('Proceed to entering your prompt message!', icon='👉')


    # Model selection
    st.subheader('Models and parameters')
    selected_model = st.sidebar.selectbox('Choose a Chatbot model', ['Llama2-7B', 'Llama2-13B', 'Llama2-70B','GPT-3.5 Turbo - 4k', 'GPT-3.5 Turbo - 16k','GPT 4 - 8k','GPT 4 - 32k'], key='selected_model')
    if selected_model == 'Llama2-7B':
        llm = 'a16z-infra/llama7b-v2-chat:4f0a4744c7295c024a1de15e1a63c880d3da035fa1f49bfd344fe076074c8eea'
    elif selected_model == 'Llama2-13B':
        llm = 'a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5'
    elif selected_model == 'Llama2-70B':
        llm = 'replicate/llama70b-v2-chat:e951f18578850b652510200860fc4ea62b3b16fac280f83ff32282f87bbd2e48'
    elif selected_model == 'GPT-3.5 Turbo - 4k':
        llm = 'gpt-3.5-turbo'
    elif selected_model == 'GPT-3.5 Turbo - 16k':
        llm = 'gpt-3.5-turbo-16k'
    elif selected_model == 'GPT 4 - 8k':
        llm = 'gpt-4'
    elif selected_model == 'GPT 4 - 32k':
        llm = 'gpt-4-32k'
    
    if "Llama" in selected_model:
        temperature = st.sidebar.slider('temperature', min_value=0.01, max_value=5.0, value=0.1, step=0.01)
        top_p = st.sidebar.slider('top_p', min_value=0.01, max_value=1.0, value=0.9, step=0.01)
        max_length = st.sidebar.slider('max_length', min_value=64, max_value=4096, value=4096, step=8)

    

    # PDF
    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

    if uploaded_file:
        text = extract_text_with_fallback()
        st.write("File uploaded successfully!")

        complex_text = dropdown_complexity()
    
        if st.button('Execute'):
            prompt = text+complex_text
            st.session_state.messages.append({"role": "user", "content": prompt})
        
        if st.button('Show text'):
            st.write(text)
    
    # Website
    web_input = st.text_input('Enter a website here:', '')
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

    if web_input:
        url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
        if url_pattern.fullmatch(web_input):
            web_text = website(web_input)
            complex_text = dropdown_complexity()
            if st.button('Zusammenfassen'):
                prompt = web_text+complex_text
                st.session_state.messages.append({"role": "user", "content": prompt})
            
            if st.button('Text Anzeigen'):
                st.write(web_text)
        else:
            st.write('Bitte valide Internetadresse eingeben!')

#API Keys
openai.api_key = open_api    
os.environ['REPLICATE_API_TOKEN'] = replicate_api

# Function for LLaMA2 response
def generate_llama2_response(prompt_input):
    string_dialogue = "You are a helpful assistant. You do not respond as 'User' or pretend to be 'User'. You only respond once as 'Assistant'."
    for dict_message in st.session_state.messages:
        if dict_message["role"] == "user":
            string_dialogue += "User: " + dict_message["content"] + "\n\n"
        else:
            string_dialogue += "Assistant: " + dict_message["content"] + "\n\n"
    start_time = time.time()
    output = replicate.run(llm, 
                           input={"prompt": f"{string_dialogue} {prompt_input} Assistant: ",
                                  "temperature":temperature, "top_p":top_p, "max_length":max_length, "repetition_penalty":1})
    full_response = ''
    for item in output:
        full_response += item
    end_time = time.time()
    elapsed_time = end_time - start_time
    #Here we enter an empty string into the cost function in order to be able to calculate costs, since the costs only depend on the execution time
    cost = cost_calculator(elapsed_time,"")
    with st.sidebar:
        st.markdown(f"<b>Execution time {llm}:</b> {elapsed_time}s<br><b>Cost</b>:<br>${cost}", unsafe_allow_html=True)
    return full_response

# GPT response function
def generate_gpt_response():
    start_messages={"role": "system", "content": "You are a helpful assistant."}
    if start_messages not in st.session_state.messages:
        st.session_state.messages.insert(0, start_messages)
    start_time = time.time()
    response = openai.ChatCompletion.create(
    model=llm,
    messages=st.session_state.messages)
    end_time = time.time()
    elapsed_time = end_time - start_time
    cost = cost_calculator(elapsed_time, response)
    with st.sidebar:
        st.markdown(f"<b>Execution time {llm}:</b> {elapsed_time}s<br><b>Cost</b>:<br>${cost}", unsafe_allow_html=True)
    return response["choices"][0]["message"]["content"]


# Saving the LLM-generated answers
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

# View or delete chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]
st.sidebar.button('Clear Chat History', on_click=clear_chat_history)



# User prompt
if prompt := st.chat_input(disabled=not replicate_api):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)



# Generate a new reply if the last message was not from the assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            if "Llama" not in selected_model:
                response = generate_gpt_response()
            else:
                response = generate_llama2_response(prompt)                
            placeholder = st.empty()
            placeholder.markdown(response)
    message = {"role": "assistant", "content": response}
    st.session_state.messages.append(message)

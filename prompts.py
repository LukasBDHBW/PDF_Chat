import streamlit as st
def dropdown_complexity(llm):
    if 'gpt-4' in llm:
        compexity = st.sidebar.selectbox('Extraction features', ['Information page','Summarized','Bullet points','Economically', 'Technically','Lecture flashcards','Lecture flashcards-de'], key='compexity')
        if compexity == 'Economically':
            start_text = 'Content:'
            last_text= 'a\n Instruction: Summarize for a economic person'
        elif compexity == 'Technically':
            start_text = 'Content:'
            last_text = '\n Instruction: Summarize in a technical way'
        elif compexity == 'Information page':
            start_text = 'Please transform the content of a Wikipedia page below into a concise and short summerized information sheet to provide my colleagues with key information about the topic. Ensure the information is accurate and reliable by performing additional checks or validations with the content itself. Structure the information in clear sections and include headings for each topic. Please note that my colleagues don\'t have much time and so the information page shouldn\'t be too long.'
            last_text = 'Content:'
        elif compexity == 'Summarized':
            start_text = 'Given the following text, generate a concise summary that captures the main ideas and presents them in a clear and understandable manner. Ensure that the summary is free from jargon and is suitable for a general audience.:'
            last_text = 'Text:'
        elif compexity == 'Bullet points':
            start_text = 'Given the following text, distill the essential ideas into brief bullet points. Prioritize clarity and conciseness, omitting extras.'
            last_text = '\n Text:'
        elif compexity == 'Lecture flashcards':
            start_text = 'Content:'
            last_text = '\n Instruction: The above content is a lecture. Could you please structure some questions and answers based on the document I can learn with flashcards. Please make sure that the core statements of the entire lecture are asked in these questions so that I can gain a good understanding of the topic. Please check based on your knowledge whether your answers are correct.'
        elif compexity == 'Lecture flashcards-de':
            start_text = 'Inhalt:'
            last_text = '\n Anleitung: Der obige Inhalt ist eine Vorlesung. Könnten Sie bitte einige Fragen und Antworten basierend auf dem Dokument „Ich kann mit Karteikarten lernen“ strukturieren? Bitte achten Sie darauf, dass bei diesen Fragen die Kernaussagen der gesamten Vorlesung abgefragt werden, damit ich ein gutes Verständnis für das Thema erlangen kann. Bitte überprüfen Sie anhand Ihres Wissens, ob Ihre Antworten richtig sind.'
    elif 'gpt-3.5' in llm:
        compexity = st.sidebar.selectbox('Extraction features', ['Information page','Summarized','Bullet points','Economically', 'Technically','Lecture flashcards','Lecture flashcards-de'], key='compexity')
        if compexity == 'Economically':
            start_text = 'Content:'
            last_text= 'a\n Instruction: Summarize for a economic person'
        elif compexity == 'Technically':
            start_text = 'Content:'
            last_text = '\n Instruction: Summarize in a technical way'
        elif compexity == 'Information page':
            start_text = 'Content:'
            last_text = '\n Instruction: Please transform this content into a concise and short summerized information sheet to provide my colleagues with key information about the topic. Ensure the information is accurate and reliable by performing additional checks or validations with the content itself. Structure the information in clear sections and include headings for each topic. Make only a few chapters so that the information page is 1/2 page long.'
        elif compexity == 'Summarized':
            start_text = 'Given the following text, generate a concise summary that captures the main ideas and presents them in a clear and understandable manner. Ensure that the summary is free from jargon and is suitable for a general audience.:'
            last_text = 'Text:'
        elif compexity == 'Bullet points':
            start_text = 'Given the following text, extract the 5 main key points and present them as concise bullet points. These bullet points should serve as reminders of the main ideas and be easily referable. Ensure clarity and avoid redundancy.'
            last_text = '\n Text:'
        elif compexity == 'Lecture flashcards':
            start_text = 'Content:'
            last_text = '\n Instruction: The above content is a lecture. Could you please structure some questions and answers based on the document I can learn with flashcards. Please make sure that the core statements of the entire lecture are asked in these questions so that I can gain a good understanding of the topic. Please check based on your knowledge whether your answers are correct.'
        elif compexity == 'Lecture flashcards-de':
            start_text = 'Inhalt:'
            last_text = '\n Anleitung: Der obige Inhalt ist eine Vorlesung. Könnten Sie bitte einige Fragen und Antworten basierend auf dem Dokument „Ich kann mit Karteikarten lernen“ strukturieren? Bitte achten Sie darauf, dass bei diesen Fragen die Kernaussagen der gesamten Vorlesung abgefragt werden, damit ich ein gutes Verständnis für das Thema erlangen kann. Bitte überprüfen Sie anhand Ihres Wissens, ob Ihre Antworten richtig sind.'
    else:
        compexity = st.sidebar.selectbox('Extraction features', ['Economically', 'Technically', 'Summarized', 'Information page','Bullet points'], key='compexity')
        if compexity == 'Economically':
            start_text = 'Content:'
            last_text= 'a\n Instruction: Summarize for a economic person'
        elif compexity == 'Technically':
            start_text = 'Content:'
            last_text = '\n Instruction: Summarize in a technical way'
        elif compexity == 'Bullet points':
            start_text = 'Content:'
            last_text = '\n Instruction: Please transform this content distill the essential ideas into brief bullet points. Prioritize clarity and conciseness, omitting extras.'
        elif compexity == 'Information page':
            start_text = 'Content:'
            last_text = '\n Instruction: Please transform this content into a concise summerized information sheet to provide my colleagues with key information about the topic. Ensure the information is accurate and reliable by performing additional checks or validations with the content itself. Structure the information in clear sections and include headings for each topic. Answer long and detailed. And don\'t stop the output until you\'re finished with the information sheet.'
        elif compexity == 'Summarized':
            start_text = 'Content:'
            last_text = "\n Instruction: Please transform this content  to a concise summary that captures the main ideas and presents them in a clear and understandable manner. Ensure that the summary is free from jargon and is suitable for a general audience."
    return start_text, last_text
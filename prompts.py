import streamlit as st
def dropdown_complexity(llm,lang):
    if lang !="de":
        if 'gpt-4' in llm:
            compexity = st.sidebar.selectbox('Extraction features', ['Information page','Summarized','Bullet points','Economically', 'Technically','Lecture flashcards'], key='compexity')
            if compexity == 'Economically':
                start_text = 'Content:'
                last_text= 'a\n Instruction: Summarize for a economic person'
            elif compexity == 'Technically':
                start_text = 'Content:'
                last_text = '\n Instruction: Summarize in a technical way'
            elif compexity == 'Information page':
                start_text = 'Please transform the content of a Wikipedia page below into a concise and short summerized information sheet to provide my colleagues with key information about the topic. Ensure the information is accurate and reliable by performing additional checks or validations with the content itself. Structure the information in clear sections and include headings for each topic. Please note that my colleagues don\'t have much time and so the information page shouldn\'t be too long.\n Content:'
                last_text = ''
            elif compexity == 'Summarized':
                start_text = 'Given the following text, generate a concise summary that captures the main ideas and presents them in a clear and understandable manner. Ensure that the summary is free from jargon and is suitable for a general audience.:\n Text:'
                last_text = ''
            elif compexity == 'Bullet points':
                start_text = 'Given the following text, distill the essential ideas into brief bullet points. Prioritize clarity and conciseness, omitting extras.\n Text:'
                last_text = ''
            elif compexity == 'Lecture flashcards':
                start_text = 'Content:'
                last_text = '\n Instruction: The above content is a lecture. Could you please structure some questions and answers based on the document I can learn with flashcards. Please make sure that the core statements of the entire lecture are asked in these questions so that I can gain a good understanding of the topic. Please check based on your knowledge whether your answers are correct.'
        elif 'gpt-3.5' in llm:
            compexity = st.sidebar.selectbox('Extraction features', ['Information page','Summarized','Bullet points','Economically', 'Technically','Lecture flashcards'], key='compexity')
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
                start_text = 'Given the following text, generate a concise summary that captures the main ideas and presents them in a clear and understandable manner. Ensure that the summary is free from jargon and is suitable for a general audience.\n Text:'
                last_text = ''
            elif compexity == 'Bullet points':
                start_text = 'Given the following text, extract the 5 main key points and present them as concise bullet points. These bullet points should serve as reminders of the main ideas and be easily referable. Ensure clarity and avoid redundancy.\n Text:'
                last_text = ''
            elif compexity == 'Lecture flashcards':
                start_text = 'Content:'
                last_text = '\n Instruction: The above content is a lecture. Could you please structure some questions and answers based on the document I can learn with flashcards. Please make sure that the core statements of the entire lecture are asked in these questions so that I can gain a good understanding of the topic. Please check based on your knowledge whether your answers are correct.'
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
    else:
        if 'gpt-4' in llm:
            compexity_de = st.sidebar.selectbox('Extraktionsfunktionen', ['Informationsseite','Zusammengefasst','Stichpunkte','Wirtschaftlich', 'Technisch','Karteikarten'], key='compexity_de')
            if compexity_de == 'Wirtschaftlich':
                start_text = 'Inhalt:'
                last_text= '\n Anleitung: Fasse den text für eine Wirtschaftsperson zusammen.'
            elif compexity_de == 'Technisch':
                start_text = 'Inhalt:'
                last_text = '\n Anleitung: Fachlich zusammenfassen'
            elif compexity_de == 'Informationsseite':
                start_text = 'Bitte wandeln Sie den Inhalt einer Wikipedia-Seite unten in ein prägnantes und kurzes, zusammenfassendes Informationsblatt um, um meinen Kollegen wichtige Informationen zum Thema zu liefern. Stellen Sie sicher, dass die Informationen korrekt und zuverlässig sind, indem Sie zusätzliche Prüfungen oder Validierungen am Inhalt selbst durchführen. Strukturieren Sie die Informationen in klare Abschnitte und fügen Sie Überschriften für jedes Thema hinzu. Bitte beachten Sie, dass meine Kollegen nicht viel Zeit haben und die Informationsseite daher nicht zu lang sein sollte.\n Inhalt:'
                last_text = ''
            elif compexity_de == 'Zusammengefasst':
                start_text = 'Erstellen Sie anhand des folgenden Textes eine prägnante Zusammenfassung, die die wichtigsten Ideen erfasst und sie klar und verständlich darstellt. Stellen Sie sicher, dass die Zusammenfassung frei von Fachjargon ist und für ein allgemeines Publikum geeignet ist.\n Text:'
                last_text = ''
            elif compexity_de == 'Stichpunkte':
                start_text = 'Fassen Sie anhand des folgenden Textes die wesentlichen Ideen in kurzen Stichpunkten zusammen. Legen Sie Wert auf Klarheit und Prägnanz und lassen Sie Extras weg.\n Text:'
                last_text = ''
            elif compexity_de == 'Karteikarten':
                start_text = 'Inhalt:'
                last_text = '\n Unterweisung: Der obige Inhalt ist eine Vorlesung. Könnten Sie bitte einige Fragen und Antworten strukturieren, die auf dem Dokument basieren, das ich mit Karteikarten lernen kann. Achten Sie bitte darauf, dass die Kernaussagen der gesamten Vorlesung in diesen Fragen abgefragt werden, damit ich ein gutes Verständnis für das Thema bekomme. Bitte überprüfen Sie anhand Ihrer Kenntnisse, ob Ihre Antworten richtig sind.'
        elif 'gpt-3.5' in llm:
            compexity_de = st.sidebar.selectbox('Extraktionsfunktionen', ['Informationsseite','Zusammengefasst','Stichpunkte','Wirtschaftlich', 'Technisch','Karteikarten'], key='compexity_de')
            if compexity_de == 'Wirtschaftlich':
                start_text = 'Inhalt:'
                last_text= '\n Anleitung: Fasse den text für eine Wirtschaftsperson zusammen.'
            elif compexity_de == 'Technisch':
                start_text = 'Inhalt:'
                last_text = '\n Anleitung: Fachlich zusammenfassen'
            elif compexity_de == 'Informationsseite':
                start_text = 'Bitte wandeln Sie den Inhalt einer Wikipedia-Seite unten in ein prägnantes und kurzes, zusammenfassendes Informationsblatt um, um meinen Kollegen wichtige Informationen zum Thema zu liefern. Stellen Sie sicher, dass die Informationen korrekt und zuverlässig sind, indem Sie zusätzliche Prüfungen oder Validierungen am Inhalt selbst durchführen. Strukturieren Sie die Informationen in klare Abschnitte und fügen Sie Überschriften für jedes Thema hinzu. Bitte beachten Sie, dass meine Kollegen nicht viel Zeit haben und die Informationsseite daher nicht zu lang sein sollte.\n Inhalt:'
                last_text = ''
            elif compexity_de == 'Zusammengefasst':
                start_text = 'Erstellen Sie anhand des folgenden Textes eine prägnante Zusammenfassung, die die wichtigsten Ideen erfasst und sie klar und verständlich darstellt. Stellen Sie sicher, dass die Zusammenfassung frei von Fachjargon ist und für ein allgemeines Publikum geeignet ist.\n Text:'
                last_text = ''
            elif compexity_de == 'Stichpunkte':
                start_text = 'Fassen Sie anhand des folgenden Textes die wesentlichen Ideen in kurzen Stichpunkten zusammen. Legen Sie Wert auf Klarheit und Prägnanz und lassen Sie Extras weg.\n Text:'
                last_text = ''
            elif compexity_de == 'Karteikarten':
                start_text = 'Inhalt:'
                last_text = '\n Unterweisung: Der obige Inhalt ist eine Vorlesung. Könnten Sie bitte einige Fragen und Antworten strukturieren, die auf dem Dokument basieren, das ich mit Karteikarten lernen kann. Achten Sie bitte darauf, dass die Kernaussagen der gesamten Vorlesung in diesen Fragen abgefragt werden, damit ich ein gutes Verständnis für das Thema bekomme. Bitte überprüfen Sie anhand Ihrer Kenntnisse, ob Ihre Antworten richtig sind.'
        else:
            compexity_de = st.sidebar.selectbox('Extraktionsfunktionen', ['Informationsseite','Zusammengefasst','Stichpunkte','Wirtschaftlich', 'Technisch'], key='compexity_de')
            if compexity_de == 'Wirtschaftlich':
                start_text = 'Inhalt:'
                last_text= '\n Anleitung: Fasse den text für eine Wirtschaftsperson zusammen.'
            elif compexity_de == 'Technisch':
                start_text = 'Inhalt:'
                last_text = '\n Anleitung: Fachlich zusammenfassen'
            elif compexity_de == 'Stichpunkte':
                start_text = 'Inhalt:'
                last_text = '\n Anweisung: Bitte verarbeiten Sie diesen Inhalt und destillieren Sie die wesentlichen Ideen in kurze Aufzählungspunkte. Legen Sie Wert auf Klarheit und Prägnanz und lassen Sie Extras weg.'
            elif compexity_de == 'Informationsseite':
                start_text = 'Inhalt:'
                last_text = '\n Anweisung: Bitte wandeln Sie diesen Inhalt in ein prägnantes Informationsblatt im Sommerformat um, um meinen Kollegen die wichtigsten Informationen zu diesem Thema zu vermitteln. Stellen Sie sicher, dass die Informationen korrekt und zuverlässig sind, indem Sie zusätzliche Überprüfungen oder Validierungen mit dem Inhalt selbst durchführen. Gliedern Sie die Informationen in klare Abschnitte und fügen Sie Überschriften für jedes Thema ein. Antworten Sie lang und ausführlich. Und stoppen Sie die Ausgabe nicht, bevor Sie mit dem Informationsblatt fertig sind.'
            elif compexity_de == 'Zusammengefasst':
                start_text = 'Inhalt:'
                last_text = "\n Anweisung: Bitte wandeln Sie diesen Inhalt in eine prägnante Zusammenfassung um, die die wichtigsten Gedanken aufgreift und sie klar und verständlich darstellt. Achten Sie darauf, dass die Zusammenfassung frei von Fachjargon ist und sich an ein allgemeines Publikum richtet."
    return start_text, last_text
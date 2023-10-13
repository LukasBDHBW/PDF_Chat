# Chatbot-Vergleich: LLama 2 Version GPT-4 vs. GPT-3.5 Turbo

Willkommen bei diesem Chatbot-Vergleichsprojekt! Hier können Sie direkt die Unterschiede zwischen der LLama 2 Version von GPT-4 und GPT-3.5 Turbo innerhalb einer Chatbot-Seite erfahren und vergleichen. 

<p align="center">
  <img src="./Data/Logo_Chatbot.png" alt="Alternate Text" width="300"/>
</p>


## Features

- **Chatbotvergleich**: Testen Sie direkt die Antwortqualität und Geschwindigkeit zwischen LLama 2 Version GPT-4 und GPT-3.5 Turbo.
- **PDF Uploader**: Laden Sie Ihre eigenen PDFs hoch und lassen Sie diese von den Chatbots analysieren.
- **Webscraper**: Lassen Sie Inhalte direkt aus dem Web von den Chatbots extrahieren und analysieren.

## Anweisungen zum Starten

1. **Konfigurationsdatei erstellen**:
   Legen Sie eine `secrets.toml` Datei im `.streamlit` Ordner an und füllen Sie sie mit Ihren eigenen API-Keys.

   Beispiel:
   ```toml
   [gpt]
   api_key = "YOUR_API_KEY"
   ```

2. **Abhängigkeiten installieren**:
   Sie müssen zuerst die in der `requirements.txt` angegebenen Abhängigkeiten installieren. Verwenden Sie dafür folgenden Befehl:

   ```bash
   pip install -r requirements.txt
   ```

3. **App starten**:
   Zum Starten der App führen Sie den folgenden Befehl in Ihrem Terminal aus:

   ```bash
   streamlit run [Dateipfad]
   ```
   
   Ersetzen Sie `[Dateipfad]` durch den tatsächlichen Pfad zur Hauptdatei Ihres Projekts, z. B. `app.py`.

Viel Spaß beim Erkunden und Vergleichen der Chatbots!
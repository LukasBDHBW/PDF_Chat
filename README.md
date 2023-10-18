# PDF Chatbot: Comparing Large Language Models

The "PDF Chatbot" project enables users to compare various Large Language Models (Llama 2, GPT-4, and GPT-3.5 Turbo). This chatbot can read PDF documents using OCR and scrape websites to summarize their content, enabling interactive chat about the summarized content.

<p align="center">
  <img src="./Data/Logo_trans.png" alt="Alternate Text" width="200"/>
</p>

## Prerequisites:

- An **OpenAI API Key**. Register on [OpenAI](https://platform.openai.com/account/api-keys) and provide your credit card information to unlock the API key.
- A **Replicate API Token** for Llama 2. Create a free account on [Replicate](https://replicate.com/) and copy the API token from [this page](https://replicate.com/account/api-tokens).

## Local Execution:

1. Create a Conda environment using the provided YAML file:
```
conda env create -f environment.yml
```

2. Activate the environment:
```
conda activate DTC
```

3. Navigate to the `PDF_Chatbot.py` folder:
```
cd path/to/PDF_Chatbot.py
```

4. Launch the app:
```
streamlit run .\PDF_Chatbot.py
```

5. Open your web browser and input your API keys to use the chatbot. Alternatively, you can create a `secrets.toml` file in the `.streamlit` directory to permanently store your API keys:

```
[API_TOKEN]
replicate_api_token = "YOUR_REPLICATE_TOKEN"
openai_api = "YOUR_OPENAI_KEY"
```

## Docker:

1. Navigate to the Docker folder:
```
cd path/to/docker_folder
```

2. Place the `secrets.toml` file, as described above, in the `.streamlit` directory.

3. Install Docker from [here](https://docs.docker.com/get-docker/).

4. Build the Docker container:
```
docker build -t pdf_chatbot .
```

5. Run the container:
```
docker run -p 8080:8080 pdf_chatbot
```

6. Open your web browser and go to [http://localhost:8080/](http://localhost:8080/).

## Evaluating LLM Classification Capabilities:

To test the classification abilities of the LLMs:

1. Install and activate the Conda environment as described above.

2. Launch the Jupyter Notebook `Classification.ipynb` in the `Notebook` folder.

3. Download the required datasets from `LINK` and place them in the `Data` folder.

Enjoy testing and comparing the models! If you have questions or suggestions, feel free to open an issue or submit a pull request.
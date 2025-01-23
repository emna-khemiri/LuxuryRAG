# LuxuryRAG

## Features

- **Luxury Fashion Insights**: Query the system to get answers to questions regarding luxury fashion, with responses based on the McKinsey & Company "State of Fashion Luxury 2025" report.
- **Conversational Interface**: Use the chatbot backend to simulate a dynamic and informative conversation about the future of luxury fashion.
- **Customizable Prompt**: The chatbot utilizes customizable prompts to ensure responses are relevant to specific queries.

## WorkFlow
* Data Preprocessing done behind the scene, stored in VectorStore
* Load data from vector store in `src/dataloader.py`
* Create prompt template in `src/prompt.py`
* Call the Cohere model, load all params into the chain in `src/chatbot.py`.




## Notes
* Vector DB: Chroma DB
* Embedding model: `Cohere embed-multilingual-v3.0`
* LLM: `Cohere Command R+`

## 4. How to Run
* `pip install -r requirements.txt`
* Run `uvicorn app:app --reload`
* Get to `http://127.0.0.1:8000/docs`
* Ask your question and wait for the answer
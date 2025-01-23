from dotenv import load_dotenv
import os
from langchain_cohere import CohereEmbeddings, ChatCohere
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from src.dataloader import DataLoader
from src.prompt import prompt_template
# Load environment variables from .env file
load_dotenv()

class ChatBot:
    def __init__(self, vector_store_path, api_key=None):
        # Use API key from .env if not provided directly
        if not api_key:
            api_key = os.getenv("COHERE_API_KEY")
        
        os.environ["COHERE_API_KEY"] = api_key
        self.embeddings = CohereEmbeddings(model="embed-multilingual-v3.0")
        self.llm = ChatCohere(
            model="command-r-plus",
            temperature=0.1,
            max_tokens=None,
            timeout=None,
            max_retries=2,
        )
        self.db = DataLoader.load_vector_store(vector_store_path, self.embeddings)
        self.retriever = self.db.as_retriever(search_type="mmr")
        self.memory = ConversationBufferMemory(
            input_key='question',
            output_key='answer',
            memory_key="chat_history",
            return_messages=True
        )
        self.prompt = PromptTemplate(
            template=prompt_template,
            input_variables=['context', 'question', 'chat_history']
        )
        self.conversational_chain = ConversationalRetrievalChain.from_llm(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.retriever,
            memory=self.memory,
            return_source_documents=True,
            combine_docs_chain_kwargs={"prompt": self.prompt}
        )

    def process_chat(self, question: str):
        """
        Generate response to users

        Args:
        question (str): The question asked from users.

        Returns:
        str: response from the llm
        """
        result = self.conversational_chain.invoke({"question": question})
        answer = result["answer"]
        history = self.memory.load_memory_variables({})
        return answer, history

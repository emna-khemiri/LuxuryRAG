from langchain_community.document_loaders import UnstructuredFileLoader
from langchain_community.vectorstores.utils import filter_complex_metadata
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import Chroma


class DataLoader:
    def __init__(self):
        self.text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
            chunk_size=10000, chunk_overlap=0
        )

    def load_data(self, files):
        loader = UnstructuredFileLoader(files, strategy="hi_res", mode="elements")
        docs = loader.load()  # Load the data
        docs = filter_complex_metadata(docs)  # Remove unused metadata
        data = self.text_splitter.split_documents(docs)
        return data

    @staticmethod
    def load_vector_store(file_path, embeddings):
        db = Chroma(persist_directory=file_path, embedding_function=embeddings)
        return db

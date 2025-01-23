from src.chatbot import ChatBot
from src.dataloader import DataLoader


def main():
    # Initialize the DataLoader and ChatBot
    data_loader = DataLoader()
    chat_bot = ChatBot(vector_store_path='./VectorStore/')

    # Example usage: process a chat related to the luxury fashion market
    answer, history = chat_bot.process_chat("What are the key trends driving the luxury market in 2025?")

    # Print the answer and chat history
    print("Answer:", answer)
    print("Chat History:", history)


if __name__ == "__main__":
    main()

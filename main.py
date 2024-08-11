from langchain_ollama import OllamaLLM
from langchain.prompts import ChatPromptTemplate

template = """

Answer the question below.

Here is the converstaion history: {context}

Question: {question}

Answer:
"""


prompt = ChatPromptTemplate.from_template(template)

model = OllamaLLM(model="llama3")
chain = prompt | model

def handle_conversation():
    context = ""
    print("Welcome to the AI Chatbot! Type 'exit' to quit")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        result  = chain.invoke({"context": context, "question": user_input})
        print("Bot: ", result)
        context += f"\n User: {user_input} \n AI: {result}"


if __name__ == '__main__':
    handle_conversation()


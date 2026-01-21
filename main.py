from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from pydantic import v1 as pydantic_v1

# Initialize chatbot
chatbot = ChatBot("AI Assistant")
trainer = ChatterBotCorpusTrainer(chatbot)

# Train with English dataset
trainer.train("chatterbot.corpus.english")

# Chat loop
while True:
    user_input = input("You: ")
    response = chatbot.get_response(user_input)
    print("AI Assistant:", response)

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from pydantic import v1 as pydantic_v1
import nltk
from nltk.chat.util import Chat, reflections

# Initialize chatbot
# chatbot = ChatBot("AI Assistant")
# trainer = ChatterBotCorpusTrainer(chatbot)

# Train with English dataset
# trainer.train("chatterbot.corpus.english")

# Chat loop
# while True:
#     user_input = input("You: ")
#     response = chatbot.get_response(user_input)
#     print("AI Assistant:", response)

# Define chatbot responses using nltk,
pairs = [
    [r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]],
    [r"what is your name?", ["I am a chatbot, created to assist you!"]]
]
 
# limited Chatbot (limBot)
chatbot = Chat(pairs, reflections)
while True:
    user_input = input("You: ")
    print("limBot:", chatbot.respond(user_input))

# responses outside the scope of the pairs will result in "none" response.
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from pydantic import v1 as pydantic_v1

# Initialize chatbot
# Use default storage adaptor with sqlite database
# Add additional Logic Adaptors
chatbot = ChatBot(
    'Clive',
    logic_adapters=[
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.MathematicalEvaluation',
    ],
)

# We can train our bot with multiple sets of data.
# First let's train with an English dataset
trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train("chatterbot.corpus.english")

# Now we'll add Lists
trainer = ListTrainer(chatbot)

trainer.train([
    'Hello, how are you?',
    'I am doing well.',
    'That is good to hear.',
    'Thank you'
])

# Additional List
trainer.train([
    'Hello, how are you?',
    'I am great.',
    'That is awesome.',
    'Thanks'
])

# There might be a better way to do this
trainer.train([
    "Thank you",
    "You are welcome",
    "How else can I assist you?",
    "Would you like to play a game?",
    "I use machine learning to understand your questions and respond."
])

# Begin User input
print('Hello. My name is Clive.')

name = input("What's Your Name?: ")
print(f"Hello {name}, how can I help you?")

# Chat loop
while True:
    user_input = input("You: ")
    response = chatbot.get_response(user_input)
    print("Clive:", response)

 # Press ctrl-c or ctrl-d on the keyboard to exit
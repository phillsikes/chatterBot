# chatterBot v1.0
## Goal
Build a simple chatbot in Python using Chatterbot and NLTK Libraries.

## What I ended up with
### mainV1
- The "AI unAssistant"
- Using the basic parameters built into Chatterbot with a fast set of training data, we get as very unhelpful assistant.
- Some responses are reasonable, while others are totally bonkers.
- Additional training will be needed to make this a more effective communicator.

### mainV2
- "limBot" the limited chatbot
- With NLTK, limBot uses pattern-matching to respond in a way that feels somewhat natural.
- The responses are appropriate when the proper question is asked.
- But this is still limited to the "pairs" data set that it uses as defined responses. 

## Next Steps
With the limited scope of these 2 tests it is clear how important the training data is to these kinds of services. The next challenge will be to investigate means by which a more complete set of training data can be used to create a more useful chatBot.

Future Goals
- Implement a larger chat model.
- Improve training data sources.
- Implement Retrieval-Augmented Generation (RAG) as a way to improve responses.
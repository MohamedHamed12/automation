from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

chatbot=ChatBot(name='Calculator',
              read_only=True,
              logic_adapters=["chatterbot.logic.MathematicalEvaluation"],
              storage_adapter="chatterbot.storage.SQLStorageAdapter")

print("Hello, I am a calculator. How may I help you?")
while (True):
    # take the input from the user
    user_input = input("me: ")

    # check if the user has typed quit to exit the prgram
    if user_input.lower() == 'quit':
        print("Exiting")
        break

    # otherwise, evaluate the user input
    # print invalid input if the AI is unable to comprehend the input
    try:
        response = chatbot.get_response(user_input)
        print("Calculator:", response)
    except:
        print("Calculator: Please enter valid input.")


# chatbot = ChatBot("Hamed",
    # storage_adapter='chatterbot.storage.SQLStorageAdapter',
    # logic_adapters=[
    #     {
    #         'import_path': 'chatterbot.logic.BestMatch',
    #         'statement_comparison_function': 'chatterbot.comparisons.levenshtein_distance',
    #         'response_selection_method': 'chatterbot.response_selection.get_first_response'
    #     }
    # ],
    # database_uri='sqlite:///database.sqlite3'
# )



# trainer = ListTrainer(chatbot)
# trainer.train([
#     "Hi",
#     "Hello",
#     "How are you?",
#     "I'm doing fine.",
#     "That is good to hear",
#     "Thank you",
#     "You're welcome."
# ])
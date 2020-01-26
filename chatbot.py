from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

def get_response(usrText, self):
    bot = ChatBot('Bot',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'maximum_similarity_threshold': 0.90,
            'default_response': 'I am sorry, but I do not understand.'
        },
        'chatterbot.logic.MathematicalEvaluation',
    ])
    trainer = ChatterBotCorpusTrainer(bot)

    while True:
        if usrText.strip().lower() == 'bye':
            return('bye')
            break          
        else:
            result = bot.get_response(usrText.strip())
            reply = str(result)
            return(reply)

        

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot("MERVYN")
bot.set_trainer(ListTrainer)

for files in os.listdir('C:/english/'):
          data = open('C:/english/' + files,'r').readlines()
          bot.train(data)
            

while True:
              message = input('DIVYA:')
              if message.strip() != 'Bye' :
                          reply = bot.get_response(message)
                          print("MERVYN:" ,reply)
              if message.strip() == 'Bye' :
                           print("MERVYN: Bye")
                           break

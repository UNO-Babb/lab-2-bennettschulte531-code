#Magic8Ball.py
#Name:Bennett Schulte
#Date:9/5/25
#Assignment:Lab 2

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  responses = (
  "It is certain.",
  "It is decidely so.",
  "Without a doubt.",
  "Yes-definitly.",
  "You may rely on it.",
  "As I see it, yes.",
  "Most likely.",
  "Outlook good.",
  "Yes.",
  "Signs point to yes.",
  "Reply hazy, try again.",
  "Ask again later.",
  "Better not tell you know.",
  "Cannot predict now.",
  "Concentrate and ask again.",
  "Don't count on it.",
  "My reply is no.",
  "My sources say no.",
  "Outlook not so good.",
  "Very doubtful.",)
  


  print("Magic 8 Ball")
  #Prompt the user for their question.
  question = input("Ask the Magic 8 Ball a question: ")
  #Answer question randomly with one of the options from your earlier list.
  answer = random.choice(responses)
  print("The Magic 8 Ball says:", answer)

if __name__ == '__main__':
  main()

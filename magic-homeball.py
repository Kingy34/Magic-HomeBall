import random

answers = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it, yes", "Most likely","Outlook good", "Yes", "Signs point to yes", "Reply hazy try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]

def main():
    print('''Magic-HomeBall, a magic 8-ball clone in python
    Think on something
    and press enter to see if the answer is positive or negative''')
    
    input()
    
    print(answers[random.randint(0,19)]+'''
    ''')

while True:
    main()
    

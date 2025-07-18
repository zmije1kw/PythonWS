import random

messages = ['It is certain.',
            'It is decidely so.',
            'Reply hazy, try again.',
            'Ask again later.',
            'My reply is no.',
            'Outlook not so good.',
            'Very doubtful',
            'Yes definitely!']

print(messages[random.randint(0,len(messages)) - 1])

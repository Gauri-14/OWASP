from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.logic import BestMatch
training_data = [
    'What is OWASP PyGoat?',
    'OWASP PyGoat is an intentionally vulnerable web application used for learning web security testing.',
    'Why should I learn web security testing?',
    'Learning web security testing can help you understand how to identify and prevent web application attacks.',
    'What types of vulnerabilities can PyGoat help me learn about?',
    'PyGoat can help you learn about various types of web application vulnerabilities, including injection attacks, cross-site scripting (XSS), and broken authentication and session management.',
    'How can I use PyGoat to learn web security testing?',
    'PyGoat includes a series of lessons and challenges designed to teach you about web security testing techniques and common vulnerabilities.',
    'Is PyGoat suitable for beginners?',
    'Yes, PyGoat is designed to be accessible to beginners and experienced professionals alike.',
    'Where can I download PyGoat?',
    'You can download PyGoat from the official GitHub repository at https://github.com/OWASP/PyGoat',
    'Are there any resources available to help me get started with PyGoat?',
    'Yes, the PyGoat documentation includes a Getting Started guide and a list of additional resources to help you learn about web security testing.',
    'Can I contribute to PyGoat?',
    'Yes, PyGoat is an open-source project and welcomes contributions from anyone interested in improving the application.',
]

chatbot = ChatBot(
    "PyGoatBot",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database_uri="sqlite:///database.sqlite3",
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "default_response": "I'm sorry, I'm not sure",
            "maximum_similarity_threshold": 0.80,
        }
    ]
)

trainer = ListTrainer(chatbot)
trainer.train(training_data)

print("Welcome to PyGoatBot! Type 'q' or 'exit' to quit.")
while True:
    try:
        user_input = input("You: ")
        if user_input.lower() == "exit" or user_input.lower() == "q":
            break

        print("Available questions:")
        for i, question in enumerate(training_data[::2], start=1):
            print(f"{i}. {question}")

        while True:
            try:
                question_index = int(input("Enter a number to select a question: "))
                break
            except ValueError:
                print("Please enter a valid number.")

        question = training_data[(question_index - 1) * 2]
        response = chatbot.get_response(question)
        print(f"PyGoatBot: {response}")

    except (KeyboardInterrupt, EOFError):
        break
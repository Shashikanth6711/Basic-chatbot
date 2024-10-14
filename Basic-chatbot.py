import tkinter as tk
from tkinter import scrolledtext
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses for the chatbot
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey!"]
    ],
    [
        r"how are you?",
        ["I'm doing well, thank you!", "I'm great, thanks for asking!"]
    ],
    [
        r"what is your name?",
        ["You can call me Chatbot.", "I'm Chatbot, nice to meet you!"]
    ],
    [
        r"want to ask a question",
        ["Yeah sure"]
    ],
    [
        r"(.) your name(.)",
        ["My name is Chatbot.", "I go by the name Chatbot."]
    ],
    [
        r"(.) (sorry|apologies)(.)",
        ["No need to apologize.", "It's alright."]
    ],
    [
        r"quit|bye|exit",
        ["Goodbye!", "Bye, take care!"]
    ],
    [
        r"how old are you?",
        ["I am just a computer program, so I don't have an age."]
    ],
    [
        r"what can you do?",
        ["I'm here to chat with you and answer your questions!"]
    ],
    [
        r"tell me a joke",
        ["Why don't scientists trust atoms? Because they make up everything!"]
    ],
    [
        r"(.) (love|like) you(.)",
        ["Aww, thank you!", "That's very kind of you!"]
    ],
    [
        r"(.) (hate|dislike) you(.)",
        ["I'm sorry to hear that."]
    ],
    [
        r"what is the weather today?",
        ["I'm just a chatbot and I can't check the weather. You can use a weather app or website to find out!"]
    ],
    [
        r"what is your favorite color?",
        ["I don't have a favorite color, as I am just a program."]
    ],
    [
        r"how can I help you?",
        ["You can ask me anything you'd like to know!"]
    ]
]

# Create a Chat object
chatbot = Chat(pairs, reflections)

def chatbot_response(user_input):
    """
    Function to get response from the chatbot.
    """
    return chatbot.respond(user_input)

def send_message():
    """
    Function to send user message and display chatbot response.
    """
    message = entry.get()
    entry.delete(0, tk.END)
    if message.lower() == 'quit':
        chat_area.insert(tk.END, "You: " + message + "\n")
        chat_area.insert(tk.END, "Chatbot: " + chatbot_response(message) + "\n")
        chat_area.insert(tk.END, "Chatbot: Bye! Take care.\n")
        entry.config(state=tk.DISABLED)
        send_button.config(state=tk.DISABLED)
    else:
        chat_area.insert(tk.END, "You: " + message + "\n")
        chat_area.insert(tk.END, "Chatbot: " + chatbot_response(message) + "\n")
        chat_area.see(tk.END)

# Create the main window
root = tk.Tk()
root.title("Chatbot")

# Create a frame to hold the chat area
chat_frame = tk.Frame(root)
chat_frame.pack(padx=10, pady=10)

# Create a scrolled text widget to display the chat
chat_area = scrolledtext.ScrolledText(chat_frame, wrap=tk.WORD, width=50, height=20)
chat_area.pack(expand=True, fill=tk.BOTH)

# Create a frame to hold the message entry field and send button
entry_frame = tk.Frame(root)
entry_frame.pack(padx=10, pady=10, fill=tk.BOTH)

# Create an entry widget to type messages
entry = tk.Entry(entry_frame, width=40)
entry.pack(side=tk.LEFT, padx=(0, 10))

# Create a button to send messages
send_button = tk.Button(entry_frame, text="Send", width=10, command=send_message)
send_button.pack(side=tk.LEFT)

# Bind the Enter key to send messages
root.bind('<Return>', lambda event=None: send_message())

# Focus on the entry field by default
entry.focus()

# Run the main event loop
root.mainloop()
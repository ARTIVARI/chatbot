
def get_response(input_text):
    responses = {
        "hi": "Hello! How can I help you?",
        "how are you?": "I'm doing well, thank you.",
        "bye": "Goodbye! Have a great day!",
        "default": "I'm not sure I understand. Can you rephrase that?"
    }
    
    
    input_text = input_text.lower()
    
    
    if input_text in responses:
        return responses[input_text]
    else:
        return responses["default"]


print("Chatbot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    
    
    if user_input.lower() == 'bye':
        print("Chatbot: Goodbye!")
        break
    
    
    response = get_response(user_input)
    print("Chatbot:", response)

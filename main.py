# ChatBot RegEx
import re

chatbotResponse = {} # Tinggal ditentuin chatbotnya mau respon apa (dibikin dictionary)

defResponse = {} # default response ke user kalo inputnya gk sesuai template

def getResponse(userInput):
    for pattern, response in chatbotResponse.items():
        if re.search(pattern, userInput, re.IGNORECASE):
            return response
    return defResponse

def chatbotRegex():
    print('Chatbot: ')
    while True:
        userInput = input('You: ')
        if re.search(r'bye|goodbye', userInput, re.IGNORECASE):
            print('Chatbot: Bye.')
            break
        response = getResponse(userInput)
        print(f'Chatbot: {response}')

if __name__ == "__main__":
    chatbotRegex()
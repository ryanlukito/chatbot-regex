import re

introduction = "Hai, saya adalah regex chatbot (YapBot), apakah anda memiliki pertanyaan?"
defaultResponse = "Maaf, saya tidak mengerti hal itu. Bisakah anda mengulanginya lagi?"

# Define the chatbot's responses based on regex patterns
chatbotResponse = {
    r'hi|hello|hey|hai|hallo': 'Hallo, siapa namamu',
    r'nama saya (.*)': 'Senang berkenalan denganmu, {0}!',
    r'bagaimana kabarmu|apa kabarmu': 'Saya baik-baik saja, bagaimana dengan kamu? saya harap kamu baik-baik saja',
    r'siapa namamu': 'Saya adalah rule-based chatbot yang dibuat oleh Alex & Ryan. Saya dibuat untuk menemani waktu kosongmu',
    r'apakah kamu juga suka (.*)': 'Sayangnya aku tidak memiliki preferensi apapun, tetapi aku bisa membantumu untuk menyukai {0}!',
    r'thank you|thanks|terimakasih|makasih .*': 'Sama-sama, jika anda punya pertanyaan lebih lanjut, silahkan tanyakan saja!',
    r'bye|goodbye|selamat tinggal|oke.*|baiklah|terimakasih': 'Goodbye! Have a great day!',
    r'aku suka (.*)': 'Wah, {0} terdengar menarik!',
}

def getResponse(userInput):
    for pattern, response in chatbotResponse.items():
        match = re.match(pattern, userInput, re.IGNORECASE)
        if match:
            # Replace placeholders with captured group(s) from the user input
            return response.format(*match.groups())
    return defaultResponse

def chatbotRegex():
    print("Selamat Datang! Ini adalah rule-based chatbot. Untuk keluar masukan -1!")
    print(f"YapBot\t: {introduction}")
    
    while True:
        user_input = input(f"User\t: ")
        
        if user_input.strip() == "-1":
            print("PROGRAM SELESAI, TERIMAKASIH!")
            break
        
        bot_response = getResponse(userInput=user_input)
        print(f"YapBot\t: {bot_response}")

if __name__ == "__main__":
    chatbotRegex()

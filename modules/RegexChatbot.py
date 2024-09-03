import re

class ChatBot:
    def __init__(
        self, 
        botName="Regex-Alex-Ryan",
        chatbotResponse=None
    ):
        if chatbotResponse is None:
            chatbotResponse = {
                r'hi|hello|hey|hai|hallo|halo': 'Halo, ada yang saya bisa bantu?',
                r'siapa namamu?': 'Saya adalah ruled based chatbot yang dibuat oleh Alex & Ryan. Saya dibuat untuk menemani kamu',
                r'apa tujuanmu dibuat?': 'Sekedar basa-basi saja',
                r'apakah kamu suka (.*)': 'I do not have preferences, but I enjoy helping you!',
                r'ya saya memiliki pertanyaan': 'Baiklah, apa pertanyaan Anda?',
                r'bagaimana|apa kabarmu': 'Saya baik-baik saja, bagaimana dengan kamu?',
                r'siapa .*mu': 'Saya adalah ruled based chatbot yang dibuat oleh Alex & Ryan.',
                r'thank you|thanks|terimakasih|makasih .*': 'Sama-sama, jika Anda punya pertanyaan lebih lanjut silakan tanyakan saja!',
                r'bye|goodbye|selamat tinggal|oke.*|baiklah|terimakasih': 'Goodbye! Have a great day!'
            }

        self.botName = botName
        self.chatbotResponse = chatbotResponse
        
        self.intro = "Hai, saya adalah Regex chatbot (yepping), apakah Anda memiliki pertanyaan?"
        self.defaultResponse = "Maaf, saya tidak mengerti hal itu. Bisakah Anda mengulanginya lagi?"
        
        self.__counter__ = 0
        self.__CharList__ = [self.botName, 'user']
        
    def reply(self, userInput):
        for pattern, response in self.chatbotResponse.items():
            if re.search(pattern=pattern, string=userInput, flags=re.IGNORECASE):
                return response
        return self.defaultResponse

    @property
    def characterTurn(self):
        self.__counter__ += 1
        return self.__CharList__[(self.__counter__ % 2)]
        
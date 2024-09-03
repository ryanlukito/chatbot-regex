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
                r'siapa namamu?': 'Saya adalah ruled based chatbot yang dibuat oleh Alex & Ryan, mahasiswa DTETI FT UGM',
                r'apa tujuanmu dibuat?': 'Memberikan informasi mengenai DTETI, mulai dari perkuliahan sampai kehidupan mahasiswa/i-nya',
                r'saya|aku memiliki pertanyaan': 'Baiklah, apa pertanyaan Anda?',
                r'apakah kamu tahu tentang (.*)': 'Tentu apakah {0} menurutmu menarik? Jelaskan pada saya!',
                r'menurut (saya|aku), (.*)':'Aku setuju dengan pendapatmu!',
                r'(.*) berkuliah di DTETI':'Saya sangat penasaran bagaimana rasanya, jelaskan pada saya!',
                r'(.*)?sulit|susah (.*)': 'Bisakah anda jelaskan dimana susahnya?',
                r'menurut (saya|aku), (susah|sulit)nya itu (.*)': 'Tenang saja, yang kamu rasakan itu valid. Tetap semangat ya!',
                r'(.*)?siapa yang paling (ganteng|baik|tidak rasis|cerdas|positif) di DTETI?': 'Wah jelas Alex Cinatra Hutasoit', #Easter Egg
                r'thank you|thanks|terimakasih|makasih (.*)?': 'Sama-sama, jika Anda punya pertanyaan lebih lanjut silakan tanyakan saja!',
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
        
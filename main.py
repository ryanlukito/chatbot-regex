import re

introduction = "Hai Saya adalah regex chatbot(yepping), apakah anda memiliki pertanyaan? "
defaultResponse = "Maaf saya tidak mengerti hal itu, bisakah anda mengulanginya lagi? "

patterns_response = {
    r'ya saya memiliki pertanyaan': 'baiklah apa pertanyaan anda? ',
    r'hi|hello|hey|hai|hallo': 'Hallo, ada yang saya bisa bantu? ',
    r'bagaimana|apa kabarmu': 'Saya baik baik saja, bagaimana dengan kamu? ',
    r'siapa .*mu': 'Saya adalah ruled based chatbot yang dibuat oleh Alex & Ryan. ',
    r'(.*) your (favorite|favourite) (.*)': 'I do not have preferences, but I enjoy helping you! ',
    r'thank you|thanks|terimakasih|makasih .*': 'sama sama, jika anda punya pertanyaan lebih lanjut silahkan tanyakan saja! ',
    r'bye|goodbye|selamat tinggal|oke.*|baiklah|terimakasih': 'Goodbye! Have a great day! '
}

def getResponse(userInput):
    for pattern, response in patterns_response.items():
        if re.search(pattern=pattern, string=userInput, flags=re.IGNORECASE):
            return response
    return defaultResponse

def ngeYepping(saveHistory=False):
    i = 0
    CharList = ['YepBot', 'user']
    print("Selamat Datang! Ini adalah rule-based chat bot. Unutk Keluar masukan -1!\n")
    
    bot_response = print(f"{CharList[i % 2]}\t: {introduction}")
    i += 1
    user_input = input(f"{CharList[i % 2]}\t: ")
    print("\n")
    
    while True:
        i += 1
        bot_response = getResponse(userInput=user_input)
        print(f"{CharList[i % 2]}\t: {bot_response}")
        user_input = input(f"{CharList[i % 2]}\t: ")
        print("\n")
        
        if user_input.strip() == "-1":
            print("PROGRAM SELESAI, TERIMAKASIH!")
            break

def main():
    ngeYepping()

if __name__ == "__main__":
    main()

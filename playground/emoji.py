def get_emoji(text = ""):
    words = text.split(' ')
    emojis = {
        ":)" : "đ",
        ":(" :  "âšī¸",
        "morning" : "âī¸"
    }

    output = ""
    for word in words:
        output += emojis.get(word.lower(), word) + ' '

    return output


message = input('> ')
print(get_emoji(message))




import emoji
text_with_emojis = """I  ❤ to code. I also 👍 to read 📚 😅.  I have many 💻 at home. I  ❤ to ✍ a lot. I have many 📱 and I love ❤  😃 😀 😄 and 😆 🤣 😂 😹 😆 🤣. 

"""

text_without_emojis = emoji.demojize(text_with_emojis)
print("My original text with emojis was : ", text_with_emojis)
print("My new text after converting emojis to text :", text_without_emojis)




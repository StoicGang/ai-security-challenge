import tiktoken

encoding = tiktoken.get_encoding("cl100k_base")

sentences = [
    "I love challenging exercise", 
    "I love cybersecurity",
    "cyberdragonification",
    "threathuntingplusplus😎",
    "threathuntingplusplus",
    "I want to learn AI security",
    "🚀 AI security is fun!"
]

dir(encoding)

for sentence in sentences:
    encoded_string = encoding.encode(sentence)
    print("-----------------------------------")
    print("Sentence:")
    print(sentence)
    print("Token IDs:")
    print(encoded_string)
    print("Token count:")
    print(len(encoded_string))

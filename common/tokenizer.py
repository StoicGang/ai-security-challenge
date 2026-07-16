import tiktoken

DEFAULT_ENCODING = "cl100k_base"

_encoding = tiktoken.get_encoding(DEFAULT_ENCODING)


def tokenize(text: str):
    # Returns the token IDs for a string.
    return _encoding.encode(text)


def token_count(text: str):
    # Returns the number of tokens in a string.
    return len(tokenize(text))


def decode(tokens):
    # Converts token IDs back into text.
    return _encoding.decode(tokens)
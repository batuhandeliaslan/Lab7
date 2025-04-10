def reverse_string(s):
    return s[::-1]

def capitalize_words(s):
    return ' '.join(word.capitalize() for word in s.split())

def remove_punctuation(s):
    import string
    return ''.join(ch for ch in s if ch not in string.punctuation)

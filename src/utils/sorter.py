def is_ukrainian(word):
    
    for ch in word.lower():
        if 'а' <= ch <= 'я' or ch in 'іїєґ':
            return True
    return False


def sort_words(words):
    
    return sorted(
        words,
        key=lambda w: (
            0 if is_ukrainian(w) else 1,  
            w.lower()                     
        )
    )
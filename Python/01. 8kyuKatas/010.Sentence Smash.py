def smash (words):
    
    return " ".join(words) if len(words) >= 1 else ""
    

print(smash(['hello', 'world', 'this', 'is', 'great']))
# >>> hello world this is great
def sortWelsh(words):
    letters = ["a", "b", "c", "ch", "d", "dd", "e", "f", "ff", "g", "ng", "h", "i", "j", "l", "ll", "m", "n", "o", "p", "r", "s", "t", "th", "u", "w", "y"]
    mapping = {}
    for i in range(len(letters)):
        mapping[letters[i]] = str(i)
    
    words_eq = {}
    for word in words:
        equivalent = []
        i = 0
        while i < len(word):
            if i < len(word) - 1 and word[i:i+2] in mapping:
                equivalent.append(mapping[word[i:i+2]])
                i += 1
            else:
                equivalent.append(mapping[word[i]])
            
            i += 1
        temp = ''.join(equivalent)
        words_eq[temp] = word
    
    temp = list(words_eq.keys())
    temp.sort()
    answer = []
    for key in temp:
        answer.append(words_eq[key])
    
    return answer

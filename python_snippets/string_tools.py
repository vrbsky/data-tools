def unique_words(word_list):
    unique = set(word_list)
    return list(unique)


def word_frequencies_1(word_list):
    freq = {}
    for w in word_list:
        freq[w] = 0
    
    for w in word_list:
        freq[w] += 1
    return freq

def word_frequencies_2(word_list):
    freq = {}
    for w in word_list:
        if w in freq.keys:
            freq[w] += 1
        else:
            freq[w] = 0
    return freq

def remove_subs(s, substring_list):
    for sub in substring_list:
        s = s.replace(sub,'')
    return s
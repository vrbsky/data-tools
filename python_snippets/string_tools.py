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

def series_get_text(s):
    print(type(s.values[0]))
    print(s.values[0])
    if type(s.values[0]) is np.ndarray:
        all_text = '\n'.join([item for sublist in s.fillna('').values for item in sublist])
    else:
        all_text = '\n'.join(s.fillna('').values)
    return all_text

def remove_accents(input_str):
    return u"".join([c for c in unicodedata.normalize('NFKD', input_str)
                     if not unicodedata.combining(c)])
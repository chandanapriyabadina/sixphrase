def compute_word_frequency(input_string):
    word_list = input_string.split()
    word_frequency = {}
    
    for word in word_list:
        word_frequency[word] = word_frequency.get(word, 0) + 1
    
    sorted_words = sorted(word_frequency.items(), key=lambda x: x[0])
    result = ' '.join([f'{word}:{count}' for word, count in sorted_words])
    

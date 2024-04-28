def uniqueMorseRepresentations(words):
    unique_code = set()
    decode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    for word in words:
        morse_word = ''
        for char in word:
            morse_word += decode[ord(char) - ord('a')]
        unique_code.add(morse_word)
    
    return len(unique_code)
            
words = ["gin","zen","gig","msg"]
print(uniqueMorseRepresentations(words))
# Supplementary Activity

# 1. Simple Word Filter
# Create a function that would accept two inputs: a sentence(string), and a list containing 
# bad words that the user would like to censor but not remove. 
# The function should return the newly filtered sentence wherein the bad words are replaced 
# with asterisks equal to the length of the censored word.

def word_filter(sentence, bad_words):
    filtered_sentence = sentence
    for word in bad_words:
        censored = '*' * len(word)
        filtered_sentence = filtered_sentence.replace(word, censored)
    return filtered_sentence

text = "Kadaphy is annoying as heck."
banned = ["annoying", "heck"]
print(word_filter(text, banned)) # Output: The quick brown *** is a ******.
# Read any given text as a string and then count the word frequency in  a dictionary

# the given any text
#----------------------------------------------------------------------------
textfile = "This!might be the new text for your of and quite!text_might"
#----------------------------------------------------------------------------

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]


new_file = ""
for t in textfile:
    if t.isalpha() == True and t!=" ":
        new_file = "{}{}".format(new_file,t)
    else:
        new_file = "{} ".format(new_file)
#print(new_file)

word_dict = {}

word_list = new_file.split()
for word in word_list:
    if word.lower() not in uninteresting_words:
        if word not in word_dict:
            word_dict[word] = 0
        word_dict[word] += 1

print(word_dict)

import random
import gensim.downloader as api
from blessings import Terminal

print("Loading model...")
model = api.load("word2vec-google-news-300")

def main(seed_word):
    term = Terminal()
    curr_word = seed_word
    used_words = [curr_word]
    done = False
    print("Starting...")
    while not done:
        candidates = [
            word for (word, score)
            in model.most_similar(curr_word)
            if word not in used_words and word.isalpha()
        ]
        if not candidates:
            done = True
        else:
            curr_word = candidates[0] #random.choice(candidates)
            used_words.append(curr_word)
        print(term.clear())
        print(curr_word)

if __name__ == "__main__":
    main()

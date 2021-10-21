import os
import asyncio
import websockets
from annoy import AnnoyIndex


class WordWalkServer:
    def __init__(self, index_fname, words_fname):
        self.index = AnnoyIndex(300, "angular")
        self.index.load(index_fname)
        self.words = open(words_fname).read().splitlines()
        self.word_to_index = {word: i for (i, word) in enumerate(self.words)}

    def similar_words(self, seed_word):
        curr_word = seed_word
        used_word_indices = [self.word_to_index[seed_word]]
        while True:
            candidates = [self.words[c] for c in
                          self.index.get_nns_by_item(self.word_to_index[curr_word], 10)
                          if c not in used_word_indices]
            if not candidates:
                return
            else:
                curr_word = candidates[0]
                used_word_indices.append(self.word_to_index[curr_word])
                yield curr_word

    async def handler(self, websocket, path):
        seed_word = await websocket.recv()
        print(f"Got seed word: {seed_word}")
        for word in self.similar_words(seed_word):
            print(f"Sending word to client: {word}")
            await websocket.send(word)

async def main():
    server = WordWalkServer(os.environ["WORD_WALK_INDEX_FILENAME"], os.environ["WORD_WALK_WORD_LIST_FILENAME"])
    async with websockets.serve(server.handler, "localhost", 8765):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())

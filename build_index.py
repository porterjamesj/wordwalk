import numpy
from annoy import AnnoyIndex

i = AnnoyIndex(300, "angular")

# Download this file from this repo: https://github.com/alexandres/lexvec
vectors_file = "lexvec.enwiki+newscrawl.300d.W.pos.vectors"

def main():
    print("Loading data...")
    data = numpy.loadtxt(
        vectors_file,
        skiprows=1,
        usecols=range(1,301)
    )

    index = AnnoyIndex(300, "angular")

    print("Building index...")
    for i in range(len(data)):
        index.add_item(i, data[i])
    index.build(10)

    print("Writing index...")
    index.save("index.ann")

if __name__ == "__main__":
    main()

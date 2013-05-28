
import sys
import nltk

if __name__ == "__main__":
    wsj = nltk.corpus.treebank.tagged_sents()
    foutTrain = open(sys.argv[1], 'w')
    foutTest = open(sys.argv[2], 'w')

    for sent in wsj:
        words = []
        tags = []
        for word, tag in sent:
            if word.find("*") == -1:
                words.append(word)
                tags.append(tag)
        line = ' '.join(words) + "\n"
        foutTrain.write(line)
        line = ' '.join(tags) + "\n"
        foutTest.write(line)
    
    foutTrain.close()
    foutTest.close()

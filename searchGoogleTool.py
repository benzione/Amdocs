import nltk
# try:
#     import re2 as re
# except ImportError:
#     import re
# else:
#     re.set_fallback_notification(re.FALLBACK_WARNING)
import sys
from spacy.en import English

if __name__ == '__main__':
    # read file
    f = open(sys.argv[1], 'r')
    text = f.read()
    f.close()

    nlp = English()
    doc = nlp(text)
    # for sent in doc:
    #     for token in sent:
    #         if token.is_alpha:
    #             print(token.orth_, token.tag_, token.head.lemma_)

    # split the text into sentences
    sentences = re.split(r'[.]', text)
    searchWords = []

    # run on each sentence in the text
    for sentence in sentences:
        # tag the any word in the sentence
        tag_sent = nltk.pos_tag(sentence.split())
        # choose specific words
        listwords = [word for word, pos in tag_sent if (pos == 'NN' or pos == 'NNS' or pos == 'NN' or pos == 'NNPS' or
                                                        pos == 'VB' or pos == 'VBD' or pos == 'VBG' or pos == 'VBN' or pos == 'VBP' or pos == 'VBZ' or
                                                        pos == 'RB' or pos == 'RBR' or pos == 'RBS')]

        # Build string for each sentnce for google search
        if listwords:
            strtmp = ''
            for i in listwords:
                strtmp = strtmp + i + ' + '

            strtmp = strtmp[:-3]
            searchWords.append(strtmp)

    print searchWords


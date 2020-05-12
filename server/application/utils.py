def get_sentences_from(text):
    return list(
      map(
        lambda sentence: sentence.strip(),
        filter(
          lambda sentence: len(sentence) > 0,
          text.strip().split('.')
        )
      )
    )


import gensim
from gensim.models import Word2Vec

def train_model(sentences):
    return Word2Vec(sentences, min_count=1, size=50, workers=3, window=3, sg=1)


def prepare_data_for_model(Sentence):
    sent = list(map(lambda s: s.as_dict(), Sentence.query.all()))

    m = {}
    for s in sent:
      if s['text_id'] in m:
        m[s['text_id']].append(s['content'])
      else:
        m[s['text_id']] = [s['content']]

    result = []
    for i in m.keys():
      result.append(m[i])

    return result

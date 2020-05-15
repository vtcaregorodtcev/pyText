from flask import jsonify
from gensim.models import Word2Vec
from .models import db, Sentence, Text


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


def get_text_by_sentence(sentence):
    # find it in db
    db_sent = db.session.query(Sentence).filter_by(content=sentence)

    sent_dict = db_sent[0].as_dict()

    # get text by this sentence
    sent_text = Text.query.get(sent_dict['text_id'])

    return sent_text.as_dict()


def jsonify_arr(arr):
    return jsonify(list(map(lambda row: row.as_dict(), arr)))


def to_db_sentences(sentences):
    return list(map(lambda sentence: Sentence(content=sentence), sentences))


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

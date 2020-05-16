from flask import jsonify
from gensim.models import Word2Vec
from .models import db, Sentence, Text

from nltk.tokenize import sent_tokenize, word_tokenize
import warnings

warnings.filterwarnings(action='ignore')

model_path = './db/trained_model.bin'


def get_text_by_sentence(sentence):
    # find it in db
    db_sent = db.session.query(Sentence).filter_by(content=sentence).first()

    sent_dict = db_sent.as_dict() if db_sent else None

    if sent_dict is None:
        return None

    # get text by this sentence
    sent_text = Text.query.get(sent_dict['text_id'])

    return sent_text.as_dict()


def jsonify_arr(arr):
    return jsonify(list(map(lambda row: row.as_dict(), arr)))


def to_db_sentences(sentences):
    return list(map(lambda sentence: Sentence(content=sentence), sentences))


def train_model(sentences):
    sample = open("./db/fairy_tale.txt", "r")
    s = sample.read()

    f = s.replace("\n", " ")

    data = []

    for i in sent_tokenize(f):
        temp = []

        for j in word_tokenize(i):
            temp.append(j.lower())

        data.append(temp)

    model = Word2Vec(data, min_count=1, size=100,
                     workers=3, window=5, sg=1)

    model.build_vocab(sentences, update=True)

    return model


def retrain_model(sentences):
    model = Word2Vec.load(model_path)
    model.build_vocab(sentences, update=True)
    model.save(model_path)

    return model


def prepare_data_for_model():
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

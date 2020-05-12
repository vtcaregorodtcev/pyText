from flask import jsonify, request, current_app as app, abort

from .models import db, Text, Sentence
from .utils import get_sentences_from, train_model, prepare_data_for_model

import json


model = train_model(prepare_data_for_model(Sentence))


@app.route('/textlist', methods=['GET', 'POST'])
def fetch_text_list():
    if request.method == 'GET':
        response = Text.query.all()
        return jsonify(list(map(lambda row: row.as_dict(), response)))
    else:
        text = json.loads(request.data)
        sentences = get_sentences_from(text['content'])

        if not (len(sentences) > 0 and text['title']):
            return abort(400, 'text must be filled')

        db_sentences = list(map(lambda sentence: Sentence(content=sentence), sentences))
        db_text = Text(title=text['title'], sentences=db_sentences)

        db.session.add(db_text)
        db.session.commit()

        return jsonify(db_text.as_dict())


@app.route('/textlist/<int:text_id>', methods=['GET'])
def fetch_text_by_id(text_id):
    text = Text.query.get(text_id)

    if not text:
        return abort(404, 'text not found')

    return jsonify(text.as_dict())


@app.route('/sentences/<int:text_id>', methods=['GET'])
def fetch_sentences(text_id):
    text = Text.query.get(text_id)

    if not text:
        return abort(404, 'text not found')

    response = db.session.query(Sentence).filter(Sentence.text_id == text_id)
    return jsonify(list(map(lambda row: row.as_dict(), response)))


@app.route('/sentences/<int:text_id>/related/<int:sentence_id>', methods=['GET'])
def fetch_related_sentences(text_id, sentence_id):
    text = Text.query.get(text_id)
    sentence = Sentence.query.get(sentence_id)

    if not text or not sentence:
        return abort(404, 'text or sentence not found')

    most_relevant_tuples = model.most_similar(sentence.as_dict()['content'])[:10]

    result_tuples = []
    for tup in most_relevant_tuples:
      sent = tup[0] # get relevant sentence

      res = db.session.query(Sentence).filter(Sentence.content == sent) # find it in db
      db_sent = list(map(lambda s: s.as_dict(), res))[0]

      sent_text = Text.query.get(db_sent['text_id']) # get text by this sentence

      result_tuples.append([sent, sent_text.as_dict(), tup[1]]) # return array

    return jsonify(result_tuples)

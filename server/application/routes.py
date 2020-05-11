from flask import jsonify
from flask import request
from flask import current_app as app

from .models import db, Text, Sentence
from .utils import get_sentences_from

import json


@app.route('/textlist', methods=['GET', 'POST'])
def fetch_text_list():
    if request.method == 'GET':
        response = Text.query.all()
        return jsonify(list(map(lambda row: row.as_dict(), response)))
    else:
        text = json.loads(request.data)
        sentences = get_sentences_from(text['content'])

        db_sentences = list(map(lambda sentence: Sentence(content=sentence), sentences))
        db_text = Text(title=text['title'], sentences=db_sentences)

        db.session.add(db_text)
        db.session.commit()

        return 'ok'

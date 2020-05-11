# start.sh

export FLASK_APP=wsgi.py
export FLASK_DEBUG=1
export SQLALCHEMY_DATABASE_URI=sqlite:///py_text.db
flask run

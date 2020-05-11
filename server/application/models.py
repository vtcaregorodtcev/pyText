from . import db

class Text(db.Model):
    """Data model for text item."""
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    title = db.Column(db.String(64),
                         index=True,
                         unique=False,
                         nullable=False)
    sentences = db.relationship("Sentence", back_populates="text")

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return '<Text {}>'.format(self.title)



class Sentence(db.Model):
    """Data model for sentence item."""
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    content = db.Column(db.Text,
                         index=True,
                         unique=False,
                         nullable=False)
    text_id = db.Column(db.Integer, db.ForeignKey('text.id'))
    text = db.relationship("Text", back_populates="sentences")

    def __repr__(self):
        return '<Text {}>'.format(self.content)

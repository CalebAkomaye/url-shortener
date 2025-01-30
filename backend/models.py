from app import db


class URI(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    short_uri = db.Column(db.String(50), nullable=False)
    main_uri = db.Column(db.String(100), nullable=False)


    def serialize_json(self):
        return{
            'id': self.id,
            'shortUri': self.short_uri,
            'main_uri': self.main_uri
        }

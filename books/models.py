from .extensions import db


class Publisher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    @classmethod
    def from_dict(cls, data):
        return Publisher(name=data['name'])

    def __repr__(self):
        return f'<Publisher: {self.name}>'


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    synopsis =db.Column(db.Text)
    published_date = db.Column(db.DateTime)
    publisher_id = db.Column(db.Integer, db.ForeignKey('publisher.id'), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'), nullable=False)

    @classmethod
    def from_dict(cls, data):
        return Book(title=data['title'],
                    synopsis=data['synopsis'],
                    published_date=data['published_date'],
                    publisher_id=data['publisher_id'],
                    author_id=data['author_id'],
                    genre_id=data['genre_id']
                    )

    def __repr__(self):
        return f'<Book: {self.title} {self.synopsis} {self.published_date} {self.publisher_id} {self.author_id} {self.genre_id}>'


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    @classmethod
    def from_dict(cls, data):
        return Author(name=data['name'])

    def __repr__(self):
        return f'<Author: {self.name}>'


class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    @classmethod
    def from_dict(cls, data):
        return Genre(name=data['name'])

    def __repr__(self):
        return f'<Genre: {self.name}>'

from flask import Blueprint, request, abort
from marshmallow.exceptions import ValidationError
from .models import Book, Author, Genre, Publisher
from .extensions import db
from .utils import make_api_result

from .schemas import publisher_schema, publishers_schema, \
    author_schema, authors_schema, book_schema, books_schema, \
    genre_schema, genres_schema, AuthorSchema, PublisherSchema, BookSchema, GenreSchema

api = Blueprint('api', __name__)


@api.errorhandler(400)
def bad_request(e):
    return {'error': e.description}, 400


@api.errorhandler(404)
def not_found(e):
    return {'error': 'not found'}, 404


@api.route('/books', methods=['GET'])
def get_books():
    return make_api_result(Book, BookSchema)


@api.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.query.get_or_404(book_id)
    return book_schema.dump(book)


@api.route('/books', methods=['POST'])
def create_book():
    json_data = request.get_json()

    try:
        # marshmallow validate the data.
        book = Book.from_dict(book_schema.load(json_data))
    except ValidationError as ex:
        abort(400, ex.messages)

    db.session.add(book)
    db.session.commit()

    return book_schema.dump(book)


@api.route('/books/<int:book_id>', methods=['PUT'])
def edit_book(book_id):
    json_data = request.get_json()

    try:
        book_data = book_schema.load(json_data, partial=True)
    except ValidationError as ex:
        abort(400, ex.messages)

    book_query = Book.query.filter_by(id=book_id)
    update_count = book_query.update(book_data)

    if update_count == 0:
        abort(404)

    db.session.commit()
    book = book_query.first()
    return book_schema.dump(book)


@api.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    del_count = Book.query.filter_by(id=book_id).delete()
    # delete method return the number of rows being deleted.
    if del_count == 0:
        abort(404)
    db.session.commit()
    return {}, 204


@api.route('/publishers', methods=['GET'])
def get_publishers():
    return make_api_result(Publisher, PublisherSchema)


@api.route('/publishers/<int:publisher_id>', methods=['GET'])
def get_publisher(publisher_id):
    publisher = Publisher.query.get_or_404(publisher_id)
    return publisher_schema.dump(publisher)


@api.route('/publishers', methods=['POST'])
def create_publisher():
    json_data = request.get_json()

    try:
        # marshmallow validate the data.
        publisher = Publisher.from_dict(publisher_schema.load(json_data))
    except ValidationError as ex:
        abort(400, ex.messages)

    db.session.add(publisher)
    db.session.commit()

    return publisher_schema.dump(publisher)


@api.route('/publishers/<int:publisher_id>', methods=['PUT'])
def edit_publisher(publisher_id):
    json_data = request.get_json()

    try:
        publisher_data = publisher_schema.load(json_data, partial=True)
    except ValidationError as ex:
        abort(400, ex.messages)

    publisher_query = Publisher.query.filter_by(id=publisher_id)
    update_count = publisher_query.update(publisher_data)

    if update_count == 0:
        abort(404)

    db.session.commit()
    publisher = publisher_query.first()
    return publisher_schema.dump(publisher)


@api.route('/publishers/<int:publisher_id>', methods=['DELETE'])
def delete_publisher(publisher_id):
    del_count = Publisher.query.filter_by(id=publisher_id).delete()
    # delete method return the number of rows being deleted.
    if del_count == 0:
        abort(404)
    db.session.commit()
    return {}, 204


@api.route('/authors', methods=['GET'])
def get_authors():
    return make_api_result(Author, AuthorSchema)


@api.route('/authors/<int:author_id>', methods=['GET'])
def get_author(author_id):
    author = Author.query.get_or_404(author_id)
    return author_schema.dump(author)


@api.route('/authors', methods=['POST'])
def create_author():
    json_data = request.get_json()

    try:
        # marshmallow validate the data.
        author = Author.from_dict(author_schema.load(json_data))
    except ValidationError as ex:
        abort(400, ex.messages)

    db.session.add(author)
    db.session.commit()

    return author_schema.dump(author)


@api.route('/authors/<int:author_id>', methods=['PUT'])
def edit_author(author_id):
    json_data = request.get_json()

    try:
        author_data = author_schema.load(json_data, partial=True)
    except ValidationError as ex:
        abort(400, ex.messages)

    author_query = Author.query.filter_by(id=author_id)
    update_count = author_query.update(author_data)

    if update_count == 0:
        abort(404)

    db.session.commit()
    author = author_query.first()
    return author_schema.dump(author)


@api.route('/authors/<int:author_id>', methods=['DELETE'])
def delete_author(author_id):
    del_count = Author.query.filter_by(id=author_id).delete()
    # delete method return the number of rows being deleted.
    if del_count == 0:
        abort(404)
    db.session.commit()
    return {}, 204


@api.route('/genres', methods=['GET'])
def get_genres():
    return make_api_result(Genre, GenreSchema)


@api.route('/genres/<int:genre_id>', methods=['GET'])
def get_genre(genre_id):
    genre = Genre.query.get_or_404(genre_id)
    return genre_schema.dump(genre)


@api.route('/genres', methods=['POST'])
def create_genre():
    json_data = request.get_json()

    try:
        # marshmallow validate the data.
        genre = Genre.from_dict(genre_schema.load(json_data))
    except ValidationError as ex:
        abort(400, ex.messages)

    db.session.add(genre)
    db.session.commit()

    return genre_schema.dump(genre)


@api.route('/genres/<int:genre_id>', methods=['PUT'])
def edit_genre(genre_id):
    json_data = request.get_json()

    try:
        genre_data = genre_schema.load(json_data, partial=True)
    except ValidationError as ex:
        abort(400, ex.messages)

    genre_query = Genre.query.filter_by(id=genre_id)
    update_count = genre_query.update(genre_data)

    if update_count == 0:
        abort(404)

    db.session.commit()
    genre = genre_query.first()
    return author_schema.dump(genre)


@api.route('/genres/<int:genre_id>', methods=['DELETE'])
def delete_genre(genre_id):
    del_count = Genre.query.filter_by(id=genre_id).delete()
    # delete method return the number of rows being deleted.
    if del_count == 0:
        abort(404)
    db.session.commit()
    return {}, 204

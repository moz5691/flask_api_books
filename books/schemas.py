from marshmallow import Schema, fields, EXCLUDE


class PublisherSchema(Schema):
    id = fields.Int()
    name = fields.Str()


class AuthorSchema(Schema):
    id = fields.Int()
    name = fields.Str()


class BookSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    synopsis = fields.Str()
    published_date = fields.DateTime(data_key="publishedDate")
    publisher_id = fields.Int(data_key="publisherId")
    genre_id = fields.Int(data_key="genreId")
    author_id = fields.Int(data_key="authorId")


class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()


class ApiSchema(Schema):
    page = fields.Int(missing=1)
    per_page = fields.Int(missing=5)
    exclude = fields.Str(missing="")
    sort_by_field = fields.Str(missing="id")
    sort_by_direction = fields.Str(missing="asc")

    class Meta:
        unknown = EXCLUDE


publisher_schema = PublisherSchema()
publishers_schema = PublisherSchema(many=True)
author_schema = AuthorSchema()
authors_schema = AuthorSchema(many=True)
book_schema = BookSchema()
books_schema = BookSchema(many=True)
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)
api_schema = ApiSchema()


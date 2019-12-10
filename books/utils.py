from flask import request, url_for
from marshmallow import EXCLUDE
from .schemas import api_schema


def make_api_result(model, schemaclass):
    """
    model:
    schema:
    """
    api_fields = api_schema.load(request.args)
    # print(api_fields)
    default_fields = api_schema.load({})
    # can check user provided field is different from default ones.
    supplied_fields = set(api_fields.items()) - set(default_fields.items())
    # default is : {'sort_by_direction': 'asc', 'page': 1, 'sort_by': 'id', 'per_page': 1, 'exclude': ''}
    result_query = model.query

    model_schema = schemaclass()
    model_fields = model_schema.load(request.args, unknown=EXCLUDE)
    print(model_fields)
    for field in model_fields:
        result_query = result_query.filter(getattr(model, field) == model_fields[field])

    # the format looks like this ;;;; order_by(Publisher.name.asc())
    # print(getattr(model, api_fields['sort_by_field']))
    # print(getattr(getattr(model, api_fields['sort_by_field']), api_fields['sort_by_direction'])())
    result_query = result_query.order_by(getattr(getattr(model, api_fields['sort_by_field']), api_fields['sort_by_direction'])())

    p = result_query.paginate(page=api_fields['page'], per_page=api_fields['per_page'])
    schema = schemaclass(many=True,
                         exclude=api_fields['exclude'].split(',') if api_fields['exclude'] else [])
    result = schema.dump(p.items)

    # supplied fields
    non_default_fields = {field[0]: field[1] for field in supplied_fields if field[0] != 'page' and field[0] != 'per_page'}

    if p.has_prev:
        prev_page = url_for(request.endpoint,
                            _external=True,
                            page=p.prev_num,
                            per_page=api_fields['per_page'],
                            **model_fields,
                            **non_default_fields
                            )
    else:
        prev_page = None

    if p.has_next:
        next_page = url_for(request.endpoint,
                            _external=True,
                            page=p.next_num,
                            per_page=api_fields['per_page'],
                            **model_fields,
                            **non_default_fields
                            )
    else:
        next_page = None

    return {
        "result": result,
        'count': p.total,
        'previous': prev_page,
        'next': next_page
    }


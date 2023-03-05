from webargs import fields

def_filter_args = {
    'page': fields.Int(required=False),
    'status': fields.Str(required=False),
}

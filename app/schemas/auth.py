from marshmallow import fields, Schema

class LoginSchema(Schema):
    # created_at is "read-only"
    email = fields.Str(required=True)
    password = fields.Str(required=True)
    id = fields.Int(dump_only=True)
    name = fields.Str(dump_only=True)
    phone = fields.Str(dump_only=True)

    

login_schema = LoginSchema()

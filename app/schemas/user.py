from marshmallow import fields, Schema

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True)
    name = fields.Str(required=True)
    phone = fields.Str(required=True)

class UserRegistrationSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Str(required=True)
    phone = fields.Str(required=True)
    password = fields.Str(required=True)

    #  password is only included at load but excluded at dump
    class Meta:
        load_only = ['password']

class UserDeleteSchema(Schema):
    id = fields.Int(required=True)

class UserEditSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str()
    email = fields.Str()
    phone = fields.Str()
    password = fields.Str()


user_schema = UserSchema()
user_edit_schema = UserEditSchema()
user_delete_schema = UserDeleteSchema()
user_registration_schema = UserRegistrationSchema()
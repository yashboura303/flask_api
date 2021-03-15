from marshmallow import Schema, fields
from marshmallow.validate import Length


class CreateCourseSchema(Schema):
    """ /api/note - POST

    Parameters:
     - title (str)
     - note (str)
     - user_id (int)
     - time_created (time)
    """
    title = fields.Str(required=True, error_messages={
                       "required": "title is required."},
                       validate=Length(max=100, min=5))
    image_path = fields.Str(required=False, validate=Length(max=100))
    description = fields.Str(required=False, validate=Length(max=255))
    discount_price = fields.Int(required=True, error_messages={
        "required": "discount_price is required."})
    price = fields.Int(required=True, error_messages={
        "required": "price is required."})
    on_discount = fields.Boolean(required=True, error_messages={
        "required": "on_discount is required."})
    id = fields.Int(required=False)

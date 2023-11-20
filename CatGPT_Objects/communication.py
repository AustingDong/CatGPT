from marshmallow import Schema, fields

class Communication:
    def __init__(self, text, language, sound):
        self.text = text
        self.language = language
        self.sound = sound

class CommunicationSchema(Schema):
    text = fields.Str(required=True)
    language = fields.Str(required=True)
    sound = fields.Bool(required=True)

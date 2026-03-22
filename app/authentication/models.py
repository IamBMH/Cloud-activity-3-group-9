from tortoise import fields, models

class User(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255, unique=True)
    address = fields.CharField(max_length=255, null=True)
    hashed_password = fields.CharField(max_length=255)

    class Meta:
        table = "users"

class Token(models.Model):
    id = fields.IntField(pk=True)
    token = fields.CharField(max_length=255, unique=True)
    user = fields.ForeignKeyField('models.User', related_name='tokens')

    class Meta:
        table = "tokens"
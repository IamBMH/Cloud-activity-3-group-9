from tortoise import fields, models


class File(models.Model):
    id = fields.IntField(pk=True)
    file_id = fields.CharField(max_length=255, unique=True)
    owner_email = fields.CharField(max_length=255)
    filename = fields.CharField(max_length=255)
    description = fields.TextField(null=True)
    content = fields.TextField(null=True)

    class Meta:
        table = "files"
from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=255)
    password = models.CharField(max_length=50)
    ship_to = models.CharField(max_length=50)
    card_info = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # オートでcreate_atしてない。update_atも同様

    class Meta:
        managed = True
        db_table = "user"
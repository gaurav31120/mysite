from django.db import models

# Create your mo(dels here.
# from food import Item ---- import food in shell
class Item(models.Model):

    def __str__(self):
        return self.item_name
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
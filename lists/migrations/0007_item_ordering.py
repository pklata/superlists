# Generated by Django 3.0.3 on 2020-05-02 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0006_list_item_unique_together'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('id',)},
        ),
    ]

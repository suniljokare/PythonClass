# Generated by Django 2.2 on 2021-01-16 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquiry', '0002_auto_20210116_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
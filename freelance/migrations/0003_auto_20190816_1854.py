# Generated by Django 2.2.3 on 2019-08-16 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelance', '0002_freereserve'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freereserve',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

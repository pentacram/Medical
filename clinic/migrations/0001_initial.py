# Generated by Django 2.2.3 on 2019-07-06 13:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Free_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='FreeDoctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', phone_field.models.PhoneField(max_length=31)),
                ('age', models.IntegerField()),
                ('info', models.TextField()),
                ('picture', models.ImageField(blank=True, null=True, upload_to='post1/')),
                ('catname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.Free_category')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('age', models.IntegerField(default=None)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', phone_field.models.PhoneField(help_text='Contact phone number', max_length=31, unique=True)),
                ('carrier', models.TextField()),
                ('picture', models.ImageField(blank=True, null=True, upload_to='post/')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', phone_field.models.PhoneField(help_text='Contact phone number', max_length=31, unique=True)),
                ('info', models.TextField()),
                ('photo', models.ImageField(blank=True, default='no-img.jpg', upload_to='media/clinic/images')),
                ('clinic_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='clinic_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.Clinic'),
        ),
    ]
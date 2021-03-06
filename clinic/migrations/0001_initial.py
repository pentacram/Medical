# Generated by Django 2.2.3 on 2019-08-17 12:39

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
            name='Reserve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('age', models.IntegerField(default=None)),
                ('date', models.DateField()),
                ('timeslot', models.IntegerField(choices=[(1, '09:00 – 10:00'), (2, '10:00 – 11:00'), (3, '11:00 – 12:00'), (4, '12:00 – 13:00'), (5, '13:00 – 14:00'), (6, '14:00 – 15:00'), (7, '15:00 – 16:00'), (8, '16:00 – 17:00'), (9, '17:00 – 18:00')])),
                ('contact_number', models.CharField(max_length=15)),
                ('comment', models.CharField(max_length=1000)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', phone_field.models.PhoneField(help_text='Contact phone number', max_length=31, unique=True)),
                ('info', models.TextField()),
                ('photo', models.ImageField(blank=True, default='no-img.jpg', upload_to='media/clinic/images')),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='clinic_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.Clinic'),
        ),
    ]

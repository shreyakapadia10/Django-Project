# Generated by Django 3.1.7 on 2021-03-07 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210307_0957'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('contact_id', models.AutoField(primary_key=True, serialize=False)),
                ('contact_name', models.CharField(max_length=50)),
                ('contact_email', models.CharField(max_length=50)),
                ('contact_phone', models.CharField(max_length=12)),
                ('contact_description', models.CharField(max_length=500)),
            ],
        ),
    ]
# Generated by Django 3.1.7 on 2021-03-12 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20210312_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderTracker',
            fields=[
                ('track_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField()),
                ('track_desc', models.CharField(max_length=5000)),
                ('track_timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]

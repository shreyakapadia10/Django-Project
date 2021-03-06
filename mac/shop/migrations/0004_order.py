# Generated by Django 3.1.7 on 2021-03-12 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_name', models.CharField(max_length=50)),
                ('order_email', models.CharField(max_length=50)),
                ('order_add', models.CharField(max_length=300)),
                ('order_phone', models.CharField(max_length=12)),
                ('order_city', models.CharField(max_length=50)),
                ('order_state', models.CharField(max_length=50)),
                ('order_pincode', models.IntegerField(max_length=6)),
                ('order_items', models.CharField(max_length=5000)),
            ],
        ),
    ]

# Generated by Django 5.1.1 on 2024-09-30 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kuwired_app', '0002_client_item_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

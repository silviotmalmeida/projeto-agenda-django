# Generated by Django 4.0.1 on 2022-01-25 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
    ]
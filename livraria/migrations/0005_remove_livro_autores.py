# Generated by Django 4.2 on 2023-09-25 19:21

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("livraria", "0004_livro_autores"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="livro",
            name="autores",
        ),
    ]

# Generated by Django 4.0.3 on 2022-04-25 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appTeste', '0005_rename_filme_acervo_filme_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='acervo',
            old_name='filme_id',
            new_name='filme',
        ),
        migrations.RenameField(
            model_name='acervo',
            old_name='usuario_id',
            new_name='usuario',
        ),
    ]

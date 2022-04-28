# Generated by Django 4.0.3 on 2022-04-27 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appTeste', '0008_remove_acervo_descricao_remove_acervo_rating_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='filme',
            name='foto',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='filme',
            name='titulo',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nome',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]

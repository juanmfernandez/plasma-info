# Generated by Django 3.0 on 2020-09-19 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='centrohabilitado',
            name='ciudad',
            field=models.CharField(blank=True, default='Resistencia', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='centrohabilitado',
            name='long_lat',
            field=models.CharField(blank=True, default='0000', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='fecha_publicacion',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='titulo',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='centrohabilitado',
            name='nro_tel',
            field=models.IntegerField(),
        ),
    ]
# Generated by Django 2.2.1 on 2019-08-06 23:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('autores', '0001_initial'),
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libros',
            fields=[
                ('book_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('published_date', models.DateField()),
                ('image', models.ImageField(upload_to='images')),
                ('autor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autores.Autors')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categorias.Categories')),
            ],
        ),
    ]

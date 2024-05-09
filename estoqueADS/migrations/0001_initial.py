# Generated by Django 4.2.11 on 2024-04-17 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=9)),
                ('descricao', models.TextField()),
                ('quantidade', models.IntegerField()),
                ('codigo', models.CharField(max_length=12)),
                ('em_estoque', models.BooleanField()),
                ('data_criacao', models.DateField()),
            ],
        ),
    ]
# Generated by Django 2.2.4 on 2019-08-01 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='equipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250)),
                ('coach', models.CharField(max_length=250)),
                ('performance', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='joueur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250)),
                ('prenom', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('solde', models.IntegerField()),
                ('mdpass', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.CharField(max_length=250)),
                ('mise', models.IntegerField()),
                ('gain', models.IntegerField()),
            ],
        ),
    ]

# Generated by Django 3.0.6 on 2020-05-12 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('slug', models.AutoField(help_text='PK AutoIncrement', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=300, null=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('views', models.IntegerField(max_length=100, null=True)),
                ('recommended', models.IntegerField(max_length=100, null=True)),
            ],
        ),
    ]

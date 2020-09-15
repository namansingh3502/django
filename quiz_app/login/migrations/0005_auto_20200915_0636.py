# Generated by Django 3.0.6 on 2020-09-15 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20200825_0631'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('username', models.CharField(max_length=128)),
                ('password', models.CharField(max_length=128)),
                ('token', models.CharField(max_length=128)),
                ('usertype', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Creator',
        ),
        migrations.DeleteModel(
            name='Participant',
        ),
    ]

# Generated by Django 3.2 on 2022-05-15 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testSolution', '0003_rename_fullname_user_full_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('image', models.URLField()),
                ('details', models.TextField()),
            ],
        ),
    ]

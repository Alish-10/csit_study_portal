# Generated by Django 4.0 on 2022-03-12 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MaterialRecommender', '0018_alter_member_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='dob',
            field=models.DateField(),
        ),
    ]

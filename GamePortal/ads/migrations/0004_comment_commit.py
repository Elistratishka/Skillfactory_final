# Generated by Django 4.0.5 on 2022-06-10 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_alter_comment_commentator'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='commit',
            field=models.BooleanField(default=False, verbose_name='Подтверждение'),
        ),
    ]
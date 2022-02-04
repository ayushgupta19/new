# Generated by Django 4.0.1 on 2022-02-04 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickreg', '0002_emailtemplate'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailtemplate',
            name='fields',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='emailtemplate',
            name='to',
            field=models.CharField(choices=[('gashu7320@gmail.com', 'Manager'), ('aayushgupta.gupta594@gmail.com', 'Assigner'), ('faqritesh@gmail.com', 'Creator')], default='gashu7320@gmail.com', max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='col',
            field=models.CharField(choices=[('gashu7320@gmail.com', 'Manager'), ('aayushgupta.gupta594@gmail.com', 'Assigner'), ('faqritesh@gmail.com', 'Creator')], default='gashu7320@gmail.com', max_length=50),
        ),
    ]
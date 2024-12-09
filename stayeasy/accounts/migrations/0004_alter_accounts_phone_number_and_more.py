# Generated by Django 5.1.1 on 2024-12-08 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_accounts_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='phone_number',
            field=models.CharField(blank=True, max_length=11),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='profile_picture',
            field=models.ImageField(default='images/iconProfileDefault.jpg', upload_to='profile_pictures/'),
        ),
    ]

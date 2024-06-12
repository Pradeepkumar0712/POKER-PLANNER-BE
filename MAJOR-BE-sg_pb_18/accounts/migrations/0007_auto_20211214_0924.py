# Generated by Django 2.2 on 2021-12-14 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20211213_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='groupinvitation',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='groupinvitation',
            name='verification',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commons.EmailVerification'),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='userjiratoken',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
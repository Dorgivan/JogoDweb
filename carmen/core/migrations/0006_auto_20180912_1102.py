# Generated by Django 2.0 on 2018-09-12 11:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0005_auto_20180912_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='pergunta',
            name='user',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='relaciona',
            name='relaciona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relacionas', to='core.Pergunta'),
        ),
    ]

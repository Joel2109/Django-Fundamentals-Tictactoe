# Generated by Django 2.0.3 on 2018-03-20 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameplay', '0002_game_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='move',
            old_name='Y',
            new_name='y',
        ),
        migrations.AlterField(
            model_name='game',
            name='status',
            field=models.CharField(choices=[('F', 'First Player To Move'), ('S', 'Second Player To Move'), ('W', 'First Player Wins'), ('L', 'Second Player Wins'), ('D', 'Draw')], default='F', max_length=1),
        ),
    ]

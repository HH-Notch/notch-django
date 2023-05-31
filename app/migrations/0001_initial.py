# Generated by Django 4.2.1 on 2023-05-31 00:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AfternoonBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('text', models.CharField(default='', max_length=50)),
                ('turn', models.IntegerField(default=1)),
                ('link', models.CharField(max_length=150, null=True)),
                ('sleep_time', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AfternoonNapMusicList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('link', models.CharField(default='', max_length=150)),
                ('nap_time', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AfternoonStudyMusicList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('link', models.CharField(default='', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='EveningBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('text', models.CharField(default='', max_length=50)),
                ('turn', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='EveningDiary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diary_turn', models.IntegerField(default=1)),
                ('brainer_turn', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='EveningSleepMusicList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('link', models.CharField(default='', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='GoodAfternoon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo_turn', models.IntegerField(default=1)),
                ('study_turn', models.IntegerField(default=1)),
                ('nap_turn', models.IntegerField(default=1)),
                ('sleep_turn', models.IntegerField(default=1)),
                ('sleep_time', models.IntegerField(default=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GoodEvening',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(default='', max_length=50)),
                ('today_feedback_turn', models.IntegerField(default=1)),
                ('tomorrow_brief_turn', models.IntegerField(default=1)),
                ('health_turn', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='GoodMorning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(default='', max_length=50)),
                ('weather_turn', models.IntegerField(default=1)),
                ('todo_turn', models.IntegerField(default=1)),
                ('music_turn', models.IntegerField(default=1)),
                ('pathfind_turn', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='MorningBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('text', models.CharField(default='', max_length=50)),
                ('turn', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='MorningDestList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('address', models.CharField(default='', max_length=100)),
                ('latitude', models.CharField(default='', max_length=20)),
                ('longtitude', models.CharField(default='', max_length=20)),
                ('link', models.CharField(default='', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='MorningMusicList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('link', models.CharField(default='', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(default='', max_length=254, unique=True, verbose_name='email address')),
                ('password', models.CharField(max_length=20)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
    ]

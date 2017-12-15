# Generated by Django 2.0 on 2017-12-15 09:56

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'district',
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('assessor_notes', models.TextField(blank=True, db_column='Assessor_notes', null=True)),
                ('datetime', models.DateTimeField()),
                ('location', models.CharField(max_length=45)),
                ('ref_comments', models.TextField(blank=True, db_column='Ref_comments', null=True)),
                ('age_group', models.CharField(choices=[('Adult', 'Adult'), ('Multi_Age', 'Multi-Age'), ('Senior', 'Senior'), ('u9', 'u9'), ('u10', 'u10'), ('u11', 'u11'), ('u12', 'u12'), ('u13', 'u13'), ('u14', 'u14'), ('u15', 'u15'), ('u16', 'u16'), ('u17', 'u17'), ('u18', 'u18'), ('u19', 'u19'), ('u20', 'u20'), ('u21', 'u21'), ('u22', 'u22')], db_column='age_group', max_length=10)),
                ('level', models.CharField(choices=[('comp', 'Competitive'), ('prem', 'Premier'), ('rec', 'Recreational'), ('scrim', 'Scrimmage')], db_column='level', max_length=10)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('C', 'Coed')], db_column='gender', max_length=10)),
            ],
            options={
                'db_table': 'game',
            },
        ),
        migrations.CreateModel(
            name='League',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'league',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('fname', models.CharField(db_column='fName', max_length=45)),
                ('lname', models.CharField(db_column='lName', max_length=45)),
                ('dob', models.DateField(db_column='DOB')),
            ],
            options={
                'db_table': 'person',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Personcontactinfo',
            fields=[
                ('email', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'personcontactinfo',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('number', models.SmallIntegerField()),
                ('fname', models.CharField(db_column='fName', max_length=45)),
                ('lname', models.CharField(db_column='lName', max_length=45)),
                ('age_group', models.CharField(choices=[('Adult', 'Adult'), ('Multi_Age', 'Multi-Age'), ('Senior', 'Senior'), ('u9', 'u9'), ('u10', 'u10'), ('u11', 'u11'), ('u12', 'u12'), ('u13', 'u13'), ('u14', 'u14'), ('u15', 'u15'), ('u16', 'u16'), ('u17', 'u17'), ('u18', 'u18'), ('u19', 'u19'), ('u20', 'u20'), ('u21', 'u21'), ('u22', 'u22')], db_column='age_group', max_length=10)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('C', 'Coed')], db_column='gender', max_length=10)),
                ('level', models.CharField(choices=[('comp', 'Competitive'), ('prem', 'Premier'), ('rec', 'Recreational'), ('scrim', 'Scrimmage')], db_column='level', max_length=10)),
            ],
            options={
                'db_table': 'player',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'state',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('name', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('C', 'Coed')], db_column='gender', max_length=10)),
                ('age_group', models.CharField(choices=[('Adult', 'Adult'), ('Multi_Age', 'Multi-Age'), ('Senior', 'Senior'), ('u9', 'u9'), ('u10', 'u10'), ('u11', 'u11'), ('u12', 'u12'), ('u13', 'u13'), ('u14', 'u14'), ('u15', 'u15'), ('u16', 'u16'), ('u17', 'u17'), ('u18', 'u18'), ('u19', 'u19'), ('u20', 'u20'), ('u21', 'u21'), ('u22', 'u22')], db_column='age_group', max_length=10)),
                ('level', models.CharField(choices=[('comp', 'Competitive'), ('prem', 'Premier'), ('rec', 'Recreational'), ('scrim', 'Scrimmage')], db_column='level', max_length=10)),
            ],
            options={
                'db_table': 'team',
            },
        ),
        migrations.CreateModel(
            name='Addresses',
            fields=[
                ('person', models.ForeignKey(db_column='Person_Id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='refdb.Person')),
                ('city', models.CharField(max_length=60)),
                ('state', models.CharField(choices=[('Alabama', 'Alabama'), ('Alaska', 'Alaska'), ('Arizona', 'Arizona'), ('Arkansas', 'Arkansas'), ('California', 'California'), ('Colorado', 'Colorado'), ('Connecticut', 'Connecticut'), ('Delaware', 'Delaware'), ('Florida', 'Florida'), ('Georgia', 'Georgia'), ('Hawaii', 'Hawaii'), ('Idaho', 'Idaho'), ('Illinois', 'Illinois'), ('Indiana', 'Indiana'), ('Iowa', 'Iowa'), ('Kansas', 'Kansas'), ('Kentucky', 'Kentucky'), ('Louisiana', 'Louisiana'), ('Maine', 'Maine'), ('Maryland', 'Maryland'), ('Massachusetts', 'Massachusetts'), ('Michigan', 'Michigan'), ('Minnesota', 'Minnesota'), ('Mississippi', 'Mississippi'), ('Missouri', 'Missouri'), ('Montana', 'Montana'), ('Nebraska', 'Nebraska'), ('Nevada', 'Nevada'), ('New_Hampshire', 'New Hampshire'), ('New_Jersey', 'New Jersey'), ('New_Mexico', 'New Mexico'), ('New_York', 'New York'), ('North_Carolina', 'North Carolina'), ('North_Dakota', 'North Dakota'), ('Ohio', 'Ohio'), ('Oklahoma', 'Oklahoma'), ('Oregon', 'Oregon'), ('Pennsylvania', 'Pennsylvania'), ('Rhode_Island', 'Rhode Island'), ('Shouth_Carolina', 'South Carolina'), ('South_Dakota', 'South Dakota'), ('Tennessee', 'Tennessee'), ('Texas', 'Texas'), ('Utah', 'Utah'), ('Vermont', 'Vermont'), ('Virginia', 'Virginia'), ('Washington', 'Washington'), ('West_Virginia', 'West Virginia'), ('Wisconsin', 'Wisconsin'), ('Wyoming', 'Wyoming')], db_column='state', max_length=20)),
                ('street_addr', models.CharField(max_length=50)),
                ('zip', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'addresses',
            },
        ),
        migrations.CreateModel(
            name='Assessor',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='refdb.Person')),
                ('good_standing', models.IntegerField(choices=[(1, 'yes'), (0, 'no')])),
                ('grade', models.IntegerField()),
            ],
            options={
                'db_table': 'assessor',
            },
            bases=('refdb.person',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Assignor',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='refdb.Person')),
                ('good_standing', models.IntegerField(choices=[(1, 'yes'), (0, 'no')])),
                ('grade', models.IntegerField()),
            ],
            options={
                'db_table': 'assignor',
            },
            bases=('refdb.person',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Cautions',
            fields=[
                ('game', models.ForeignKey(db_column='Game_Id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='refdb.Game')),
                ('reason', models.CharField(choices=[('DRP', 'Delaying the Restart of Play'), ('DISS', 'Dissent by Word or Action'), ('EL', 'Entering or Leaving the Field Without Permission'), ('FRD', 'Failure to Respect the Required Distance'), ('PI', 'Persistant Infringement of the Laws of the Game'), ('UB', 'Unsporting Behavior')], db_column='reason', max_length=10)),
                ('player_number', models.SmallIntegerField(db_column='Player_number')),
                ('second_caution', models.IntegerField(choices=[(1, 'yes'), (0, 'no')])),
            ],
            options={
                'db_table': 'cautions',
            },
        ),
        migrations.CreateModel(
            name='GameHasReferee',
            fields=[
                ('game', models.ForeignKey(db_column='Game_Id', on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='refdb.Game')),
                ('position', models.CharField(choices=[('Ctr', 'Center'), ('AR1', 'AR1'), ('AR2', 'AR2'), ('fourth', '4th Official')], max_length=10)),
            ],
            options={
                'db_table': 'game_has_referee',
            },
        ),
        migrations.CreateModel(
            name='Goals',
            fields=[
                ('game', models.ForeignKey(db_column='Game_Id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='refdb.Game')),
                ('scoring_team', models.CharField(db_column='scoring_Team', max_length=45)),
                ('player_number', models.SmallIntegerField(db_column='Player_number')),
                ('minute', models.SmallIntegerField()),
            ],
            options={
                'db_table': 'goals',
            },
        ),
        migrations.CreateModel(
            name='Guardians',
            fields=[
                ('person', models.ForeignKey(db_column='Person_Id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='refdb.Person')),
                ('fname', models.CharField(db_column='fName', max_length=45)),
                ('lname', models.CharField(db_column='lName', max_length=45)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'guardians',
            },
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='refdb.Person')),
                ('good_standing', models.IntegerField(choices=[(1, 'yes'), (0, 'no')])),
                ('grade', models.IntegerField()),
            ],
            options={
                'db_table': 'instructor',
            },
            bases=('refdb.person',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='LeagueHasReferee',
            fields=[
                ('league_name', models.ForeignKey(db_column='League_name', on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='leagueRef_league', serialize=False, to='refdb.League')),
            ],
            options={
                'db_table': 'league_has_referee',
            },
        ),
        migrations.CreateModel(
            name='Referee',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='refdb.Person')),
                ('grade', models.IntegerField()),
                ('field_training', models.IntegerField(choices=[(1, 'yes'), (0, 'no')])),
                ('paid', models.IntegerField(choices=[(1, 'yes'), (0, 'no')])),
                ('suspended', models.IntegerField(choices=[(1, 'yes'), (0, 'no')])),
                ('received_badge', models.IntegerField(choices=[(1, 'yes'), (0, 'no')])),
                ('last_certified', models.DateField()),
            ],
            options={
                'db_table': 'referee',
            },
            bases=('refdb.person',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Sendoffs',
            fields=[
                ('game', models.ForeignKey(db_column='Game_Id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='refdb.Game')),
                ('reason', models.CharField(choices=[('DOGSOH', 'Denying an Obvious Goal-Scoring Opportunity by Handling'), ('DOGSOFK', 'Denying an Obvious Goal-Scoring Opportunity by a Free-Kick Offense'), ('SFP', 'Serious Foul Play'), ('SP', 'Spitting at a Person'), ('VC', 'Violent Conduct'), ('LANG', 'Offensive, Insulting, or Abusive Language or Gesture'), ('CAUT', 'Receiving a Second Caution')], db_column='reason', max_length=10)),
                ('player_number', models.SmallIntegerField(db_column='Player_number')),
                ('report', models.TextField()),
            ],
            options={
                'db_table': 'sendoffs',
            },
        ),
        migrations.AddField(
            model_name='player',
            name='team_name',
            field=models.ForeignKey(db_column='Team_name', on_delete=django.db.models.deletion.PROTECT, to='refdb.Team'),
        ),
        migrations.AddField(
            model_name='personcontactinfo',
            name='person',
            field=models.ForeignKey(db_column='Person_Id', on_delete=django.db.models.deletion.CASCADE, to='refdb.Person'),
        ),
        migrations.AddField(
            model_name='person',
            name='district_name',
            field=models.ForeignKey(db_column='district_name', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='person_district', to='refdb.District'),
        ),
        migrations.AddField(
            model_name='person',
            name='state_name',
            field=models.ForeignKey(db_column='State_name', null=True, on_delete=django.db.models.deletion.SET_NULL, to='refdb.District'),
        ),
        migrations.AddField(
            model_name='league',
            name='district_name',
            field=models.ForeignKey(db_column='District_name', on_delete=django.db.models.deletion.CASCADE, related_name='league_district', to='refdb.District'),
        ),
        migrations.AddField(
            model_name='league',
            name='state_name',
            field=models.ForeignKey(db_column='State_name', on_delete=django.db.models.deletion.CASCADE, to='refdb.District'),
        ),
        migrations.AddField(
            model_name='game',
            name='home_team_name',
            field=models.ForeignKey(db_column='home_Team_name', on_delete=django.db.models.deletion.PROTECT, related_name='was_home', to='refdb.Team'),
        ),
        migrations.AddField(
            model_name='game',
            name='league_name',
            field=models.ForeignKey(db_column='League_name', null=True, on_delete=django.db.models.deletion.SET_NULL, to='refdb.League'),
        ),
        migrations.AddField(
            model_name='game',
            name='visiting_team_name',
            field=models.ForeignKey(db_column='visiting_Team_name', on_delete=django.db.models.deletion.PROTECT, related_name='was_visitor', to='refdb.Team'),
        ),
        migrations.AddField(
            model_name='district',
            name='state_name',
            field=models.ForeignKey(db_column='state_name', on_delete=django.db.models.deletion.CASCADE, to='refdb.State'),
        ),
        migrations.CreateModel(
            name='RefereeTestScores',
            fields=[
                ('referee_person', models.ForeignKey(db_column='Referee_Person_Id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='refdb.Referee')),
                ('grade9', models.IntegerField(blank=True, null=True)),
                ('grade8', models.IntegerField(blank=True, null=True)),
                ('grade7', models.IntegerField(blank=True, null=True)),
                ('grade6', models.IntegerField(blank=True, null=True)),
                ('grade5', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'referee_test_scores',
            },
        ),
        migrations.AddField(
            model_name='sendoffs',
            name='player',
            field=models.ForeignKey(db_column='Player_id', on_delete=django.db.models.deletion.CASCADE, to='refdb.Player'),
        ),
        migrations.AddField(
            model_name='referee',
            name='last_certifying_instructor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='refdb.Instructor'),
        ),
        migrations.AlterUniqueTogether(
            name='personcontactinfo',
            unique_together={('person', 'email', 'phone')},
        ),
        migrations.AddField(
            model_name='leaguehasreferee',
            name='league_district_name',
            field=models.ForeignKey(db_column='League_district_name', on_delete=django.db.models.deletion.CASCADE, related_name='leagueRef_district', to='refdb.League'),
        ),
        migrations.AddField(
            model_name='leaguehasreferee',
            name='league_state_name',
            field=models.ForeignKey(db_column='League_state_name', on_delete=django.db.models.deletion.CASCADE, to='refdb.League'),
        ),
        migrations.AddField(
            model_name='leaguehasreferee',
            name='referee',
            field=models.ForeignKey(db_column='Referee_Id', on_delete=django.db.models.deletion.CASCADE, to='refdb.Referee'),
        ),
        migrations.AddField(
            model_name='league',
            name='primary_assignor',
            field=models.ForeignKey(db_column='primary_Assignor_Id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='refdb.Assignor'),
        ),
        migrations.AlterUniqueTogether(
            name='guardians',
            unique_together={('person', 'fname', 'lname')},
        ),
        migrations.AlterUniqueTogether(
            name='goals',
            unique_together={('game', 'scoring_team', 'minute')},
        ),
        migrations.AddField(
            model_name='gamehasreferee',
            name='referee',
            field=models.ForeignKey(db_column='Referee_Id', on_delete=django.db.models.deletion.PROTECT, to='refdb.Referee'),
        ),
        migrations.AddField(
            model_name='game',
            name='assessor',
            field=models.ForeignKey(blank=True, db_column='Assessor_Id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='refdb.Assessor'),
        ),
        migrations.AddField(
            model_name='game',
            name='assignor',
            field=models.ForeignKey(db_column='Assignor_Id', on_delete=django.db.models.deletion.PROTECT, to='refdb.Assignor'),
        ),
        migrations.AlterUniqueTogether(
            name='district',
            unique_together={('name', 'state_name')},
        ),
        migrations.AddField(
            model_name='cautions',
            name='player',
            field=models.ForeignKey(db_column='Player_id', on_delete=django.db.models.deletion.CASCADE, to='refdb.Player'),
        ),
        migrations.AlterUniqueTogether(
            name='sendoffs',
            unique_together={('game', 'player')},
        ),
        migrations.AlterUniqueTogether(
            name='leaguehasreferee',
            unique_together={('league_name', 'league_district_name', 'league_state_name', 'referee')},
        ),
        migrations.AlterUniqueTogether(
            name='league',
            unique_together={('name', 'district_name', 'state_name')},
        ),
        migrations.AlterUniqueTogether(
            name='gamehasreferee',
            unique_together={('game', 'referee')},
        ),
        migrations.AlterUniqueTogether(
            name='cautions',
            unique_together={('game', 'player', 'second_caution')},
        ),
    ]

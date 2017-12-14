# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#  y * Rearrange models' order
#  y * Make sure each model has one field with primary_key=True
# y  * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#  y * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

BOOL_CHOICES = (
    (1, 'yes'),
    (0, 'no'),
)

LEVEL_CHOICES = (
    (comp, 'Competitive'),
    (Prem, 'Premier'),
    (Rec, 'Recreational'),
    (Scrim, 'Scrimmage'),
)

AGE_CHOICES = (
    (Adult, 'Adult'),
    (Multi_Age, 'Multi-Age'),
    (Senior, 'Senior'),
    (u9, 'u9'),
    (u10, 'u10'),
    (u11, 'u11'),
    (u12, 'u12'),
    (u13, 'u13'),
    (u14, 'u14'),
    (u15, 'u15'),
    (u16, 'u16'),
    (u17, 'u17'),
    (u18, 'u18'),
    (u19, 'u19'),
    (u20, 'u20'),
    (u21, 'u21'),
    (u22, 'u22'),
)

CAUTION_CHOICES = (
    (DRP, 'Delaying the Restart of Play'),
    (DISS, 'Dissent by Word or Action'),
    (EL, 'Entering or Leaving the Field Without Permission'),
    (FRD, 'Failure to Respect the Required Distance'),
    (PI, 'Persistant Infringement of the Laws of the Game'),
    (UB, 'Unsporting Behavior'),
)

SENDOFF_CHOICES = (
    (DOGSOH, 'Denying an Obvious Goal-Scoring Opportunity by Handling'),
    (DOGSOFK, 'Denying an Obvious Goal-Scoring Opportunity by a Free-Kick Offense'),
    (SFP, 'Serious Foul Play'),
    (SP, 'Spitting at a Person'),
    (VC, 'Violent Conduct'),
    (LANG, 'Offensive, Insulting, or Abusive Language or Gesture'),
    (CAUT, 'Receiving a Second Caution'),
)

POSITION_CHOICES = (
    (Ctr, 'Center'),
    (AR1, 'AR1'),
    (AR2, 'AR2'),
    (fourth, '4th Official'),
)

STATE_CHOICES = (
    (Alabama, 'Alabama'),
    (Alaska, 'Alaska'),
    (Arizona, 'Arizona'),
    (Arkansas, 'Arkansas'),
    (California, 'California'),
    (Colorado, 'Colorado'),
    (Connecticut, 'Connecticut'),
    (Delaware, 'Delaware'),
    (Florida, 'Florida'),
    (Georgia, 'Georgia'),
    (Hawaii, 'Hawaii'),
    (Idaho, 'Idaho'),
    (Illinois, 'Illinois'),
    (Indiana, 'Indiana'),
    (Iowa, 'Iowa'),
    (Kansas, 'Kansas'),
    (Kentucky, 'Kentucky'),
    (Louisiana, 'Louisiana'),
    (Maine, 'Maine'),
    (Maryland, 'Maryland'),
    (Massachusetts, 'Massachusetts'),
    (Michigan, 'Michigan'),
    (Minnesota, 'Minnesota'),
    (Mississippi, 'Mississippi'),
    (Missouri, 'Missouri'),
    (Montana, 'Montana'),
    (Nebraska, 'Nebraska'),
    (Nevada, 'Nevada'),
    (New_Hampshire, 'New Hampshire'),
    (New_Jersey, 'New Jersey'),
    (New_Mexico, 'New Mexico'),
    (New_York, 'New York'),
    (North_Carolina, 'North Carolina'),
    (North_Dakota, 'North Dakota'),
    (Ohio, 'Ohio'),
    (Oklahoma, 'Oklahoma'),
    (Oregon, 'Oregon'),
    (Pennsylvania, 'Pennsylvania'),
    (Rhode_Island, 'Rhode Island'),
    (Shouth_Carolina, 'South Carolina'),
    (South_Dakota, 'South Dakota'),
    (Tennessee, 'Tennessee'),
    (Texas, 'Texas'),
    (Utah, 'Utah'),
    (Vermont, 'Vermont'),
    (Virginia, 'Virginia'),
    (Washington, 'Washington'),
    (West_Virginia, 'West Virginia'),
    (Wisconsin, 'Wisconsin'),
    (Wyoming, 'Wyoming'),
)

class Team(models.Model):
    name = models.CharField(primary_key=True, max_length=45)
    gender = models.CharField(db_column='gender', choices=GENDER_CHOICES)
    age_group = models.CharField(db_column='age_group', choices=AGE_CHOICES)
    level = models.CharField(db_column='level', choices=LEVEL_CHOICES)

    class Meta:
        db_table = 'team'

class Player(models.Model):
    id = models.AutoField(db_column = 'Id', primary_key=True)
    number = models.SmallIntegerField()
    fname = models.CharField(db_column='fName', max_length=45)  # Field name made lowercase.
    lname = models.CharField(db_column='lName', max_length=45)  # Field name made lowercase.
    team_name = models.ForeignKey('Team', models.SET_NULL, db_column='Team_name')  # Field name made lowercase.
    age_group = models.CharField(db_column='age_group', choices=AGE_CHOICES)
    gender = models.CharField(db_column='gender', choices=GENDER_CHOICES)
    level = models.CharField(db_column='level', choices=LEVEL_CHOICES)

    class Meta:
        db_table = 'player'


class State(models.Model):
    name = models.CharField(primary_key=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'state'

class Person(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    fname = models.CharField(db_column='fName', max_length=45)  # Field name made lowercase.
    lname = models.CharField(db_column='lName', max_length=45)  # Field name made lowercase.
    dob = models.DateField(db_column='DOB')  # Field name made lowercase.
    district_name = models.ForeignKey(District, models.SET_NULL, db_column='district_name')
    state_name = models.ForeignKey(District, models.SET_NULL, db_column='State_name')  # Field name made lowercase.

    class Meta:
        db_table = 'person'

class Addresses(models.Model):
    person = models.ForeignKey('Person', models.CASCADE, db_column='Person_Id', primary_key=True)  # Field name made lowercase.
    city = models.CharField(max_length=60)
    state = models.CharField(db_column='state', choices=STATE_CHOICES)
    street_addr = models.CharField(max_length=50)
    zip = models.CharField(max_length=15)

    class Meta:
        db_table = 'addresses'


class Assessor(Person):
    good_standing = models.IntegerField(choices=BOOL_CHOICES)
    grade = models.IntegerField()

    class Meta:
        db_table = 'assessor'


class Assignor(Person):
    good_standing = models.IntegerField(choices=BOOL_CHOICES)
    grade = models.IntegerField()

    class Meta:

        db_table = 'assignor'

class Instructor(Person):
    person = models.ForeignKey('Person', models.CASCADE, db_column='Person_Id', primary_key=True)  # Field name made lowercase.
    good_standing = models.IntegerField(choices=BOOL_CHOICES)
    grade = models.IntegerField()

    class Meta:
        db_table = 'instructor'

class Referee(Person):
    grade = models.IntegerField()
    field_training = models.IntegerField(choices=BOOL_CHOICES)
    paid = models.IntegerField(choices=BOOL_CHOICES)
    suspended = models.IntegerField(choices=BOOL_CHOICES)
    received_badge = models.IntegerField(choices=BOOL_CHOICES)
    last_certified = models.DateField()
    last_certifying_instructor = models.ForeignKey(Instructor, models.RESTRICT)

    class Meta:
        db_table = 'referee'


class District(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    state_name = models.ForeignKey('State', models.CASCADE, db_column='state_name')

    class Meta:
        db_table = 'district'
        unique_together = (('name', 'state_name'),)

class League(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    district_name = models.ForeignKey(District, models.CASCADE, db_column='District_name', primary_key=True)  # Field name made lowercase.
    state_name = models.ForeignKey(District, models.CASCADE, db_column='State_name', primary_key=True)  # Field name made lowercase.
    primary_assignor = models.ForeignKey(Assignor, models.SET_NULL, db_column='primary_Assignor_Id')  # Field name made lowercase.

    class Meta:
        db_table = 'league'
        unique_together = (('name', 'district_name', 'state_name'),)


class Game(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    league_name = models.ForeignKey('League', models.SET_NULL, db_column='League_name')  # Field name made lowercase.
    assignor = models.ForeignKey(Assignor, models.RESTRICT, db_column='Assignor_Id')  # Field name made lowercase.
    assessor = models.ForeignKey(Assessor, models.SET_NULL, db_column='Assessor_Id', blank=True, null=True)  # Field name made lowercase.
    assessor_notes = models.TextField(db_column='Assessor_notes', blank=True, null=True)  # Field name made lowercase.
    home_team_name = models.ForeignKey('Team', models.RESTRICT, db_column='home_Team_name')  # Field name made lowercase.
    visiting_team_name = models.ForeignKey('Team', models.RESTRICT, db_column='visiting_Team_name')  # Field name made lowercase.
    datetime = models.DateTimeField()
    location = models.CharField(max_length=45)
    ref_comments = models.TextField(db_column='Ref_comments', blank=True, null=True)  # Field name made lowercase.
    age_group = models.CharField(db_column='age_group', choices=AGE_CHOICES)
    level = models.CharField(db_column='level', choices=LEVEL_CHOICES)
    gender = models.CharField(db_column='gender', choices=GENDER_CHOICES)

    class Meta:
        db_table = 'game'

class Cautions(models.Model):
    game = models.ForeignKey('Game', models.CASCADE, db_column='Game_Id', primary_key=True)  # Field name made lowercase.
    player = models.ForeignKey('Player', models.CASCADE, db_column='Player_id')  # Field name made lowercase.
    reason = models.CharField(db_column='reason', choices=CAUTION_CHOICES)
    player_number = models.SmallIntegerField(db_column='Player_number')  # Field name made lowercase.
    second_caution = models.IntegerField(choces=BOOL_CHOICES)

    class Meta:
        db_table = 'cautions'
        unique_together = (('game', 'player', 'second_caution'),)


class GameHasReferee(models.Model):
    game = models.ForeignKey(Game, models.RESTRICT, db_column='Game_Id', primary_key=True)  # Field name made lowercase.
    referee = models.ForeignKey('Referee', models.RESTRICT, db_column='Referee_Id')  # Field name made lowercase.
    position = models.CharField(max_length=10, choices=POSITION_CHOICES)

    class Meta:
        db_table = 'game_has_referee'
        unique_together = (('game', 'referee'),)

class Goals(models.Model):
    game = models.ForeignKey(Game, models.CASCADE, db_column='Game_Id', primary_key=True)  # Field name made lowercase.
    scoring_team = models.CharField(db_column='scoring_Team', max_length=45, primary_key=True)  # Field name made lowercase.
    player_number = models.SmallIntegerField(db_column='Player_number')  # Field name made lowercase.
    minute = models.SmallIntegerField(primary_key=True)

    class Meta:
        db_table = 'goals'


class Guardians(models.Model):
    person = models.ForeignKey('Person', models.CASCADE, db_column='Person_Id', primary_key=True)  # Field name made lowercase.
    fname = models.CharField(db_column='fName', max_length=45, primary_key=True)  # Field name made lowercase.
    lname = models.CharField(db_column='lName', max_length=45, primary_key=True)  # Field name made lowercase.
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)

    class Meta:
        db_table = 'guardians'


class LeagueHasReferee(models.Model):
    league_name = models.ForeignKey(League, models.CASCADE, db_column='League_name', primary_key=True)  # Field name made lowercase.
    league_district_name = models.ForeignKey(League, models.CASCADE, db_column='League_district_name')  # Field name made lowercase.
    league_state_name = models.ForeignKey(League, models.CASCADE, db_column='League_state_name')  # Field name made lowercase.
    referee = models.ForeignKey('Referee', models.CASCADE, db_column='Referee_Id', primary_key=True)  # Field name made lowercase.

    class Meta:
        db_table = 'league_has_referee'
        unique_together = (('league_name', 'league_district_name', 'league_state_name', 'referee'),)


class Personcontactinfo(models.Model):
    person = models.ForeignKey(Person, models.CASCADE, db_column='Person_Id', primary_key=True)
    email = models.CharField(max_length=50, primary_key=True)
    phone = models.CharField(max_length=15, primary_key=True)

    class Meta:
        db_table = 'personcontactinfo'


class RefereeTestScores(models.Model):
    referee_person = models.ForeignKey(Referee, models.CASCADE, db_column='Referee_Person_Id', primary_key=True)  # Field name made lowercase.
    grade9 = models.IntegerField(blank=True, null=True)
    grade8 = models.IntegerField(blank=True, null=True)
    grade7 = models.IntegerField(blank=True, null=True)
    grade6 = models.IntegerField(blank=True, null=True)
    grade5 = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'referee_test_scores'

class Sendoffs(models.Model):
    game = models.ForeignKey(Game, models.CASCADE, db_column='Game_Id', primary_key=True)  # Field name made lowercase.
    player = models.ForeignKey(Player, models.SET_NULL, db_column='Player_id', primary_key=True)  # Field name made lowercase.
    reason = models.CharField(db_column='reason', choices=SENDOFF_CHOICES)
    player_number = models.SmallIntegerField(db_column='Player_number')  # Field name made lowercase.
    report = models.TextField()

    class Meta:
        db_table = 'sendoffs'
        unique_together = (('game', 'player'),)

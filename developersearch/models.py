from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.


class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=254, unique=True, null=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'programming_languages'


class Language(models.Model):
    code = models.CharField(max_length=254, unique=True, null=False)

    def __str__(self):
        return self.code

    class Meta:
        db_table = 'languages'


class Developer(models.Model):
    email = models.EmailField(max_length=254, unique=True, null=False)
    programming_languages = models.ManyToManyField(ProgrammingLanguage)
    languages = models.ManyToManyField(Language)

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'developers'


class Interview(models.Model):
    score = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(max_length=500)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)

    class Meta:
        db_table = 'interviews'

from django.db import models
from django_countries.fields import CountryField


class Degree(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Subject(models.Model):
    subject = models.CharField(max_length=50)

    def __str__(self):
        return self.subject


class Spiecification(models.Model):
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.subject.subject} - {self.degree.name}'


class Service(models.Model):
    service = models.CharField(max_length=50)
    spiecification = models.ForeignKey(
        Spiecification, on_delete=models.CASCADE, related_name='spiecification_service', blank=True,null=True)

    def __str__(self):
        return f'{self.service} - {self.spiecification.degree.name} - {self.spiecification.subject.subject}'


class Project(models.Model):
    project = models.CharField(max_length=50)
    spiecification = models.ForeignKey(Spiecification, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.project} - {self.spiecification}"


class TaskProject(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="taskproject")
    task = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.task} - {self.project.project}'


class Country(models.Model):
    country = CountryField()

    def __str__(self):
        return self.country.name


class Bank(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    Bank = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.Bank


class NumberAccount(models.Model):
    Bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    NumberOfAccount = models.IntegerField()
    NameOfAccount = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.Bank.Bank} - account -{self.pk}'

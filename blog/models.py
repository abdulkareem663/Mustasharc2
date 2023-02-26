from django.db import models
from Center.models import *
from ckeditor.fields import RichTextField

class SEO(models.Model):
    head= models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    img = models.ImageField(upload_to='blog/',blank=True, null=True)
    keyword = models.JSONField()

class Description(models.Model):
    img = models.ImageField(upload_to='blog/description/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    body = RichTextField()


class degree_desc(models.Model):
    seo = models.OneToOneField(SEO, on_delete=models.CASCADE)
    degree = models.ForeignKey(Degree , on_delete=models.CASCADE)
    description = models.OneToOneField(Description, on_delete=models.CASCADE)


class subject_desc(models.Model):
    seo = models.OneToOneField(SEO, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject , on_delete=models.CASCADE)
    description = models.OneToOneField(Description, on_delete=models.CASCADE)


class spiecification_desc(models.Model):
    seo = models.OneToOneField(SEO, on_delete=models.CASCADE)
    spiecification = models.ForeignKey(Spiecification , on_delete=models.CASCADE)
    description = models.OneToOneField(Description, on_delete=models.CASCADE)


class service_desc(models.Model):
    seo = models.OneToOneField(SEO, on_delete=models.CASCADE)
    service = models.ForeignKey(Service , on_delete=models.CASCADE)
    description = models.OneToOneField(Description, on_delete=models.CASCADE)


class project_desc(models.Model):
    seo = models.OneToOneField(SEO, on_delete=models.CASCADE)
    project = models.ForeignKey(Project , on_delete=models.CASCADE)
    description = models.OneToOneField(Description, on_delete=models.CASCADE)


class task_project_desc(models.Model):
    seo = models.OneToOneField(SEO, on_delete=models.CASCADE)
    task_project = models.ForeignKey(TaskProject , on_delete=models.CASCADE)
    description = models.OneToOneField(Description, on_delete=models.CASCADE)



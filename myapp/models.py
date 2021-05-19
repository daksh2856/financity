from django.db import models

# Create your models here.

class contactus(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()
    subject=models.CharField(max_length=50)
    message=models.TextField()

class user(models.Model):
    fname=models.CharField(max_length=25)
    lname=models.CharField(max_length=25)
    phone=models.CharField(max_length=10)
    dob = models.DateField(null=True)
    email=models.EmailField()
    gender = models.CharField(max_length = 1,choices = [('M', 'Male'), ('F','Female'), ('O','Other')],null=True)
    password=models.CharField(max_length=24)
    address = models.TextField(blank=True)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)

class blog(models.Model):
    subject=models.CharField(max_length=125)
    image=models.ImageField()
    description=models.TextField()
    published_date = models.DateField()
    user_id = models.ForeignKey(user, on_delete = models.CASCADE)
  

class comment(models.Model):
    message=models.CharField(max_length=350)
    user_id = models.ForeignKey(user, on_delete = models.CASCADE)
    blog_id = models.ForeignKey(blog, on_delete = models.CASCADE)

class review(models.Model):
    subject=models.CharField(max_length=125)
    message=models.CharField(max_length=350)
    user_id = models.ForeignKey(user, on_delete = models.CASCADE)

class budget(models.Model):
    year=models.DateField()
    title=models.CharField(max_length=125)
    link=models.URLField()


class annualreports(models.Model):
    year=models.DateField()
    title=models.CharField(max_length=125)
    link=models.URLField()
    published=models.DateField()

class services(models.Model):
    title=models.CharField(max_length=125)
    link=models.URLField()


class dataandstatistics(models.Model):
    categories=models.CharField(max_length=125)
    subject=models.CharField(max_length=125)
    link=models.URLField()

class actandrules(models.Model):
    name=models.CharField(max_length=125)
    act=models.CharField(max_length=125)
    rules=models.CharField(max_length=125)
    link=models.URLField()

class guidelines(models.Model):
    title=models.CharField(max_length=125)
    published=models.CharField(max_length=125)
    link=models.URLField()





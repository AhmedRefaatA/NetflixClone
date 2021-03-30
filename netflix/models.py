from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=233)
    

    def __str__(self):
        return str(self.name)

class Producer(models.Model):
    name = models.CharField(max_length=233)
    

    def __str__(self):
        return str(self.name)

class Country(models.Model):
    name = models.CharField(max_length=233)

    def __str__(self):
        return self.name

class Classification(models.Model):
    name = models.CharField(max_length=233)

    def __str__(self):
        return self.name


class Rate(models.Model):
    rate = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return str(self.rate)


class Movie(models.Model):
    title = models.CharField(max_length=255)
    story = models.TextField()
    duration = models.IntegerField(null=True ,blank=True)
    publish_year = models.DateField(null=True ,blank=True)
    poster = models.ImageField(upload_to="movies/posters", null=True, blank=True)
    video = models.FileField(upload_to='movies/video', null=True, blank=True)
    categories = models.ManyToManyField(Category)
    country = models.ForeignKey(Country,null=True, on_delete=models.SET_NULL)
    rate = models.OneToOneField(Rate, null=True, on_delete=models.SET_NULL)
    classification = models.ForeignKey(Classification,null=True, on_delete=models.SET_NULL)
    producer = models.ManyToManyField(Producer)
    def __str__(self):
        return str(self.title)


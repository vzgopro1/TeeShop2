from django.db import models

SEASON_CHOICES = (
    ('summer', 'Summer'),
    ('winter', 'Winter'),
    ('spring', 'Spring'),
    ('autumn', 'Autumn')
)


class User(models.Model):
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=50)
    status = models.BooleanField()
    username = models.CharField(max_length=35)
    password = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='UsersAvatars/')
    creationDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

class Store(models.Model):
    title = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    emile = models.EmailField()
    flat = models.CharField(max_length=12)
    street = models.CharField(max_length=25)
    city = models.CharField(max_length=25)

    def __str__(self):
        return self.title

class ProductCategory(models.Model):
    title = models.CharField(max_length=25)

    def __str__(self):
        return self.title

class Rating(models.Model):
    opinions = models.TextField()
    valuation = models.IntegerField()

    def __str__(self):
        return self.opinions

class Post(models.Model):
    title = models.CharField(max_length=50)
    descriptions = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.IntegerField()
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE)
    likes = models.IntegerField()
    # language
    creationDate = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='Posts/')

    def __str__(self):
        return str(self.id)

class Product(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    region = models.CharField(max_length=35)
    HarvestSeason = models.CharField(max_length=25, choices=SEASON_CHOICES)
    ProductYear = models.DateTimeField(auto_now=True)


class Trade(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    #store=models.ForeignKey('Store',on_delete=models.CASCADE)
    productioncountry = models.TextField()
    price = models.IntegerField()
    weight = models.IntegerField()
    term = models.DateTimeField()
    delivery = models.TextField()
    deliverycost = models.IntegerField()
    class Meta:
        verbose_name_plural = 'Trade'
    def __str__(self):
        return self.product
class Package(models.Model):
    image = models.ImageField()
    weight = models.IntegerField()
    volume = models.IntegerField()
    class Meta:
        verbose_name_plural ='Package'
    def __str__(self):
        return self.image
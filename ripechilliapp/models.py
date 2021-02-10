from django.db import models

# Create your models here.
class IndexImg(models.Model):
    heading = models.CharField(max_length=100)
    tagline = models.CharField(max_length=200)

    def __str__ (self):
        return self.heading


TYPECARD = [
    ('web', 'WEB'),
    ('logo', 'LOGO'),
]

class KindOfCards(models.Model):
    types = models.CharField(choices=TYPECARD, max_length=70)
    logo_icon = models.CharField(max_length=100)
    card_title = models.CharField(max_length=100)

    def __str__(self):
        return self.card_title

TYPEFAQS = [
    ('web', 'WEB'),
    ('logo', 'LOGO'),
]
class Faqs(models.Model):
    faq_types = models.CharField(choices=TYPEFAQS, max_length=100)
    faq_title = models.CharField(max_length=500)
    faq_ans = models.CharField(max_length=5000)

    def __str__(self):
        return self.faq_title

class AboutRipe(models.Model):
    brief = models.TextField()

class GetStarted(models.Model):
    card_title = models.CharField(max_length=100)
    card_tagline = models.CharField(max_length=200)
    card_desc = models.TextField()
    card_btn = models.CharField(max_length=100)
    title_color = models.CharField(max_length=100)
    btn_color = models.CharField(max_length=100)
    logo = models.CharField(max_length=50)
    link = models.CharField(max_length=100)
    def __str__(self):
        return self.card_title    


TYPEPLANS = [
    ('web', 'WEB'),
    ('logo', 'LOGO'),
]
class Plans(models.Model):
    types = models.CharField(choices=TYPEPLANS, max_length=100)
    plan_title = models.CharField(max_length=100)
    plan_price = models.CharField(max_length=100)
    plan_tagline = models.CharField(max_length=100)

    def __str__(self):
        self.plan_title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name

class keywords(models.Model):
    terms = models.TextField()

class WhyRipeChilli(models.Model):
    logo = models.CharField(max_length=70)
    Title = models.CharField(max_length=70)
    Desc = models.TextField()

    def __str__(self):
        return self.Title

class WebSamples(models.Model):
    link = models.CharField(max_length=200)
    image = models.ImageField()
    title = models.CharField(max_length=100)
    alt = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    
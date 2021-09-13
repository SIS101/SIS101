from django.db import models

class AdminSetting(models.Model):
    auto_application_fee_invoicing=models.BooleanField(default=True)
    auto_tution_fee_invoicing=models.BooleanField(default=True)

class WebsiteSetting(models.Model):
    #site info
    full_name=models.CharField(max_length=50, default="KAFUE INSTITUTE OF HEALTH SCIENCES AND RESEARCH")
    short_name=models.CharField(max_length=10, default="KIHSR")
    email=models.EmailField(default="info@kihsr.ac.zm")
    contact_number_1=models.CharField(max_length=20, default="+260")
    contact_number_2=models.CharField(max_length=20, blank=True)
    moto=models.CharField(max_length=100, default="Creating Tomorrow's Health Workers")
    description=models.CharField(max_length=200, blank=True)

    #site images
    favicon=models.ImageField(upload_to="website", default="defaults/favicon.ico")
    logo=models.ImageField(upload_to="website", default="defaults/logo.png")
    first_slide_image=models.ImageField(upload_to="website/slide", default="defaults/slide1.jpg")
    second_slide_image=models.ImageField(upload_to="website/slide", default="defaults/slide2.jpg")
    prgrammes_image=models.ImageField(upload_to="programmes", default="defaults/programmes.png")
    short_courses_image=models.ImageField(upload_to="short_courses", default="defaults/short-courses.png")
    library_image=models.ImageField(upload_to="library", default="defaults/books.png")
    background_image=models.ImageField(upload_to="website/background", default="defaults/nurses.jpg")

    #social links
    facebook_link=models.URLField(default="https://www.facebook.com/kafueihser/")

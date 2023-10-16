from django.db import models

def upload_to(instance,filename):
    return 'triocodex/{filename}'.format(filename=filename)
# Create your models here.
class Content(models.Model):


    logo = models.ImageField(upload_to=upload_to)

    # Hero Section
    heroTitle = models.CharField(max_length=10000,default="heroTitle")
    heroSubTitle = models.CharField(max_length=10000,default="heroSubTitle")
    heroButtonText = models.CharField(max_length=10000,default="heroButtonText")
    heroButtonLink = models.CharField(max_length=10000,default="heroButtonLink")
    heroImage = models.ImageField(upload_to=upload_to)

    # About Section
    aboutHeader = models.CharField(max_length=10000,default="aboutHeader")
    aboutTitle = models.CharField(max_length=10000,default="aboutTitle")
    aboutSubTitle = models.CharField(max_length=10000,default="aboutSubTitle")
    aboutButtonText = models.CharField(max_length=10000,default="aboutButtonText")
    aboutButtonLink = models.CharField(max_length=10000,default="aboutButtonLink")
    aboutImage = models.ImageField(upload_to=upload_to)

    # About Value
    valueHeader = models.CharField(max_length=10000,default="valueHeader")
    valueTitle = models.CharField(max_length=10000,default="valueTitle")
    # 1
    value1Title = models.CharField(max_length=10000,default="value1Title")
    value1Description = models.TextField(default="Value1Description")
    value1Image = models.ImageField(upload_to=upload_to)
    # 2
    value2Title = models.CharField(max_length=10000,default="value2Title")
    value2Description = models.TextField(default="Value2Description")
    value2Image = models.ImageField(upload_to=upload_to)
    # 3
    value3Title = models.CharField(max_length=10000,default="value2Title")
    value3Description = models.TextField(default="Value3Description")
    value3Image = models.ImageField(upload_to=upload_to)

    # Counter
    clientCounter = models.IntegerField(default=1)
    projectCounter = models.IntegerField(default=1)
    hourCounter = models.IntegerField(default=1)
    hardWorkerCounter = models.IntegerField(default=1)

    # Services
    serviceHeader = models.CharField(max_length=500,default="ServiceHeader")
    serviceTItle = models.CharField(max_length=1000,default="ServiceTitle")


    # Footer 
    footerLogo = models.ImageField(upload_to=upload_to)
    footerTitle = models.CharField(max_length=10000,default="Footer Details")


   # Company Social Media 
    facebook =  models.CharField(max_length=2000,default="https://facebook.com/iamsheikhtabarak")
    instagram =  models.CharField(max_length=2000,default="https://instagram.com/sheikh_tabarak")
    linkedin =  models.CharField(max_length=2000,default="https://linkedin.com/in/sheikhtabarak")
    fiverr =  models.CharField(max_length=2000,default="https://fiverr.com/sheikhtabarak")
    upwork =  models.CharField(max_length=2000,default="https://upwork.com/user/sheikhtabarak")

    #copyrightContent
    copyright =  models.CharField(max_length=5000,default="Copyrights 2023 TrioCodex")


    #contact
    address= models.CharField(max_length=5000,default="GUjranwala")
    emails= models.CharField(max_length=2000,default="tricodex@gmail.com")
    phone= models.CharField(max_length=2000,default="xxxx-xxxxxxx")
    openHours= models.CharField(max_length=5000,default="Monday - Friday<br>9:00AM - 5:00PM")

class Service(models.Model):
    icon =  models.CharField(max_length=500,default="ri-discuss-line icon")
    title =  models.CharField(max_length=1000,default="title")
    description =  models.TextField(default="Description")
    bicon =  models.CharField(max_length=500,default="ri-discuss-line icon")
    buttonText = models.CharField(max_length=10000,default="")
    color = models.CharField(max_length=100,default="blue")

    def __str__(self):
        return self.title

    

class Faqs(models.Model):
    question =  models.CharField(max_length=2000,default="FAQs Questions")
    answer =  models.CharField(max_length=10000,default="FAQs Answer")


    
class Testimonial(models.Model):
    testimonialImage = models.ImageField(upload_to=upload_to)


       
class Team(models.Model):
    profileImage = models.ImageField(upload_to=upload_to)
    name =  models.CharField(max_length=2000,default="Name Team")
    designation =  models.CharField(max_length=2000,default=" Description Name")
    description =  models.CharField(max_length=10000,default="Description Team")
    facebook =  models.CharField(max_length=2000,default="https://facebook.com/iamsheikhtabarak")
    instagram =  models.CharField(max_length=2000,default="https://instagram.com/sheikh_tabarak")
    linkedin =  models.CharField(max_length=2000,default="https://linkedin.com/in/sheikhtabarak")
    fiverr =  models.CharField(max_length=2000,default="https://fiverr.com/sheikhtabarak")
    upwork =  models.CharField(max_length=2000,default="https://upwork.com/user/sheikhtabarak")





       
class Project(models.Model):
    project = models.ImageField(upload_to=upload_to)
    name =  models.CharField(max_length=10000,default="Project Team")
    description =  models.CharField(max_length=10000,default="Project Description")
    category = models.ForeignKey(Service,on_delete=models.CASCADE)
    projectLink = models.CharField(max_length=10000,default="Project Link")
    projectGithub = models.CharField(max_length=10000,default="Project Guthub")




class ClientLogos(models.Model):
    clientsLogos = models.ImageField(upload_to=upload_to)



class ContactForm(models.Model):
    name= models.CharField(max_length=2000,default="Name")
    emails= models.CharField(max_length=2000,default="Emails")
    subject= models.CharField(max_length=2000,default="Subject")
    message= models.CharField(max_length=10000,default="message")


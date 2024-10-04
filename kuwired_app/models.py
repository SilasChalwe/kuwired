from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#Hero Section Standalone
#cta -->call to actions 
class HeroSection(models.Model):
    headline = models.CharField(max_length=255)
    subheadline = models.TextField() 
    motion = models.TextField() 
    cta_button_text = models.CharField(max_length=50)
    cta_button_url = models.URLField()
    class  Meta:
        db_table = 'HeroSection' 
    def __str__(self):
        return self.headline
    
#Icon Box  for (Services OverView) Standalone
class IconBox(models.Model):
    title = models.CharField(max_length=255)
    subheadline = models.TextField()  
    class  Meta:
        db_table = 'IconBox' 
    def __str__(self):
        return self.title
    
class testimonial(models.Model):
    client_name = models.CharField( max_length=50)
    client_company = models.CharField( max_length=100,blank=True,null=True) 
    client_feedback = models.TextField()
    image = models.ImageField(upload_to="images/testimonials/")
    role = models.CharField( max_length=50)
    class  Meta:
        db_table = 'testimonial'
        
    def __str__(self):
        return f"{self.client_name}- {self.client_company}" 
        
#Call To Action
class CallToAction(models.Model):
    headline = models.CharField(max_length=255)
    subheadline = models.TextField() 
    cta_button_text = models.CharField(max_length=50)
    cta_button_url = models.URLField()
    class  Meta:
        db_table = 'CallToAction' 
    def __str__(self):
        return self.headline
       
#Category for Products in Porfolio
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name  
             
# Portfolio Model                            
class ProductItem(models.Model):
    project_name = models.CharField(max_length=50)
    project_description = models.TextField()
    project_image = models.ImageField(upload_to='images/')
    project_filter_branding = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    project_url = models.URLField(blank=True,null=True)       
    class  Meta:
        db_table = 'Product'
    
    def __str__(self):
        return self.project_name 
    
# FAQ   
class FAQ(models.Model):
    question= models.CharField(max_length=255)
    answer = models.CharField(max_length=225)
    
    class Meta:
        db_table = 'FAQ'
        
    def __str__(self):
        return self.question   
 
#Privacy Policy
class PrivacyPolicy(models.Model):
    content = models.TextField()

    class Meta:
        db_table = 'PrivacyPolicy'
       
    def __str__(self):
        return "Privacy Policy"

#Terms of Service
class TermsOfService(models.Model):
    content = models.TextField()
    
    class Meta:
        db_table = 'TermsOfService'
        
    def __str__(self):
        return "Terms of Service"
 
 
# Service
class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=100, blank=True)  # Optional icon class for bootstrap icons
    detail = models.TextField(blank=True)  # Optional additional detail
    video_url = models.URLField(blank=True, null=True)  # For video streaming about the service

    def __str__(self):
        return self.title  
    

# 2. Video(for service video section)
class ServiceVideo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    video_url = models.URLField()  # Video URL (could be YouTube, Vimeo, or an embedded file)
    thumbnail = models.ImageField(upload_to='videos/thumbnails/', blank=True, null=True)  # Optional thumbnail

    def __str__(self):
        return self.title   
    
# About Us
class AboutUs(models.Model):
    content = models.TextField()
    
    class Meta:
        db_table = 'AboutUs'
        
    def __str__(self):
        return "About Us"  
    
class TeamMember(models.Model):
    team_name = models.CharField( max_length=50)
    team_image = models.ImageField(upload_to="images/teams/")
    team_role = models.CharField( max_length=50)
    project_url = models.URLField(blank=True,null=True)       

    class  Meta:
        db_table = 'TeamMember'
        
    def __str__(self):
        return self.team_name   

 

 
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.email}"
    
        
class Client_Item(models.Model):
        name = models.CharField( max_length=50)
        image = models.ImageField( upload_to='clients/')    
        class Meta:
            db_table = 'Client_Item'
                
        def __str__(self):
            return self.name          

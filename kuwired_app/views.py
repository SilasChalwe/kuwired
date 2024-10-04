from .forms import ContactForm
from .models import FAQ, CallToAction, ProductItem, TeamMember, testimonial
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Client_Item,HeroSection,Service,AboutUs




def home_view(request): 
    portfolio_items = ProductItem.objects.select_related('project_filter_branding').all()
    testimonials = testimonial.objects.all().order_by('client_name')
    client = Client_Item.objects.all().order_by('name')
    faq = FAQ.objects.all()
    cta= CallToAction.objects.first()
    hero = HeroSection.objects.first()
    services = Service.objects.all() 
    about_us = AboutUs.objects.first()
    context = {'products_items':portfolio_items,
               'testimonials':testimonials,
               'faqs':faq,
                'clients':client,
                'cta':cta,
                'hero':hero,
                'services':services,'about_us':about_us,
               }
   
    return render(request, 'home/index.html', context)

'''
#contact us view
def contact_view(request):
    form = ContactForm()
    if request.method =="POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            #send mail here and save the contact
            form.save()
            return redirect('kuwired-contact-success')
        else:
            error_message =  messages.error('form has invalid details')
            return render(request,'contacts/contact.html',{'error-message':error_message})
    return render(request,'contacts/contact.html',{'form':form})
'''

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message sent! We will get back to you soon.")
            return redirect('contact_us')
    else:
        form = ContactForm()

    return render(request, 'contacts/contact_us.html', {'form': form})



def contact_sent_view(request):
    return render(request,'contacts/contact_success.html')

def Product_view(request):
    portfolios = ProductItem.objects.select_related('project_filter_branding').all()
    testimonials = testimonial.objects.all().order_by('name')
    teams = TeamMember.objects.all().order_by('team_name')
    context = {'portfolios':portfolios,'testimonials':testimonials,'teams':teams}
   
    return render(request,'products/product-details.html',context)

def products_list_view(request):
    portfolios = ProductItem.objects.select_related('project_filter_branding').all().order_by('project_name')
    context = {'portfolios':portfolios}
    return render(request,'products/products_list.html',context)




def about_view(request):
    return render(request,'contacts/about_us.html')

def team_view(request):
    teams = TeamMember.objects.all().order_by('team_name')
    print(teams)
    context = {'teams':teams}
    return render(request,'team/team.html',context)

#services view
def services_view(request):
    return render(request,'services/services.html')
from django.shortcuts import render
from .models import Content,Faqs,Testimonial,ContactForm ,Service,Project,Testimonial,ClientLogos,Team
# Create your views here.
def index(request):
    content = Content.objects.all().first()
    faqs = Faqs.objects.all()
    content = Testimonial.objects.all()
    services = Service.objects.all()
    project = Project.objects.all()
    testimonial = Testimonial.objects.all()
    clientlogo = ClientLogos.objects.all()
    teams = Team.objects.all()
    clientlogo = ClientLogos.objects.all()
    clientlogo = ClientLogos.objects.all()
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]
        contct = ContactForm(name=name,emails=email,subject=subject,message=message)
        contct.save()

    context = {
        "content": content,
        "faq": faqs,
        "services": services,
        "project": project,
        "testimonial": testimonial,
        "clientlogo": clientlogo,
        "teams": teams,
    }
    
    return render(request,'index.html',context)
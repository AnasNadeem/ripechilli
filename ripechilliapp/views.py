from django.shortcuts import render
from .models import IndexImg, KindOfCards, Faqs, AboutRipe ,GetStarted, Plans, Contact,keywords, WhyRipeChilli, WebSamples, Internship
from django.views.generic import TemplateView 
from django.views.generic.edit import FormView
from .forms import ContactForm, internForm
from django.core.mail import send_mail
from django.contrib import messages
from django.template.loader import render_to_string
# Create your views here 

class SampleView(TemplateView):
    template_name = 'ripechilli/webSamples.html'
    context_object_name = 'context'

    def get_context_data(self, **kwargs):
        context = super(SampleView, self).get_context_data(**kwargs)
        context['keyword'] = keywords.objects.all()
        context['about'] = AboutRipe.objects.all()
        context['websample'] = WebSamples.objects.all()

        return context

class WebView(TemplateView):
    template_name = 'ripechilli/webplans.html'
    context_object_name = 'context'

    def get_context_data(self, **kwargs):
        context = super(WebView, self).get_context_data(**kwargs)
        context['faq'] = Faqs.objects.filter(faq_types="web")
        context['kindofcard'] = KindOfCards.objects.filter(types="web")
        context['about'] = AboutRipe.objects.all()
        context['plan'] = Plans.objects.all()
        context['keyword'] = keywords.objects.all()

        return context

class LogoView(TemplateView):
    template_name = 'ripechilli/logoplans.html'
    context_object_name = 'context'

    def get_context_data(self, **kwargs):
        context = super(LogoView, self).get_context_data(**kwargs)
        context['faq'] = Faqs.objects.filter(faq_types="logo")
        context['kindofcard'] = KindOfCards.objects.filter(types="logo")
        context['about'] = AboutRipe.objects.all()
        context['plan'] = Plans.objects.all()
        context['keyword'] = keywords.objects.all()

        return context

class AboutView(TemplateView):
    template_name = 'ripechilli/about.html'
    context_object_name = 'context'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['about'] = AboutRipe.objects.all()
        context['keyword'] = keywords.objects.all()

        return context

class IndexView(TemplateView):
    template_name = 'ripechilli/index.html'
    context_object_name = 'context'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['card'] = GetStarted.objects.all()
        context['keyword'] = keywords.objects.all()
        context['whyRC'] = WhyRipeChilli.objects.all()
        context['about'] = AboutRipe.objects.all()
        context['keyword'] = keywords.objects.all()

        return context


class ContactView(FormView):
    model = Contact
    template_name = 'ripechilli/contactus.html'
    form_class = ContactForm
    success_url = '/'
    context_object_name = 'context'
    
    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['keyword'] = keywords.objects.all()
        context['about'] = AboutRipe.objects.all()

        return context
        
    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        phone = form.cleaned_data['phone']
        message = form.cleaned_data['message']

        contact = Contact.objects.create(name=name, email=email, phone=phone, message=message)
        # send an email
        send_mail(
            'Message from'+ name,#subject
            message + phone,#message
            email,#from mail
            ['ripechilli@gmail.com'],#to mail
        )
        return super(ContactView, self).form_valid(form)

def intern(request):
    if request.method=="POST":
        intern_name = request.POST.get('name')
        intern_email = request.POST.get('email')
        intern_phone = request.POST.get('phone')
        intern_profession = request.POST.get('profession')
        intern_pin_code = request.POST.get('pin_code')
        intern_city = request.POST.get('city')
        intern_state = request.POST.get('state')
        intern_question1 = request.POST.get('question1')
        intern_question2 = request.POST.get('question2')
        form = Internship(name=intern_name,email=intern_email,phone=intern_phone,
                pin_code=intern_pin_code,city=intern_city,state=intern_state,
                proffesion=intern_profession,question1=intern_question1,question2=intern_question2)
        form.save()
        messages.info(request, f"Successfully registered for {intern_name}.We will be in touch very soon.")
    context = {
        'form':internForm,
    }
    return render(request, 'ripechilli/hiring.html', context)

def mailSendCom(request):
    content = render_to_string('ripechilli/mailbody.txt')
    if request.method=="POST":
        email_one = request.POST.get('mail_one')
        email_two = request.POST.get('mail_two')
        email_three = request.POST.get('mail_three')
        email_four = request.POST.get('mail_four')
        email_five = request.POST.get('mail_five')

    # send an email
        send_mail(
            'Ripe Chilli',#subject
            content,#message
            'ripechilli@gmail.com',#from mail
            [email_one, email_two, email_three, email_four, email_five],#to mail
        )
    return render(request, 'ripechilli/sent_mail.html')
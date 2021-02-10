from django.shortcuts import render
from .models import IndexImg, KindOfCards, Faqs, AboutRipe ,GetStarted, Plans, Contact,keywords, WhyRipeChilli, WebSamples
from django.views.generic import TemplateView 
from django.views.generic.edit import FormView
from .forms import ContactForm
from django.core.mail import send_mail
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
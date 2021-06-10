from django.urls import path
from .views import SampleView, WebView, LogoView, AboutView, IndexView, ContactView, intern, mailSendCom
urlpatterns = [
    path('', IndexView.as_view(), name='Index'),
    path('webSample/', SampleView.as_view(), name='WebSamples'),
    path('logo/', LogoView.as_view(), name='Logo'),
    path('website/', WebView.as_view(), name='Website'),
    path('about/', AboutView.as_view(), name='About'),
    path('contact/', ContactView.as_view(), name='Contact'),
    path('internship/', intern, name='intern'),
    path('sentmail/', mailSendCom, name='mail'),
]

from django.urls import path, include
from ..views import main

urlpatterns = [
    path('', include([
        path('', main.homepage, name='homepage'),
        path('privacy-policy/', main.privacy_policy, name='privacy_policy'),
        path('terms-of-use/', main.terms_of_use, name='terms_of_use')
    ])),
]

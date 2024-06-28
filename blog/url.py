from django.urls import path
from .views import *
urlpatterns = [
    path('about/', about, name='about'),
    path('glasses/', glasses, name='glasses'),
    path('contact/', contact, name='contact'),
    path('', index, name='index'),
    path('product/', product, name='product'),
    path('shop/', shop, name='shop'),
    path('remot/', remot, name='remot'),
    path('video/', video, name='video'),
    path('sunDetail/<slug:sun>/', sunDetailView, name='sunDetailView'),
    path('aboutDetail/<int:id>/', aboutVVV, name='aboutDetailView'),
    path('haqidaDetail/<slug:haqida>/', haqidaDetailView, name='haqidaDetailView'),
    path('carusDetail/<slug:carus>/', caruselDetailView, name='caruselDetailView'),
    path('suns/update/<slug>/', SunglaUpdateView.as_view(), name='suns_update'),
    path('suns/delete/<slug>/', SunglaDeleteView.as_view(), name='suns_delete'),
    path('suns_create/',SunlaCreateView.as_view(), name='suns_create'),
    path('search/', SearchResultslist.as_view(), name="search_results"),
]

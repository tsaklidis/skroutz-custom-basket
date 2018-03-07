from django.conf.urls import url
from skroutzbasket.public import views

urlpatterns = [
    # Home page
    url('^$', views.home, name='home'),
    url('^item/add/', views.item_add, name='item_add'),

]
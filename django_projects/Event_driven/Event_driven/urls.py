"""Event_driven URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from EventDriven import views
from django.urls import path, include
urlpatterns = [
    path('events', views.index, name='event-index'),
    path('events/<int:id>', views.get_event_by_id, name='event-detail'),
    path('create_event', views.create_event, name='create_event'),
    path('delete_event/<int:id>', views.delete_event, name='delete_event'),
    path('user/', include('user.urls')),
    path('booking', views.boooking, name='booking'),
    path('checkout', views.checkout, name='checkout')
    #path('book-tickets/<int:id>', views.book_event, name='book-event'),
    #path('events/search_event', views.index, name='search_event')
    #path("/book-tickets",)
]
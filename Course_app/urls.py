from django.urls import path
from . import views

urlpatterns = [
    path('', views.card_list_view, name='card_list'),  # URL for card list
    path('card/<int:card_id>/', views.topic_detail_view, name='topic_list'),  # URL for topics of a card
    path('card/<int:card_id>/topic/<int:topic_id>/', views.topic_detail_view, name='topic_detail'),  # URL for topic details
]

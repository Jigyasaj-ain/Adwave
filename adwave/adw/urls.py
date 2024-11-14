from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),  
    path('about/', views.about, name='about'),  # About Us page
    path('display/', views.display, name='display'),  # Display page
    path('features/', views.features, name='features'),  # Features page
    # path('login/', views.login, name='login'),  # Login page
    path('submitads/', views.submitads, name='submitads'),  # Submit Ads page
    path('feedback/', views.feedback, name='feedback'), #feedback page
    path('submit_ad/', views.submit_ad, name='submit_ad'),
    path('signuplogin/', views.signuplogin, name='signuplogin'), 
    path('login/', views.login_view, name='login'),
  
    # Add other URLs for home, logout, etc.

    # path('', views.all_user),
    # path('submit-ad/', views.submit_ad, name='submit_ad'),
    # path('success/', views.success_page, name='success_page'),  # Page after successful submission
]

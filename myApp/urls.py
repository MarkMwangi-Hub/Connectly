from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from myApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login, name='login'),
    path('create/', views.create, name='create'),
    path('', views.index, name='index'),

    path('FAQS/', views.faq, name='faq'),

    path('About/', views.about, name='about'),

    path('Explore/', views.explore, name='explore'),

    path('Forums/', views.forums, name='forums'),

    path('settings/', views.settings, name='edit_profile'),

    path('details/', views.exploredetails, name='details'),

    path('upload/', views.upload_image, name='upload_image'),

    path('edit_image/<int:image_id>/',views.edit_image, name='edit_image'),

    path('delete_image/<int:image_id>/',views.delete_image, name='delete_image'),

    path('logout/', views.logout, name='logout'),

    path('profile/', views.view_profile, name='view_profile'),

    path('profile/edit/', views.edit_profile, name='edit_profile'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
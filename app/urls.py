from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('', views.index, name='index'),
    path('sec', views.second, name='second'),
    path('pass_data', views.pass_data, name='pass_data'),
    path('student', views.student, name='student'),
    path('student_list', views.student_list, name='student_list'),
    path('form', views.form, name='form'),
    path('about', views.about, name='about'),
    path('404', views.custom_404_view, name='custom_404'),
]
# ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
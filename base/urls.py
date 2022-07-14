from django.urls import path , include
from .views import BlogList, BlogDetail
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', BlogList.as_view(),name='blogs'),
    path('blog/<int:pk>', BlogDetail.as_view(), name='blog'),
    path('tinymce/', include('tinymce.urls')),

]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
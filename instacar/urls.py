from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from authentication.views import signup_view, logout_view, login_view
from insta_user.views import index

urlpatterns = [
    path('', index, name='homepage'),
    path('login/', login_view),
    path('logout/', logout_view),
    path('signup/', signup_view),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


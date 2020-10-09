from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from authentication.views import signup_view, logout_view, login_view
from insta_user.views import index, profile_view
from insta_post.views import index, post_form_view, comment_form_view, photo_detail, up_vote, down_vote


urlpatterns = [
    path('', index, name='homepage'),
    path('login/', login_view),
    path('logout/', logout_view),
    path('signup/', signup_view),
    path('newpost/', post_form_view),
    path('upvote/<int:post_id>/', up_vote),
    path('downvote/<int:post_id>/', down_vote),
    path('post/<int:post_id>/', photo_detail, name="post"),
    path('post/<int:post_id>/newcomment/', comment_form_view),
    path('admin/', admin.site.urls),
    path('<str:username>/', profile_view, name='profile'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


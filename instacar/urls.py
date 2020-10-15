from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from authentication.views import signup_view, logout_view, LoginView
from insta_user.views import index, profile_view, profile_edit_view, del_user
from insta_post.views import IndexView, post_form_view, comment_form_view, photo_detail, up_vote, down_vote, del_post, post_edit_view, del_comment, edit_comment, FollowView, UnfollowView


urlpatterns = [
    path('', IndexView.as_view(), name='homepage'),
    path('login/', LoginView.as_view()),
    path('logout/', logout_view),
    path('signup/', signup_view),
    path('newpost/', post_form_view),
    path('upvote/<int:post_id>/', up_vote),
    path('downvote/<int:post_id>/', down_vote),
    path('post/<int:post_id>/', photo_detail, name="post"),
    path('post/<int:post_id>/newcomment/', comment_form_view),
    path('post/<int:post_id>/edit/', post_edit_view, name='post_edit'),
    path('post/<int:post_id>/delete/', del_post, name='del_post'),
    path('comment/<int:pk>/delete/', del_comment, name='del_comment'),
    path('comment/<int:pk>/edit/', edit_comment, name='del_comment'),
    path('following/<int:follow_id>/', FollowView.as_view()),
    path('unfollowing/<int:unfollow_id>/', UnfollowView.as_view()),
    path('admin/', admin.site.urls),
    path('<str:username>/edit/', profile_edit_view, name='profile_edit'),
    path('<str:username>/delete/', del_user, name='delete'),
    path('<str:username>/', profile_view, name='profile'),

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


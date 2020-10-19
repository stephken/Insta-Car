from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from authentication.views import signup_view, logout_view, LoginView
from insta_user.views import profile_edit_view, del_user, profile_view, FollowView, UnfollowView
from insta_post import views
from insta_search.views import SearchResultsView
from insta_comment.views import comment_form_view, del_comment, edit_comment, comment_likes
from django.views.generic import TemplateView
from django.views.defaults import page_not_found, server_error


urlpatterns = [
    path('', views.IndexView.as_view(), name='homepage'),
    path('login/', LoginView.as_view()),
    path('logout/', logout_view),
    path('signup/', signup_view),
    path('newpost/', views.post_form_view),
    path('upvote/<int:post_id>/', views.up_vote),
    path('post/<int:post_id>/', views.photo_detail, name="post"),
    path('post/<int:post_id>/newcomment/', comment_form_view),
    path('post/<int:post_id>/edit/', views.post_edit_view, name='post_edit'),
    path('post/<int:post_id>/delete/', views.del_post, name='del_post'),
    path('comment/<int:pk>/delete/', del_comment, name='del_comment'),
    path('comment/<int:pk>/edit/', edit_comment, name='del_comment'),
    path('comment/<int:pk>/like/', comment_likes, name='like'),
    path('following/<int:follow_id>/', FollowView.as_view()),
    path('unfollowing/<int:unfollow_id>/', UnfollowView.as_view()),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('500/', TemplateView.as_view(template_name="500.html")),
    path('404/', TemplateView.as_view(template_name="404.html")),
    path('admin/', admin.site.urls),
    path('<str:username>/edit/', profile_edit_view, name='profile_edit'),
    path('<str:username>/delete/', del_user, name='delete'),
    path('<str:username>/', profile_view, name='profile'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
handler404 = 'insta_post.views.handler404'

handler500 = 'insta_post.views.handler500'

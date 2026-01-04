from django.urls import path, include, re_path
from . import views as music_nation_views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'music_nation'
urlpatterns = [
    path('', music_nation_views.home, name='home'),
    path('@<str:username>/', music_nation_views.profile_detail, name='profile_detail'),
    path('@<str:username>/add/', music_nation_views.add_album, name='add_album'),
    path('@<str:username>/album/<str:album>/', music_nation_views.album_detail, name='album_detail'),
    path('login/', LoginView.as_view(template_name='music_nation/user_login.html'), name="login"),
    path('signup/', music_nation_views.signup, name='signup'),
    path('@<str:username>/album/<str:album>/delete/', music_nation_views.delete_album, name='delete_album'),
    path('@<str:username>/album/<str:album>/add/', music_nation_views.add_song, name='add_song'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

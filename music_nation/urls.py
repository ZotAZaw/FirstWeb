from django.urls import path, include, re_path
from . import views as v1
from django.contrib.auth import views as v2

app_name = 'music_nation'
urlpatterns = [
    path('', v1.home, name='home'),
    path('@<str:username>/', v1.profile_detail, name='profile_detail'),
    path('@<str:username>/add/', v1.add_album, name='add_album'),
    path('@<str:username>/album/<str:album>/', v1.album_detail, name='album_detail'),
    path('login/', v2.LoginView.as_view(template_name='music_nation/user_login.html'), name="login"),
    path('signup/', v1.signup, name='signup'),
    path('@<str:username>/album/<str:album>/delete/', v1.delete_album, name='delete_album'),
    path('@<str:username>/album/<str:album>/add/', v1.add_song, name='add_song'),
    path('logout/', v2.LogoutView.as_view(), name='logout'),
    path("search/", v1.search_songs, name="search_songs"),
    # forgot password
    path(
        "password-reset/",
        v2.PasswordResetView.as_view(
            template_name="registration/password_reset_form.html"
        ),
        name="password_reset",
    ),
    path(
        "password-reset/done/",
        v2.PasswordResetDoneView.as_view(
            template_name="registration/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        v2.PasswordResetConfirmView.as_view(
            template_name="registration/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        v2.PasswordResetCompleteView.as_view(
            template_name="registration/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
]

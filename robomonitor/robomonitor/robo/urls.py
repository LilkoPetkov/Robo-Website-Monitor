from django.urls import path
from .views import IndexView, UserCreateView, UserLogoutView, ProfileUpdateView, WebsiteCreateView, \
    WebsitesView, dns_check_page, UserLoginView, WebsiteDeleteView, WebsiteUpdateView, logs_page, error_404_view, \
    four_o_four

urlpatterns = [

    # Index
    path("", IndexView.as_view(), name="index"),

    # Websites
    path("websites/", WebsitesView, name="websites"),
    path("websites/review/<int:pk>/", dns_check_page, name="dns check"),
    path("websites/add", WebsiteCreateView.as_view(), name="website create"),
    path("websites/delete/<int:pk>/", WebsiteDeleteView.as_view(), name="website delete"),
    path("websites/update/<int:pk>/", WebsiteUpdateView.as_view(), name="website update"),

    # User
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("register/", UserCreateView.as_view(), name="register"),

    # Profile
    path("profile-update/<int:pk>", ProfileUpdateView.as_view(), name="profile_update"),

    # Error
    path("404/", four_o_four, name="four_o_four"),

    # Logs
    path("websites/logs/<int:pk>/", logs_page, name="logs"),
]

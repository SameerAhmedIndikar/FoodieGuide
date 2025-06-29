from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from recipes.views import SignUpView  # Import your SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('accounts/', include('django.contrib.auth.urls')), 
    # Remove the explicit path('accounts/logout/', ...) and let auth.urls handle it
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
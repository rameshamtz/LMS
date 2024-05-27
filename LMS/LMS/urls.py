
from django.contrib import admin
from django.urls import path,include
from . import views
from . import user_login
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.baseView,name='base'),
    path('404',views.page_not_found,name='404'),
    path('',views.homeView,name='home'),
    path('product/filter-data',views.filter_data,name="filter-data"),
    path('search',views.search,name="search_course"),
    path('courses',views.singleCourseView,name='single_course'),
    path('course/<slug:slug>',views.course_details,name='course_details'),
    path('contact_us/',views.contactUsView,name='contact_us'),
    path('about_us/',views.aboutUsView,name='about_us'),
    path('accounts/register/',user_login.registerView,name='register'),
    path('accounts/login/',user_login.loginView,name='login'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/profile',user_login.profile,name='profile'),
    path('accounts/profile/update',user_login.profile_update,name='profile_update')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    # Examples:
    url(r'^$', 'newsletter.views.home', name='home'),
    url(r'^contact/$', 'newsletter.views.contact', name='contact'),
    url(r'^about/$', 'trydjango18.views.about', name='about'),
    url(r'^demo_home/$', 'dashboard.views.demo_home', name='demo_home'),
    url(r'^demo_sales/$', 'dashboard.views.demo_sales', name='demo_sales'),
    url(r'^demo_customers/$', 'dashboard.views.demo_customers', name='demo_customers'),
    url(r'^demo_acustomers/$', 'dashboard.views.demo_acustomers', name='demo_acustomers'),
    url(r'^demo_arefund/$', 'dashboard.views.demo_arefund', name='demo_arefund'),
    url(r'^zzz/$', 'dashboard.views.zzz', name='zzz'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
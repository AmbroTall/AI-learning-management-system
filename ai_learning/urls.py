"""
URL configuration for ai_learning project.
"""
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static

from learning.sitemaps import StaticSitemap, ModuleSitemap, JobSitemap, CertificateSitemap
from learning import views as learning_views

handler404 = learning_views.handler404
handler500 = learning_views.handler500

sitemaps = {
    'static': StaticSitemap,
    'modules': ModuleSitemap,
    'jobs': JobSitemap,
    'certificates': CertificateSitemap,
}


def robots_txt(request):
    lines = [
        'User-agent: *',
        'Allow: /',
        'Disallow: /admin/',
        'Disallow: /dashboard/',
        'Disallow: /profile/',
        'Disallow: /org/',
        'Disallow: /challenge/',
        'Disallow: /payments/',
        'Disallow: /notifications/',
        '',
        f'Sitemap: {settings.SITE_URL}/sitemap.xml',
    ]
    return HttpResponse('\n'.join(lines), content_type='text/plain')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('robots.txt', robots_txt),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('', include('learning.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

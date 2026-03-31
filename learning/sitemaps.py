from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Module, JobPosting, Certificate


class StaticSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return [
            'home', 'jobs', 'subscription_plans', 'register', 'login',
        ]

    def location(self, item):
        return reverse(item)


class ModuleSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.6

    def items(self):
        return Module.objects.filter(is_active=True)

    def location(self, obj):
        return reverse('module_detail', args=[obj.id])


class JobSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):
        return JobPosting.objects.filter(is_active=True)

    def location(self, obj):
        return reverse('jobs')

    def lastmod(self, obj):
        return obj.created_at


class CertificateSitemap(Sitemap):
    """Public certificate verification pages."""
    changefreq = 'never'
    priority = 0.3

    def items(self):
        return Certificate.objects.filter(is_valid=True)

    def location(self, obj):
        return reverse('verify_certificate', args=[obj.cert_number])

    def lastmod(self, obj):
        return obj.issued_at

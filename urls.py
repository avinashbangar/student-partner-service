from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'shareit.views.home', name='home'),
    # url(r'^shareit/', include('shareit.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^sign-up/','shareit.share.views.create'),
    url(r'^thankyou/','shareit.share.views.thankyou'),
    url(r'^thanks/','shareit.share.views.thanks'),
    url(r'^profile/(?P<id>\d+)/$','shareit.share.views.profile'),
    url(r'^requests/','shareit.share.views.requests'),
    url(r'^search/','shareit.share.views.search'),
    url(r'^results/','shareit.share.views.results'),
    url(r'^message/(?P<id>\d+)/$','shareit.share.views.message'),
    url(r'^mail/','shareit.share.views.mail'),
    url(r'^fbc/','shareit.share.views.fbc'),
    url(r'^login/','shareit.share.views.login'),
    url(r'^home/','shareit.facebook.views.home'),
    url(r'^token/(?P<id>\d+)/$','shareit.share.views.token'),
    url(r'^data/','shareit.share.views.data'),
    url(r'^fblogin/','shareit.facebook.views.login'),
    url(r'^about/','shareit.share.views.about'),
    url(r'^contact/','shareit.share.views.contact'),
    #(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    #(r'^fbck/', include('facebook.urls')),
)



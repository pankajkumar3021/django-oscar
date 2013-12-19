from django.conf.urls import patterns, url

from oscar.core.application import Application
from oscar.apps.dashboard.catalogue import views


class CatalogueApplication(Application):
    name = None

    default_permissions = ['is_staff', ]
    permissions_map = _map = {
        'catalogue-product': (['is_staff'], ['partner.dashboard_access']),
        'catalogue-product-create': (['is_staff'],
                                     ['partner.dashboard_access']),
        'catalogue-product-list': (['is_staff'], ['partner.dashboard_access']),
        'catalogue-product-delete': (['is_staff'],
                                     ['partner.dashboard_access']),
        'catalogue-product-lookup': (['is_staff'],
                                     ['partner.dashboard_access']),
    }

    product_list_view = views.ProductListView
    product_lookup_view = views.ProductLookupView
    product_create_redirect_view = views.ProductCreateRedirectView
    product_createupdate_view = views.ProductCreateUpdateView
    product_delete_view = views.ProductDeleteView

    product_class_list_view = views.ProductClassListView
    product_class_create_update_view = views.ProductClassCreateUpdateView
    product_class_delete_view = views.ProductClassDeleteView

    product_attribute_list_view = views.AttributeListView
    product_attribute_create_update_view = views.AttributeCreateUpdateView
    product_attribute_delete_view = views.AttributeDeleteView

    category_list_view = views.CategoryListView
    category_detail_list_view = views.CategoryDetailListView
    category_create_view = views.CategoryCreateView
    category_update_view = views.CategoryUpdateView
    category_delete_view = views.CategoryDeleteView

    stock_alert_view = views.StockAlertListView

    def get_urls(self):
        urls = [
            url(r'^products/(?P<pk>\d+)/$',
                self.product_createupdate_view.as_view(),
                name='catalogue-product'),
            url(r'^products/create/$',
                self.product_create_redirect_view.as_view(),
                name='catalogue-product-create'),
            url(r'^products/create/(?P<product_class_id>\d+)/$',
                self.product_createupdate_view.as_view(),
                name='catalogue-product-create'),
            url(r'^products/(?P<pk>\d+)/delete/$',
                self.product_delete_view.as_view(),
                name='catalogue-product-delete'),
            url(r'^$', self.product_list_view.as_view(),
                name='catalogue-product-list'),

            url(r'^stock-alerts/$', self.stock_alert_view.as_view(),
                name='stock-alert-list'),
            url(r'^product-lookup/$', self.product_lookup_view.as_view(),
                name='catalogue-product-lookup'),

            url(r'^categories/$', self.category_list_view.as_view(),
                name='catalogue-category-list'),
            url(r'^categories/(?P<pk>\d+)/$',
                self.category_detail_list_view.as_view(),
                name='catalogue-category-detail-list'),
            url(r'^categories/create/$', self.category_create_view.as_view(),
                name='catalogue-category-create'),
            url(r'^categories/(?P<pk>\d+)/update/$',
                self.category_update_view.as_view(),
                name='catalogue-category-update'),
            url(r'^categories/(?P<pk>\d+)/delete/$',
                self.category_delete_view.as_view(),
                name='catalogue-category-delete'),

            url(r'^product-classes/$', self.product_class_list_view.as_view(),
                name='catalogue-product-class-list'),
            url(r'^product-classes/(?P<pk>\d+)$', 
                self.product_class_create_update_view.as_view(),
                name='catalogue-product-class'),
            url(r'^product-classes/create/$', 
                self.product_class_create_update_view.as_view(),
                name='catalogue-product-class-create'),
            url(r'^product-classes/(?P<pk>\d+)/delete/$',
                self.product_class_delete_view.as_view(),
                name='catalogue-product-class-delete'),

            url(r'^product-attributes/$', 
                self.product_attribute_list_view.as_view(),
                name='catalogue-product-attribute-list'),
            url(r'^product-attributes/create/$', 
                self.product_attribute_create_update_view.as_view(),
                name='catalogue-product-attribute-create'),
            url(r'^product-attributes/(?P<pk>\d+)$', 
                self.product_attribute_create_update_view.as_view(),
                name='catalogue-product-attribute'),
           url(r'^product-attributes/(?P<pk>\d+)/delete/$',
                self.product_attribute_delete_view.as_view(),
                name='catalogue-product-attribute-delete'),

        ]
        return self.post_process_urls(patterns('', *urls))


application = CatalogueApplication()

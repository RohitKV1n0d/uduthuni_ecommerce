from oscar.apps.catalogue.views import ProductDetailView, CatalogueView

class ProductDetailView(ProductDetailView):
    template_name = 'oscar/catalogue/product_detail.html'


class CatalogueView(CatalogueView):
    template_name = 'oscar/catalogue/home.html'

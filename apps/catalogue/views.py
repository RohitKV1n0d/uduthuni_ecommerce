from oscar.apps.catalogue.views import ProductDetailView 

class ProductDetailView(ProductDetailView):
    template_name = 'oscar/catalogue/product_detail.html'

    
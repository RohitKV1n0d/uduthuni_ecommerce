from oscar.apps.catalogue.views import ProductDetailView, CatalogueView , ProductCategoryView


class ProductDetailView(ProductDetailView):
    template_name = 'oscar/catalogue/product_detail.html'


class CatalogueView(CatalogueView):
    template_name = 'oscar/catalogue/home.html'

class ProductCategoryView(ProductCategoryView):
    template_name = 'oscar/catalogue/catagory.html'
    

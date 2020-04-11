from django.shortcuts import render,get_object_or_404
from .models import Shop,Product,TutorialSeries
from django.http import HttpResponse

# Create your views here.

#from senate code example

def single_slug(request, single_slug):
    # first check to see if the url is in categories.

    categories = [c.category_slug for c in Shop.objects.all()]
    if single_slug in categories:
        matching_series = TutorialSeries.objects.filter(tutorial_category__category_slug=single_slug)
        series_urls = {}

        for m in matching_series.all():
            part_one = Product.objects.filter(tutorial_series__tutorial_series=m.tutorial_series)
            series_urls[m] = part_one

        return render(request=request,
                      template_name='products/shop_products.html',
                      context={"tutorial_series": matching_series, "part_ones": series_urls})
    
    tutorials = [t.tutorial_slug for t in Product.objects.all()]
    if single_slug in tutorials:
        return HttpResponse(f"{single_slug} is a tutorial")

    return HttpResponse(f"{single_slug} does not correspond")






def homepage(request):
    shops = Shop.objects.all()
    return render(request, 'products/shop.html',{'shops':shops})

# def shop_products(request, id):
#     products = Product.objects.filter(shop_id=id)
#     return render(request, 'products/shop_products.html', {'shops': shops})

# def product_details(request, id):
#     product_detail = get_object_or_404(Product, pk = id)
#     return render(request, 'products/product_details.html', {'product':product_detail})

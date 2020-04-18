from django.shortcuts import render, get_object_or_404
from .models import Shop, Product, ProductDetails
from django.http import HttpResponse
from django.db.models import Q

# Create your views here.

# from senate code example

#From Sentdex try again
def single_slug(request, single_slug):
    # loop through TutorialCategory objects so we can match slugs
    categories = [c.category_slug for c in Shop.objects.all()]
    if single_slug in categories:
        # find matching series by matching slugs
        # __ after a forieng key points to an attribute of that foriegn key
        matching_series = Product.objects.filter(tutorial_category__category_slug=single_slug)
        
        series_urls = {}
        for m in matching_series.all():
            # .earliest() can be used since we used DateTime field 
            part_one = ProductDetails.objects.filter(tutorial_series__tutorial_series=m.tutorial_series).earliest("tutorial_published")
            series_urls[m] = part_one.tutorial_slug

        return render(request,
                      "products/shop_products.html",
                      {"part_ones": series_urls})

    tutorials = [t.tutorial_slug for t in ProductDetails.objects.all()]
    if single_slug in tutorials:
        this_tutorial = ProductDetails.objects.get(tutorial_slug = single_slug)

        # Create sidebar showing series
        ## get tutorials in same series as this_tutorial
        #tutorials_from_series = ProductDetails.objects.filter(tutorial_series__tutorial_series=this_tutorial.tutorial_series).order_by("tutorial_published")

        ## convert to list to get index of this_tutorial
        #this_tutorial_idx = list(tutorials_from_series).index(this_tutorial)

        return render(request,
                      "products/product_details.html",
                      {"tutorial": this_tutorial,
                      })

    return HttpResponse(f"{single_slug} doesn't correspond to anything")




# def single_slug(request, single_slug):


#     # first check to see if the url is in categories.

#     categories = [c.shop_slug for c in Shop.objects.all()]
#     if single_slug in categories:
#         matching_series = Product.objects.filter(
#             shop_name__shop_slug=single_slug).all()
#         series_urls = {}

#         for m in matching_series.all():
#             part_one = Product.objects.filter(product_name=m.product_name)
#             series_urls[m] = part_one

#         return render(request=request,
#                       template_name='products/shop_products.html',
#                       context={"product_name": matching_series, "part_ones": series_urls})



#     products = Product.objects.filter(Q(shop_name__shop_slug=single_slug) | Q(
#             productdetails__test_something=single_slug))
#     return render(
#             request=request,
#             template_name='products/product_details.html',
#             context={"products": products, "slug":single_slug})
#     # product_details = [t.test_something for t in ProductDetails.objects.all()]
#     # if single_slug in product_details:
#     #     this_product = ProductDetails.objects.get(test_something=single_slug)

#     #     return render(request, 'products/product_details.html', {"product": this_product})
#     return HttpResponse(f"{single_slug} does not correspond")


# from stackoverflow
def product_details(request):
    products = Product.objects.filter(Q(shop_name__shop_slug=single_slug) | Q(
            productdetails__test_something=single_slug))
    return render(
            request=request,
            template_name='products/shop_products.html',
            context={"products": products, "slug":single_slug}
)



def homepage(request):
    shops = Shop.objects.all()
    return render(request, 'products/shop.html', {'shops': shops})

# def shop_products(request, id):
#     products = Product.objects.filter(shop_id=id)
#     return render(request, 'products/shop_products.html', {'shops': shops})

# def product_details(request, id):
#     product_detail = get_object_or_404(Product, pk = id)
#     return render(request, 'products/product_details.html', {'product':product_detail})

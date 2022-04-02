import pandas as pd
from django.shortcuts import render

from apps.products.models import Product, Purchase


def chart_select_view(request):
    product_df = pd.DataFrame(Product.objects.all().values())
    purchase_df = pd.DataFrame(Purchase.objects.all().values())
    print(product_df)
    context = {
        'products': product_df.to_html(),
        'purchases': purchase_df.to_html(),
    }
    return render(request, 'products/main.html', context)

import pandas as pd
from django.shortcuts import render

from apps.products.models import Product, Purchase


def chart_select_view(request):
    product_df = pd.DataFrame(Product.objects.all().values())
    purchase_df = pd.DataFrame(Purchase.objects.all().values())
    product_df['product_id'] = (Purchase.objects.all().values())
    df = pd.merge(purchase_df, product_df, on='product_id')
    context = {
        'products': product_df.to_html(),
        'purchases': purchase_df.to_html(),
        'df': df.to_html(),
    }
    return render(request, 'products/main.html', context)

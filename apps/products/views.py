import pandas as pd
from django.shortcuts import render

from apps.products.models import Product, Purchase


def chart_select_view(request):
    error_message = None
    df = None

    product_df = pd.DataFrame(Product.objects.all().values())
    purchase_df = pd.DataFrame(Purchase.objects.all().values())
    product_df['product_id'] = product_df['id']
    if purchase_df.shape[0] > 0:
        df = pd.merge(purchase_df, product_df, on='product_id').drop(['id_y', 'date_y'], axis=1).rename({'id_x': 'id', 'date_x': 'date'}, axis=1)
        if request.method == 'POST':
            chart_type = request.POST['sales']
            date_from = request.POST['date_from']
            date_to = request.POST['date_to']
    else:
        error_message = 'No records in the database'
        df = ''
    context = {
        'error_message': error_message,
        # 'products': product_df.to_html(),
        # 'purchases': purchase_df.to_html(),
        'df': df.to_html(),
    }
    return render(request, 'products/main.html', context)

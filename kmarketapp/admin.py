from django.contrib import admin
from.models import *

all_models = [Cart, Master, Product,
            ProductCategory, ProductImage,
            Seller, UserProfile, UserRole, Wishlist]

for model in all_models:
    admin.site.register(model)


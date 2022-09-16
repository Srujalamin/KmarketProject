# Generated by Django 4.1 on 2022-09-15 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("kmarketapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ProductName", models.CharField(max_length=30)),
                ("ProductPrice", models.DecimalField(decimal_places=2, max_digits=7)),
                ("Quantity", models.IntegerField()),
            ],
            options={"db_table": "product",},
        ),
        migrations.CreateModel(
            name="ProductCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Category", models.CharField(max_length=30)),
            ],
            options={"db_table": "productcategory",},
        ),
        migrations.CreateModel(
            name="Wishlist",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "Product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="kmarketapp.product",
                    ),
                ),
                (
                    "UserProfile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="kmarketapp.userprofile",
                    ),
                ),
            ],
            options={"db_table": "wishlist",},
        ),
        migrations.CreateModel(
            name="Seller",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("SellerName", models.CharField(max_length=50)),
                ("GSTN", models.CharField(max_length=15)),
                (
                    "UserProfile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="kmarketapp.userprofile",
                    ),
                ),
            ],
            options={"db_table": "seller",},
        ),
        migrations.CreateModel(
            name="ProductImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "Image",
                    models.FileField(default="avatar.png", upload_to="products/"),
                ),
                (
                    "Product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="kmarketapp.product",
                    ),
                ),
            ],
            options={"db_table": "productimage",},
        ),
        migrations.AddField(
            model_name="product",
            name="ProductCategory",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="kmarketapp.productcategory",
            ),
        ),
        migrations.CreateModel(
            name="Cart",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Quantity", models.IntegerField()),
                ("TotalPrice", models.DecimalField(decimal_places=2, max_digits=7)),
                (
                    "Product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="kmarketapp.product",
                    ),
                ),
                (
                    "UserProfile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="kmarketapp.userprofile",
                    ),
                ),
            ],
            options={"db_table": "cart",},
        ),
    ]
from django.db import models

class UserRole(models.Model):
    Role = models.CharField(max_length=10)

    class Meta:
        db_table = 'userrole'

    def __str__(self) -> str:
        return self.Role

class Master(models.Model):
    UserRole = models.ForeignKey(UserRole, on_delete=models.CASCADE)
    Email = models.EmailField(unique=True)
    Password =models.CharField(max_length=12)
    isActive=models.BooleanField(default=False)
    DateCreated = models.DateTimeField(auto_now_add=True)
    DateModified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'master'

    def __str__(self) -> str:
        return self.Email

gender_choices = (
    ('m', 'male'),
    ('f', 'female'),
)

class UserProfile(models.Model):
    Master = models.ForeignKey(Master, on_delete=models.CASCADE)
    ProfileImage = models.FileField(upload_to="profiles/", default='avatar.png')
    FullName = models.CharField(max_length=30, blank=True, default='')
    Gender = models.CharField(max_length=10, choices=gender_choices)
    Mobile = models.CharField(max_length=10, blank=True, default='')
    BirthDate = models.DateField(default="1990-01-01")
    Country = models.CharField(max_length=30, blank=True, default='')
    State = models.CharField(max_length=30, blank=True, default='')
    City = models.CharField(max_length=30, blank=True, default='')
    Address = models.CharField(max_length=30, blank=True, default='')

    class Meta:
        db_table = 'userprofile'

    def __str__(self) -> str:
        return self.FullName if self.FullName else 'No Name! Need to be update.'

class Seller(models.Model):
    UserProfile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    SellerName = models.CharField(max_length=50)
    GSTN = models.CharField(max_length=15)

    class Meta:
        db_table = 'seller'

class ProductCategory(models.Model):
    Category = models.CharField(max_length=30)

    class Meta:
        db_table = 'productcategory'

class Product(models.Model):
    ProductCategory = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    ProductName = models.CharField(max_length=30)
    ProductPrice = models.DecimalField(decimal_places=2, max_digits=7)
    Quantity = models.IntegerField()

    class Meta:
        db_table = 'product'

class ProductImage(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Image = models.FileField(upload_to="products/", default='avatar.png')

    class Meta:
        db_table = 'productimage'

class Wishlist(models.Model):
    UserProfile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'wishlist'

class Cart(models.Model):
    UserProfile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Quantity = models.IntegerField()
    TotalPrice = models.DecimalField(decimal_places=2, max_digits=7)

    class Meta:
        db_table = 'cart'
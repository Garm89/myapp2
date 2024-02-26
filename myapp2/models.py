from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    registration_date = models.DateField(auto_now_add=True)

# Create
new_client = Client.objects.create(name='Имя клиента', email='email@example.com', phone_number='1234567890', address='Адрес клиента')

# Read
all_clients = Client.objects.all()
specific_client = Client.objects.get(id=1)

# Update
specific_client.name = 'Новое имя клиента'
specific_client.save()

# Delete
specific_client.delete()    

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    added_date = models.DateField(auto_now_add=True)


# Create
new_product = Product.objects.create(name='Название продукта', description='Описание продукта', price=10.00, quantity=100)

# Read
all_products = Product.objects.all()
specific_product = Product.objects.get(id=1)

# Update
specific_product.price = 15.00
specific_product.save()

# Delete
specific_product.delete()    

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateField(auto_now_add=True)


# Create
new_order = Order.objects.create(client=specific_client, total_amount=100.00)

# Read
all_orders = Order.objects.all()
specific_order = Order.objects.get(id=1)

# Update
specific_order.total_amount = 150.00
specific_order.save()

# Delete
specific_order.delete()    
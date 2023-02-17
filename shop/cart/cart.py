from decimal import Decimal
from django.conf import settings
from users.models import Product

class Cart(object):

    def __init__(self, request):

        # ініціалізація корзини.
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # зберігаємо пусту корзину у нашій сесії
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
    
    def __iter__(self):

        # Перебираєм товари в корзині і отримуємо товари із бази данних.

        product_ids = self.cart.keys()
        # Отримуєм товари і добавляємо їх в корзину.
        products = Product.objects.filter(id__in=product_ids)

        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        # Рахуємо кількість товарів в корзині
        return sum(item['quantity'] for item in self.cart.values())

    def add(self, product, quantity=1, update_quantity=False):
        # Добавляєм товари в корзину або обновляємо його кількість.

        product_id = str(product_id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity':0,
            'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()
    
    def save(self):
        # Зберігаємо товар
        self.session.modified = True
    
    def remove(self, product):
        # Видаляємо товар
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
    
    def get_total_price(self):
        # Отримуємо загальну вартість
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
    
    def clear(self):
        # Очистити корзину в  сесії
        del self.session[settings.CART_SESSION_ID]
        self.save()


from store.models import Product, Profile


class Cart():
    def __init__(self, request):
        self.session = request.session
        # Get request
        self.request = request
        # Get the current session key if it exists
        cart = self.session.get('session_key')

        # If the user is new, no session key!  Create one!
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # Make sure cart is available on all pages of site
        self.cart = cart

    def add(self, product,quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
        # Logic
        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

        # Deal with logged in user
        if self.request.user.is_authenticated:
			# Get the current user profile
            current_user = Profile.objects.filter(user__id=self.request.user.id)
			# Convert {'3':1, '2':4} to {"3":1, "2":4}
            carty = str(self.cart)
            carty = carty.replace("\'", "\"")
            # Save carty to the Profile Model
            current_user.update(old_cart=str(carty))



    def db_add(self, product, quantity):
        product_id = str(product)
        product_qty = str(quantity)
        # Logic
        if product_id in self.cart:
            pass
        else:
            #self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)

        self.cart[product_id] = int(product_qty)


        # Deal with logged in user
        if self.request.user.is_authenticated:
			# Get the current user profile
            current_user = Profile.objects.filter(user__id=self.request.user.id)
			# Convert {'3':1, '2':4} to {"3":1, "2":4}
            carty = str(self.cart)
            carty = carty.replace("\'", "\"")
			# Save carty to the Profile Model
            current_user.update(old_cart=str(carty))


           
    
    def __len__(self):
        return len(self.cart)
    
    

    def get_prods(self):
		# Get ids from cart
        product_ids = self.cart.keys()
		# Use ids to lookup products in database model
        products = Product.objects.filter(id__in=product_ids)

		# Return those looked up products
        return products
    
    def get_quants(self):
        quantities = self.cart
        return quantities
    

    def update(self, product, quantity):
            product_id = str(product)
            product_qty = int(quantity)

            # Get cart
            ourcart = self.cart
            # Update Dictionary/cart
            ourcart[product_id] = product_qty


            self.session.modified = True
            if self.request.user.is_authenticated:
                # Get the current user profile
                current_user = Profile.objects.filter(user__id=self.request.user.id)
			    # Convert {'3':1, '2':4} to {"3":1, "2":4}
                carty = str(self.cart)
                carty= carty.replace("\'", "\"")
			    # Save carty to the Profile Model
                current_user.update(old_cart=str(carty))



            thing = self.cart
            return thing
    


    def delete(self, product):
        product_id = str(product)
        # Delete from dictionary/cart
        if product_id in self.cart:
            del self.cart[product_id]
        

        self.session.modified = True

        # Deal with logged in user
        if self.request.user.is_authenticated:
            # Get the current user profile
            current_user = Profile.objects.filter(user__id=self.request.user.id)
			# Convert {'3':1, '2':4} to {"3":1, "2":4}
            carty = str(self.cart)
            carty = carty.replace("\'", "\"")
			# Save carty to the Profile Model
            current_user.update(old_cart=str(carty))



    def cart_total(self):
        # Get product IDs from the cart
        product_ids = self.cart.keys()
        # Lookup those keys in our products database model
        products = Product.objects.filter(id__in=product_ids)
         # Initialize total
        total = 0
    
        for product in products:
            # Check if the product ID exists in the cart
            if str(product.id) in self.cart:
            # Get the quantity of the product from the cart
             quantity = self.cart[str(product.id)]
            # Calculate total based on whether the product is on sale or not
            if product.is_sale:
                 total += product.sale_price * quantity
            else:
                total += product.price * quantity

        return total

    


  

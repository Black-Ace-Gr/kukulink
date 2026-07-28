from marketplace.models import Product


def search_products(question):

    products = Product.objects.all()

    q = question.lower()
    if "register" in q:
        return "Click Register in the navigation bar, create your account, verify your details, and you can begin buying or selling."

    if "sell" in q:
        return "After logging in, go to Dashboard → Add Product and complete the product details."

    if "buyer" in q:
        return "Browse the marketplace, open a listing, and contact the seller from the product page."

    if "broiler" in q:
        products = products.filter(name__icontains="broiler")

    elif "layer" in q:
        products = products.filter(name__icontains="layer")

    elif "egg" in q:
        products = products.filter(name__icontains="egg")

    elif "feed" in q:
        products = products.filter(name__icontains="feed")

    return list(products[:15])

def serialize(products):

    result = ""

    for p in products:

        result += f"""

Product: {p.name}

Price: {p.price}

Seller: {p.seller.username}

"""

    return result
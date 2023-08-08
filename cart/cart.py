from mysite import settings


class Cart:
    def __init__(self, request):
        """
        장바구니를 초기화 합니다.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

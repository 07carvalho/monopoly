
class Property:

    def __init__(self, position, sale_price, rental_price, owner):
        self._position = position
        self._sale_price = sale_price
        self._rental_price = rental_price
        self._owner = owner

    @property
    def owner(self):
        """get owner"""
        return self._owner

    @owner.setter
    def owner(self, owner):
        """set owner"""
        self._owner = owner


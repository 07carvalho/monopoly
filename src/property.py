
class Property:

    def __init__(self, position: int, sale_price: int, rental_price: int, owner):
        self._position = position
        self._sale_price = sale_price
        self._rental_price = rental_price
        self._owner = owner

    def __str__(self):
        return str(self._position)

    @property
    def position(self) -> int:
        """get position"""
        return self._position

    @position.setter
    def position(self, num: int):
        """set position"""
        self._position = num

    @property
    def sale_price(self) -> int:
        """get sale price"""
        return self._sale_price

    @sale_price.setter
    def sale_price(self, sale_price: int):
        """set sale price"""
        self._sale_price = sale_price

    @property
    def rental_price(self) -> int:
        """get rental price"""
        return self._rental_price

    @rental_price.setter
    def rental_price(self, value: int):
        """set rental price"""
        self._rental_price = value

    @property
    def owner(self):
        """get owner"""
        return self._owner

    @owner.setter
    def owner(self, player):
        """set owner"""
        self._owner = player

    def has_owner(self) -> bool:
        return self.owner is not None

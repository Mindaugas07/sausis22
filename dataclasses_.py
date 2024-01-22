from dataclasses import dataclass
from typing import List

# @dataclass
# class Address:
#     street_name: str
#     house_number: str
#     postal_code: str


# @dataclass
# class Person:
#     name: str
#     age: int
#     email: str
#     address: Address

#     def get_name(self) -> str:
#         return self.name


# human = Person(
#     name="Jogaila",
#     age=45,
#     email="jogaila@gmail.com",
#     address=Address(street_name="Naujakuriu", house_number="45", postal_code="456789"),
# )

# print(human.get_name())

# print(human, human.name, human.age, human.age == 45, human.email)

# human_one = Person(name="Jogaila", age=45, email="jogaila@gmail.com")

# employee_list = [human, Person(name="Kestutis", age=55, email="kestas@gmail.com")]

# class CEO:
#     apple = Person(name="Jogaila", age=45, email="jogaila@gmail.com")
#     intel = Person(name="Jogaila", age=45, email="jogaila@gmail.com")

# CEO.apple.age


# @dataclass
# class Product:
#     id: str
#     name: str
#     description: str
#     price: float
#     quantity_in_stock: int

#     def calculate_total_cost(self, amount: int, discount: float = None) -> float:
#         if discount:
#             return self.price * amount * discount
#         else:
#             return self.price * amount


# milk = Product(
#     id=45,
#     name="Milk FTW",
#     description="Low fat high protein milk.",
#     price=1.1,
#     quantity_in_stock=456,
# )

# print(milk.calculate_total_cost(20))
# print(milk.calculate_total_cost(20, 0.9))


@dataclass
class Book:
    book_id: int
    title: str
    author: "Author"
    publication_year: int
    price: float
    quantity_in_stock: int

    # def __post_init__(
    #     self,
    #     book_id: int,
    #     title: str,
    #     publication_year: int,
    #     price: float,
    #     quantity_in_stock: int,
    #     author: "Author",
    # ):
    #     self.book_id = book_id
    #     self.title = title
    #     self.publication_year = publication_year
    #     self.price = price
    #     self.quantity_in_stock = quantity_in_stock
    #     self.author = author

    def sell(self, quantity: int) -> int:
        self.quantity_in_stock -= quantity


@dataclass
class Author:
    author_id: int
    name: str
    birth_year: int
    books: List[Book]

    # def __post_init__(
    #     self, author_id: int, name: str, birth_year: int, books: List[Book]
    # ):
    #     self.author_id = author_id
    #     self.name = name
    #     self.birth_year = birth_year
    #     self.books = []


@dataclass
class Order:
    order_id: str
    customer: "Customer"
    books: List[Book]
    total_price: float
    status: str("Pending" or "Shipped")

    # def __post_init__(
    #     self,
    #     order_id: str,
    #     customer: "Customer",
    #     books: List[Book],
    #     tottal_price: float,
    #     status: str("Pending" or "Shipped"),
    # ) -> None:
    #     self.order_id = order_id
    #     self.customer = customer
    #     self.books = []
    #     self.tottal_price = tottal_price
    #     self.status = status

    def calculate_total_price(self) -> float:
        self.total__price = 0
        for book in self.books:
            self.total__price += book.price
        return self.total__price


@dataclass
class Customer:
    customer_id: str
    name: str
    email: str
    orders: List[Order]

    # def __post_init__(
    #     self, customer_id: str, name: str, email: str, orders: List[Order]
    # ) -> None:
    #     self.customer_id = customer_id
    #     self.name = name
    #     self.email = email
    #     self.orders = []


jungle_book = Book(
    book_id="456789fdsg",
    title="Jungle Book",
    publication_year=1945,
    price=20.45,
    quantity_in_stock=213,
    author=Author(
        author_id="1245",
        name="Tom Bairon",
        birth_year=1912,
        books=[Book],
    ),
)


bible = Book(
    book_id="456789",
    title="The Bible",
    publication_year=12,
    price=9.99,
    quantity_in_stock=1000,
    author=Author(
        author_id="2222",
        name="Jesus",
        birth_year=1212,
        books=[Book],
    ),
)


customer_jonas = Customer(
    customer_id="789546",
    name="Jonas Petraitis",
    email="jjjppp@gmail.com",
    orders=List[Order],
)

order_jonas = Order(
    order_id="78965",
    customer=customer_jonas,
    books=[jungle_book, bible, bible],
    total_price=Order.calculate_total_price(),
    status="Pending",
)

print(jungle_book.quantity_in_stock)
jungle_book.sell(12)
print(jungle_book.quantity_in_stock)
print(jungle_book.author.name)
print(order_jonas.books)

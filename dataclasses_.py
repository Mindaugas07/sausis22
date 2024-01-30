from dataclasses import dataclass, field
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


# @dataclass
# class Book:
#     book_id: int
#     title: str
#     author: "Author"
#     publication_year: int
#     price: float
#     quantity_in_stock: int

#     # def __post_init__(
#     #     self,
#     #     book_id: int,
#     #     title: str,
#     #     publication_year: int,
#     #     price: float,
#     #     quantity_in_stock: int,
#     #     author: "Author",
#     # ):
#     #     self.book_id = book_id
#     #     self.title = title
#     #     self.publication_year = publication_year
#     #     self.price = price
#     #     self.quantity_in_stock = quantity_in_stock
#     #     self.author = author

#     def sell(self, quantity: int) -> int:
#         self.quantity_in_stock -= quantity


# @dataclass
# class Author:
#     author_id: int
#     name: str
#     birth_year: int
#     books: List["Book"]

#     # def __post_init__(
#     #     self, author_id: int, name: str, birth_year: int, books: List[Book]
#     # ):
#     #     self.author_id = author_id
#     #     self.name = name
#     #     self.birth_year = birth_year
#     #     self.books = []


# @dataclass
# class Customer:
#     customer_id: str
#     name: str
#     email: str
#     # orders: List["Order"] = field(default_factory=List)
#     orders: List["Order"]

#     # def __post_init__(
#     #     self, customer_id: str, name: str, email: str, orders: List[Order]
#     # ) -> None:
#     #     self.customer_id = customer_id
#     #     self.name = name
#     #     self.email = email
#     #     self.orders = []


# @dataclass
# class Customer:
#     customer_id: str
#     name: str
#     email: str
#     # orders: List[Order] = field(default_factory=List)
#     orders: List["Order"]
#     # def __post_init__(
#     #     self, customer_id: str, name: str, email: str, orders: List[Order]
#     # ) -> None:
#     #     self.customer_id = customer_id
#     #     self.name = name
#     #     self.email = email
#     #     self.orders = []


# @dataclass
# class Order:
#     order_id: str
#     customer: "Customer"
#     total_price: float
#     status: str
#     books: List["Book"]

#     # def __post_init__(
#     #     self,
#     #     order_id: str,
#     #     customer: "Customer",
#     #     books: List[Book],
#     #     tottal_price: float,
#     #     status: str("Pending" or "Shipped"),
#     # ) -> None:
#     #     self.order_id = order_id
#     #     self.customer = customer
#     #     self.books = []
#     #     self.tottal_price = tottal_price
#     #     self.status = status

#     def calculate_total_price(self) -> float:
#         total_price_final = 0
#         for book in self.books:
#             total_price_final += Book.price
#         return total_price_final


# jungle_book = Book(
#     book_id="456789fdsg",
#     title="Jungle Book",
#     publication_year=1945,
#     price=20.45,
#     quantity_in_stock=213,
#     author=Author(
#         author_id="1245",
#         name="Tom Bairon",
#         birth_year=1912,
#         books=[Book],
#     ),
# )


# bible = Book(
#     book_id="456789",
#     title="The Bible",
#     publication_year=12,
#     price=9.99,
#     quantity_in_stock=1000,
#     author=Author(
#         author_id="2222",
#         name="Jesus",
#         birth_year=1212,
#         books=[Book],
#     ),
# )

# author_jesus = Author(author_id="2222", name="Jesus", birth_year=1212, books=[bible])
# author_bairon = Author(
#     author_id="1245", name="Tom Bairon", birth_year=1912, books=[jungle_book]
# )

# customer_jonas = Customer(
#     customer_id="789546",
#     name="Jonas Petraitis",
#     email="jjjppp@gmail.com",
#     orders=List[Order],
# )

# order_jonas = Order(
#     order_id="78965",
#     customer=customer_jonas,
#     books=[jungle_book, bible],
#     total_price=Order.calculate_total_price(),
#     status="Pending",
# )

# print(jungle_book.quantity_in_stock)
# jungle_book.sell(12)
# # author_jungle_book_books = jungle_book.author.books
# print(jungle_book.quantity_in_stock)
# print(jungle_book.author.name)
# print(author_bairon.books)
# # print(order_jonas.calculate_total_price())
# print(order_jonas.books)


# @dataclass
# class Book:
#     title: str
#     author: str
#     publication_year: int
#     isbn: str


# @dataclass
# class Library:
#     books: List["Book"]

#     def add_book(self, book) -> None:
#         self.books.append(book)

#     def remove_book(self, book) -> None:
#         self.books.remove(book)

#     def search_book_by_title(self, name) -> str:
#         if len(self.books) > 0:
#             for book in self.books:
#                 if name in book.title:
#                     return f"Book '{book.title}' is in the library"
#                 else:
#                     return f"Book '{name}' is not present in the library"
#         else:
#             return "No books in the library"

#     def search_book_by_author(self, author) -> str:
#         if len(self.books) > 0:
#             for book in self.books:
#                 if author in book.author:
#                     return f"Book '{book.title}' written by {book.author} is in the library"
#                 else:
#                     return f"No book is present in the library written by {author}"
#         else:
#             return "No books in the library"

#     def get_books(self) -> List[str]:
#         return self.books


# jungle_book = Book(
#     title="Jungle Book",
#     author="Vytautas Jogaila",
#     publication_year=1945,
#     isbn="789ty",
# )

# bible = Book(
#     title="The Bible",
#     author="Tom Bairon",
#     publication_year=12,
#     isbn="456ret",
# )

# library_one = Library([])
# library_one.add_book(bible)
# print(library_one.get_books())
# library_one.remove_book(bible)
# print(library_one.get_books())
# print(library_one.search_book_by_author("Tom"))
# print(library_one.search_book_by_author("Tim"))
# library_one.add_book(bible)
# library_one.add_book(jungle_book)
# print(library_one.get_books())
# print(library_one.search_book_by_author("Tom"))
# print(library_one.search_book_by_author("Tim"))


@dataclass
class Employee:
    employee_id: int
    name: str
    age: str
    salary: float
    department: "Department"


@dataclass
class Department:
    department_id: int
    name: str
    employees: List["Employee"]

    def average_salary(self) -> float:
        total_dep_salary = 0
        for index, employee in enumerate(self.employees):
            total_dep_salary += employee.salary
        return total_dep_salary / (index + 1)

    def get_name(self) -> str:
        return self.name


@dataclass
class EmployeeManagement:
    departments: List["Department"]

    def get_all_employees(self) -> List["Employee"]:
        all_employees = []
        for department in self.departments:
            for employee in department.employees:
                all_employees.append(employee)
        return all_employees

    def total_salary(self) -> float:
        total_comp_salary = 0
        for department in self.departments:
            for employee in department.employees:
                total_comp_salary += employee.salary
        return total_comp_salary

    def get_employees_in_age_range(
        self, min_age: int, max_age: int
    ) -> List["Employee"]:
        all_employees = EmployeeManagement.get_all_employees(self)
        filtered_employees = list(
            filter(lambda employee: min_age <= employee.age <= max_age, all_employees)
        )
        return filtered_employees

    def sort_employees_by_salary(self) -> List["Employee"]:
        all_employees = EmployeeManagement.get_all_employees(self)
        sorted_employees_by_salary = [employee for employee in all_employees]
        return sorted(sorted_employees_by_salary, key=lambda d: d.salary, reverse=True)

    def filter_employees_by_department(
        self, department_name: "Department"
    ) -> List["Employee"]:
        all_employees = EmployeeManagement.get_all_employees(self)
        filtered_employees_by_department = list(
            filter(
                lambda employee: employee.department == department_name, all_employees
            )
        )
        return filtered_employees_by_department


empl_one = Employee(
    employee_id=123,
    name="Vardenis Pavardenis",
    age=45,
    salary=45000,
    department="Sales department",
)
empl_two = Employee(
    employee_id=754,
    name="Vytautas Jogaila",
    age=19,
    salary=78000,
    department="Sales department",
)
empl_three = Employee(
    employee_id=444,
    name="Algirdas Kestutis",
    age=60,
    salary=100000,
    department="Finances department",
)


sales_department = Department(
    department_id=456798, name="Sales department", employees=[empl_one, empl_two]
)
financial_department = Department(
    department_id=789456, name="Finances department", employees=[empl_three]
)

management = EmployeeManagement(departments=[sales_department, financial_department])

print(sales_department.average_salary())
print(management.total_salary())
print(sales_department.employees)
print(management.get_employees_in_age_range(min_age=21, max_age=99))
print(management.sort_employees_by_salary())
print(management.filter_employees_by_department("Sales department"))


# from dataclasses import dataclass


# def get_default_age(gender: int) -> int:
#     return 0 if gender == "male" else 1


# def get_default_gender():
#     return "female"


# @dataclass
# class Person:
#     name: str
#     # age: int = field(default_factory=lambda title: get_default_age(title))
#     gender: str = field(default_factory=get_default_gender)


# p1 = Person(name="John", title="male")
# print(p1)  # Person(name='John', age=18, gender='male')

# p2 = Person("Jane", 25, "female")
# print(p2)  # Person(name='Jane', age=25, gender='female')

# from dataclasses import dataclass


# @dataclass(frozen=True)
# class Person:
#     name: str
#     age: int


# jonas = Person(name="Jonas", age=21)
# jonas.name = "Vytautas"
# print(jonas.name)


# @dataclass
# class Person:
#     name: str
#     age: int


# @dataclass
# class Employee(Person):
#     id: str
#     department: str


# empl = Employee(name="John", age=30, id="1234", department="Sales")
# print(empl)

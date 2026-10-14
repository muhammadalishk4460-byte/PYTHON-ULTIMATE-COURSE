"""
Professional Dealership Management System
------------------------------------------
Features:
  - Vehicle inventory (Car, Bike) using inheritance
  - Customer and Salesperson management
  - Sales with discount, tax, commission and invoice
  - Search / filter vehicles
  - Reports (inventory value, sales, top salesperson)
  - Data saved in JSON file (dealership_data.json)

Run:  python dealership_system.py
"""

from __future__ import annotations

import json
from abc import ABC, abstractmethod
from datetime import datetime
from pathlib import Path

DATA_FILE = Path(__file__).with_name("dealership_data.json")
TAX_RATE = 0.18  # 18% tax - apni marzi se change kar lena


# ----------------------------------------------------------------------
# Custom Exceptions
# ----------------------------------------------------------------------
class DealershipError(Exception):
    """Base error for the dealership system."""


class NotFoundError(DealershipError):
    pass


class InvalidOperationError(DealershipError):
    pass


_counters: dict[str, int] = {}


def new_id(prefix: str) -> str:
    """Short sequential IDs: V001, C001, E001, S001."""
    _counters[prefix] = _counters.get(prefix, 0) + 1
    return f"{prefix}{_counters[prefix]:03d}"


def register_id(existing_id: str) -> None:
    """Saved data load hone par counter aage barhao (old IDs ignore)."""
    letters = existing_id.rstrip("0123456789")
    digits = existing_id[len(letters):]
    if letters and digits:
        _counters[letters] = max(_counters.get(letters, 0), int(digits))


# ----------------------------------------------------------------------
# Vehicles
# ----------------------------------------------------------------------
class Vehicle(ABC):
    vehicle_type = "Vehicle"

    def __init__(self, make, model, year, price, color, mileage=0,
                 status="available", vehicle_id=None):
        if price <= 0:
            raise InvalidOperationError("Price positive honi chahiye.")
        if not 1950 <= int(year) <= datetime.now().year + 1:
            raise InvalidOperationError("Year ghalat hai.")
        self.vehicle_id = vehicle_id or new_id("V")
        self.make = make
        self.model = model
        self.year = int(year)
        self.price = float(price)
        self.color = color
        self.mileage = int(mileage)
        self.status = status  # available / sold

    @property
    def is_available(self) -> bool:
        return self.status == "available"

    def mark_sold(self) -> None:
        if not self.is_available:
            raise InvalidOperationError("Ye gaari pehle hi sold hai.")
        self.status = "sold"

    @abstractmethod
    def extra_info(self) -> str:
        """Subclass-specific details."""

    @abstractmethod
    def extra_data(self) -> dict:
        """Subclass-specific data for saving."""

    def to_dict(self) -> dict:
        data = {
            "type": self.vehicle_type,
            "vehicle_id": self.vehicle_id,
            "make": self.make,
            "model": self.model,
            "year": self.year,
            "price": self.price,
            "color": self.color,
            "mileage": self.mileage,
            "status": self.status,
        }
        data.update(self.extra_data())
        return data

    def title(self) -> str:
        return f"{self.year} {self.make} {self.model}"

    def __str__(self) -> str:
        return (f"[{self.vehicle_id}] {self.vehicle_type:<5} | {self.title():<28} | "
                f"{self.color:<8} | {self.mileage:>7} km | Rs {self.price:>12,.0f} | "
                f"{self.status.upper():<9} | {self.extra_info()}")


class Car(Vehicle):
    vehicle_type = "Car"

    def __init__(self, *args, doors=4, transmission="Manual", fuel="Petrol", **kwargs):
        super().__init__(*args, **kwargs)
        self.doors = int(doors)
        self.transmission = transmission
        self.fuel = fuel

    def extra_info(self) -> str:
        return f"{self.doors} doors, {self.transmission}, {self.fuel}"

    def extra_data(self) -> dict:
        return {"doors": self.doors, "transmission": self.transmission, "fuel": self.fuel}


class Bike(Vehicle):
    vehicle_type = "Bike"

    def __init__(self, *args, engine_cc=70, bike_type="Standard", **kwargs):
        super().__init__(*args, **kwargs)
        self.engine_cc = int(engine_cc)
        self.bike_type = bike_type

    def extra_info(self) -> str:
        return f"{self.engine_cc}cc, {self.bike_type}"

    def extra_data(self) -> dict:
        return {"engine_cc": self.engine_cc, "bike_type": self.bike_type}


def vehicle_from_dict(d: dict) -> Vehicle:
    common = dict(
        vehicle_id=d["vehicle_id"], status=d["status"], mileage=d["mileage"],
    )
    base = (d["make"], d["model"], d["year"], d["price"], d["color"])
    if d["type"] == "Car":
        return Car(*base, doors=d["doors"], transmission=d["transmission"],
                   fuel=d["fuel"], **common)
    if d["type"] == "Bike":
        return Bike(*base, engine_cc=d["engine_cc"], bike_type=d["bike_type"], **common)
    raise DealershipError(f"Unknown vehicle type: {d['type']}")


# ----------------------------------------------------------------------
# People
# ----------------------------------------------------------------------
class Person:
    def __init__(self, name, phone, email="", person_id=None, prefix="P"):
        self.person_id = person_id or new_id(prefix)
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self) -> str:
        return f"[{self.person_id}] {self.name} | {self.phone} | {self.email}"


class Customer(Person):
    def __init__(self, name, phone, email="", cnic="", person_id=None, purchases=None):
        super().__init__(name, phone, email, person_id, prefix="C")
        self.cnic = cnic
        self.purchases = purchases or []  # list of sale ids

    def to_dict(self) -> dict:
        return {"person_id": self.person_id, "name": self.name, "phone": self.phone,
                "email": self.email, "cnic": self.cnic, "purchases": self.purchases}


class Salesperson(Person):
    def __init__(self, name, phone, email="", commission_rate=0.02,
                 person_id=None, total_commission=0.0):
        super().__init__(name, phone, email, person_id, prefix="E")
        self.commission_rate = float(commission_rate)
        self.total_commission = float(total_commission)

    def earn(self, sale_amount: float) -> float:
        commission = sale_amount * self.commission_rate
        self.total_commission += commission
        return commission

    def to_dict(self) -> dict:
        return {"person_id": self.person_id, "name": self.name, "phone": self.phone,
                "email": self.email, "commission_rate": self.commission_rate,
                "total_commission": self.total_commission}


# ----------------------------------------------------------------------
# Sale
# ----------------------------------------------------------------------
class Sale:
    def __init__(self, vehicle_id, vehicle_title, customer_id, customer_name,
                 salesperson_id, salesperson_name, price, discount, payment_method,
                 sale_id=None, date=None, tax=None, total=None, commission=None):
        self.sale_id = sale_id or new_id("S")
        self.vehicle_id = vehicle_id
        self.vehicle_title = vehicle_title
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.salesperson_id = salesperson_id
        self.salesperson_name = salesperson_name
        self.price = price
        self.discount = discount
        self.payment_method = payment_method
        self.date = date or datetime.now().strftime("%Y-%m-%d %H:%M")
        taxable = price - discount
        self.tax = tax if tax is not None else taxable * TAX_RATE
        self.total = total if total is not None else taxable + self.tax
        self.commission = commission or 0.0

    def invoice(self) -> str:
        line = "=" * 52
        return (
            f"{line}\n"
            f"{'DEALERSHIP INVOICE':^52}\n"
            f"{line}\n"
            f"Invoice No : {self.sale_id}\n"
            f"Date       : {self.date}\n"
            f"Customer   : {self.customer_name} ({self.customer_id})\n"
            f"Salesperson: {self.salesperson_name}\n"
            f"Vehicle    : {self.vehicle_title} ({self.vehicle_id})\n"
            f"Payment    : {self.payment_method}\n"
            f"{'-' * 52}\n"
            f"Price      : Rs {self.price:>15,.2f}\n"
            f"Discount   : Rs {self.discount:>15,.2f}\n"
            f"{f'Tax ({TAX_RATE * 100:.0f}%)':<11}: Rs {self.tax:>15,.2f}\n"
            f"{'-' * 52}\n"
            f"TOTAL      : Rs {self.total:>15,.2f}\n"
            f"{line}"
        )

    def to_dict(self) -> dict:
        return dict(self.__dict__)


# ----------------------------------------------------------------------
# Dealership (main controller)
# ----------------------------------------------------------------------
class Dealership:
    def __init__(self, name: str):
        self.name = name
        self.vehicles: dict[str, Vehicle] = {}
        self.customers: dict[str, Customer] = {}
        self.staff: dict[str, Salesperson] = {}
        self.sales: list[Sale] = []

    # ---- inventory ----
    def add_vehicle(self, vehicle: Vehicle) -> Vehicle:
        self.vehicles[vehicle.vehicle_id] = vehicle
        return vehicle

    def get_vehicle(self, vehicle_id: str) -> Vehicle:
        try:
            return self.vehicles[vehicle_id.upper()]
        except KeyError:
            raise NotFoundError(f"Vehicle '{vehicle_id}' nahi mili.")

    def remove_vehicle(self, vehicle_id: str) -> None:
        vehicle = self.get_vehicle(vehicle_id)
        if not vehicle.is_available:
            raise InvalidOperationError("Sold gaari delete nahi ho sakti.")
        del self.vehicles[vehicle.vehicle_id]

    def search_vehicles(self, keyword="", vehicle_type=None, max_price=None,
                        only_available=True) -> list[Vehicle]:
        keyword = keyword.lower()
        results = []
        for v in self.vehicles.values():
            if only_available and not v.is_available:
                continue
            if vehicle_type and v.vehicle_type.lower() != vehicle_type.lower():
                continue
            if max_price is not None and v.price > max_price:
                continue
            if keyword and keyword not in f"{v.make} {v.model} {v.color}".lower():
                continue
            results.append(v)
        return sorted(results, key=lambda x: x.price)

    # ---- people ----
    def add_customer(self, customer: Customer) -> Customer:
        self.customers[customer.person_id] = customer
        return customer

    def add_salesperson(self, sp: Salesperson) -> Salesperson:
        self.staff[sp.person_id] = sp
        return sp

    def get_customer(self, cid: str) -> Customer:
        try:
            return self.customers[cid.upper()]
        except KeyError:
            raise NotFoundError(f"Customer '{cid}' nahi mila.")

    def get_salesperson(self, eid: str) -> Salesperson:
        try:
            return self.staff[eid.upper()]
        except KeyError:
            raise NotFoundError(f"Salesperson '{eid}' nahi mila.")

    # ---- sales ----
    def sell_vehicle(self, vehicle_id, customer_id, salesperson_id,
                     discount=0.0, payment_method="Cash") -> Sale:
        vehicle = self.get_vehicle(vehicle_id)
        customer = self.get_customer(customer_id)
        sp = self.get_salesperson(salesperson_id)

        if not vehicle.is_available:
            raise InvalidOperationError("Ye gaari available nahi hai.")
        if discount < 0 or discount > vehicle.price:
            raise InvalidOperationError("Discount ghalat hai.")

        sale = Sale(vehicle.vehicle_id, vehicle.title(), customer.person_id,
                    customer.name, sp.person_id, sp.name, vehicle.price,
                    discount, payment_method)
        sale.commission = sp.earn(vehicle.price - discount)
        vehicle.mark_sold()
        customer.purchases.append(sale.sale_id)
        self.sales.append(sale)
        return sale

    # ---- reports ----
    def inventory_value(self) -> float:
        return sum(v.price for v in self.vehicles.values() if v.is_available)

    def total_revenue(self) -> float:
        return sum(s.total for s in self.sales)

    def top_salesperson(self):
        if not self.staff:
            return None
        return max(self.staff.values(), key=lambda s: s.total_commission)

    def report(self) -> str:
        available = sum(1 for v in self.vehicles.values() if v.is_available)
        sold = len(self.vehicles) - available
        top = self.top_salesperson()
        top_text = f"{top.name} (Rs {top.total_commission:,.0f} commission)" if top else "N/A"
        return (
            f"\n===== {self.name} - REPORT =====\n"
            f"Total vehicles     : {len(self.vehicles)}\n"
            f"Available          : {available}\n"
            f"Sold               : {sold}\n"
            f"Inventory value    : Rs {self.inventory_value():,.0f}\n"
            f"Total sales        : {len(self.sales)}\n"
            f"Total revenue      : Rs {self.total_revenue():,.0f}\n"
            f"Customers          : {len(self.customers)}\n"
            f"Staff              : {len(self.staff)}\n"
            f"Top salesperson    : {top_text}\n"
        )

    # ---- persistence ----
    def save(self, path: Path = DATA_FILE) -> None:
        data = {
            "name": self.name,
            "vehicles": [v.to_dict() for v in self.vehicles.values()],
            "customers": [c.to_dict() for c in self.customers.values()],
            "staff": [s.to_dict() for s in self.staff.values()],
            "sales": [s.to_dict() for s in self.sales],
        }
        path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    @classmethod
    def load(cls, path: Path = DATA_FILE, default_name="Ali Motors") -> "Dealership":
        if not path.exists():
            return cls(default_name)
        data = json.loads(path.read_text(encoding="utf-8"))
        d = cls(data["name"])
        for v in data["vehicles"]:
            register_id(v["vehicle_id"])
            d.add_vehicle(vehicle_from_dict(v))
        for c in data["customers"]:
            register_id(c["person_id"])
            d.add_customer(Customer(**c))
        for s in data["staff"]:
            register_id(s["person_id"])
            d.add_salesperson(Salesperson(**s))
        for s in data["sales"]:
            register_id(s["sale_id"])
            d.sales.append(Sale(**s))
        return d


# ----------------------------------------------------------------------
# Command Line Interface
# ----------------------------------------------------------------------
def ask(prompt, cast=str, default=None):
    while True:
        raw = input(prompt).strip()
        if not raw and default is not None:
            return default
        try:
            value = cast(raw)
            if cast is str and not value:
                raise ValueError
            return value
        except ValueError:
            print("  Ye zaroori hai / ghalat input hai, dobara likho." if cast is str else "  Sahi number likho.")


def show(items, empty="Kuch nahi mila."):
    items = list(items)
    if not items:
        print(empty)
    for item in items:
        print(item)


def add_vehicle_flow(shop: Dealership):
    kind = ask("Type (car/bike): ").lower()
    make = ask("Make (e.g. Toyota): ")
    model = ask("Model: ")
    year = ask("Year: ", int)
    price = ask("Price (Rs): ", float)
    color = ask("Color: ")
    mileage = ask("Mileage km (0): ", int, default=0)
    if kind == "car":
        doors = ask("Doors (4): ", int, default=4)
        trans = ask("Transmission (Manual/Auto): ", default="Manual")
        fuel = ask("Fuel (Petrol/Diesel/Hybrid): ", default="Petrol")
        v = Car(make, model, year, price, color, mileage,
                doors=doors, transmission=trans, fuel=fuel)
    elif kind == "bike":
        cc = ask("Engine cc (70): ", int, default=70)
        btype = ask("Bike type (Standard/Sports/Cruiser): ", default="Standard")
        v = Bike(make, model, year, price, color, mileage, engine_cc=cc, bike_type=btype)
    else:
        print("Sirf 'car' ya 'bike' likho.")
        return
    shop.add_vehicle(v)
    print(f"Vehicle add ho gayi: {v.vehicle_id}")


def sell_flow(shop: Dealership):
    cars = shop.search_vehicles()
    if not cars:
        print("Koi available gaari nahi. Pehle gaari add karo.")
        return
    if not shop.customers:
        print("Koi customer nahi. Pehle customer add karo (option 5).")
        return
    if not shop.staff:
        print("Koi salesperson nahi. Pehle salesperson add karo (option 7).")
        return
    print("\n--- Available vehicles ---")
    show(cars)
    vid = ask("Vehicle ID (e.g. V001): ")
    print("\n--- Customers ---")
    show(shop.customers.values())
    cid = ask("Customer ID (e.g. C001): ")
    print("\n--- Salespersons ---")
    show(shop.staff.values())
    eid = ask("Salesperson ID (e.g. E001): ")
    discount = ask("Discount Rs (0): ", float, default=0.0)
    pay = ask("Payment method (Cash/Bank/Installment): ", default="Cash")
    sale = shop.sell_vehicle(vid, cid, eid, discount, pay)
    print(sale.invoice())
    print(f"Salesperson commission: Rs {sale.commission:,.2f}")


def search_flow(shop: Dealership):
    kw = ask("Keyword (khali = sab): ", default="")
    vt = ask("Type car/bike (khali = sab): ", default="") or None
    mp = ask("Max price (khali = koi limit nahi): ", float, default=0.0) or None
    show(shop.search_vehicles(kw, vt, mp))


MENU = """
===== {name} =====
 1. Vehicle add karo
 2. Saari vehicles dekho (available + sold)
 3. Vehicle search karo
 4. Vehicle delete karo
 5. Customer add karo
 6. Customers dekho
 7. Salesperson add karo
 8. Salespersons dekho
 9. Gaari becho (Invoice)
10. Sales history
11. Report
 0. Save & Exit
"""


def main():
    first_run = not DATA_FILE.exists()
    shop = Dealership.load()
    if first_run:  # sirf pehli dafa demo data
        shop.add_salesperson(Salesperson("Ahmed Khan", "0300-1111111", commission_rate=0.02))
        shop.add_vehicle(Car("Toyota", "Corolla", 2022, 6_500_000, "White", 15000,
                             doors=4, transmission="Auto", fuel="Petrol"))
        shop.add_vehicle(Bike("Honda", "CD 70", 2024, 190_000, "Red", 0,
                              engine_cc=70, bike_type="Standard"))

    actions = {
        "1": lambda: add_vehicle_flow(shop),
        "2": lambda: show(shop.search_vehicles(only_available=False), "Inventory khali hai."),
        "3": lambda: search_flow(shop),
        "4": lambda: (show(shop.search_vehicles()), shop.remove_vehicle(ask("Vehicle ID: ")),
                      print("Delete ho gayi.")),
        "5": lambda: print("Added:", shop.add_customer(Customer(
            ask("Name: "), ask("Phone: "),
            ask("Email (optional): ", default=" ").strip(),
            ask("CNIC (optional): ", default=" ").strip())).person_id),
        "6": lambda: show(shop.customers.values(), "Koi customer nahi."),
        "7": lambda: print("Added:", shop.add_salesperson(Salesperson(
            ask("Name: "), ask("Phone: "),
            commission_rate=ask("Commission rate (0.02 = 2%): ", float, default=0.02)
        )).person_id),
        "8": lambda: show(shop.staff.values(), "Koi staff nahi."),
        "9": lambda: sell_flow(shop),
        "10": lambda: show((f"{s.sale_id} | {s.date} | {s.vehicle_title} -> "
                            f"{s.customer_name} | Rs {s.total:,.0f}" for s in shop.sales),
                           "Abhi koi sale nahi hui."),
        "11": lambda: print(shop.report()),
    }

    while True:
        print(MENU.format(name=shop.name))
        try:
            choice = input("Option chuno: ").strip()
        except (KeyboardInterrupt, EOFError):
            choice = "0"
        if choice == "0":
            shop.save()
            print("Data save ho gaya. Khuda hafiz!")
            break
        action = actions.get(choice)
        if not action:
            print("Ghalat option.")
            continue
        try:
            action()
            shop.save()  # har action ke baad auto-save
        except DealershipError as err:
            print(f"Error: {err}")
        except (KeyboardInterrupt, EOFError):
            print("\nCancel kar diya.")
        except Exception as err:  # unexpected - program band na ho
            print(f"Unexpected error: {err}")


if __name__ == "__main__":
    main()
# Order Management System

##  Description

This project is a console-based Order Management System developed in Python.
It allows users to manage clients, products, and orders, as well as generate reports and calculate daily income.

The system is designed using a **modular structure**, where each functionality is separated into different files for better organization and maintainability.

---

## Features

* Register clients
* Register products (using tuples)
* Create orders
* View registered orders
* Calculate total income
* Generate final reports

---

## System Structure

The project is divided into modules:

```
main.py
clientes.py
productos.py
pedidos.py
reportes.py
```

### Module Responsibilities

* **clientes.py**

  * Register clients
  * View orders

* **productos.py**

  * Register products using tuples

* **pedidos.py**

  * Create orders
  * Calculate total income

* **reportes.py**

  * Generate system reports

* **main.py**

  * Integrates all modules
  * Provides the user interface (menu)

---

## Data Structures Used

* **Dictionaries**

  * Used to store clients, products, and orders

* **Tuples**

  * Used to store product information (ID, name, price)

---

##  How to Run

1. Make sure you have Python installed.
2. Place all files in the same folder.
3. Open a terminal in that folder.
4. Run:

```
python main.py
```

---

##  Example Workflow

1. Register a client
2. Register a product
3. Create an order
4. View orders
5. Check total income
6. Generate report

---

##  Example Data

```
Client:
ID: 1
Name: John
Email: john@email.com

Product:
ID: P1
Name: Mouse
Price: 50

Order:
ID: O1
Client: John
Product: Mouse
Quantity: 2
Total: 100
```

---

##  Project Requirements Covered

* ✔ Use of functions with parameters
* ✔ Functions return values
* ✔ Use of dictionaries
* ✔ Use of tuples
* ✔ Modular programming
* ✔ Functional system

---

## Team Work

This project was developed collaboratively:

* Couder  1: Client management and order visualization
* Couder  2: Product management and report generation
* Couderr 3: Order creation and income calculation

---

## Notes

* The system does not use lists, as required.
* All data is stored in memory (no database).
* The interface is console-based.

---

## License

This project was carried out by Couder de Riwi.

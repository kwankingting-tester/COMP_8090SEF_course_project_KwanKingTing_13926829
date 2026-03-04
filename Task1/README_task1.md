# Task 1: Personal Finance Tracker

## Problem Description
A real-life personal finance management system that helps users record income and expenses, calculate balance, and store data persistently using JSON.

## OOP Concepts Demonstrated (All required concepts used)

- Abstraction: `Transaction` is an abstract base class with `@abstractmethod`
- Inheritance: `Income` and `Expense` classes inherit from `Transaction`
- Polymorphism: Both child classes override `get_type()` and `__str__()`
- Encapsulation: All attributes use `_` prefix (private)
- Composition: `FinanceManager` contains multiple `Account` objects


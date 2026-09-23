# Odoo Estate Workshop

A Real Estate management module developed as part of an official Odoo workshop.

The project demonstrates core Odoo development concepts including models, fields, ORM relationships, constraints, computed fields, business logic, XML views, menus, access rights, and module dependencies.

## Modules

### `estate`

The main Real Estate module.

It provides:

* Property management
* Property types
* Property tags
* Property offers
* Salesperson assignment
* Property status workflow
* Computed total area
* Computed best offer
* Sales information
* Chatter integration
* List, Form, and Kanban views
* Business and SQL constraints

### `estate_accounts`

An additional module that extends the Real Estate functionality toward Odoo Accounting.

It contains logic intended to create a customer invoice when a property is sold, including:

* Property price
* 6% commission
* Administrative fees

> Note: The accounting extension is part of the workshop project and may require further adjustments before being used in a production environment.

## Main Models

### `estate.property`

Represents a real estate property.

Includes information such as:

* Name
* Description
* Availability date
* Expected price
* Selling price
* Bedrooms
* Living area
* Garden information
* Property type
* Property tags
* Salesperson
* Customer
* Offers
* Property state

Property states include:

`New` → `Offer Received` → `Offer Accepted` → `Sold`

Properties can also be cancelled.

### `estate.property.offer`

Represents an offer made for a property.

Offers can be:

* Accepted
* Refused

Accepting an offer updates the property's selling price, customer, and state.

### `estate.property.type`

Used to organize properties by type.

### `estate.property.tag`

Used to categorize properties with colored tags.

## Business Rules

The project includes several validation rules, including:

* Property names must be unique.
* Property type names must be unique.
* Property tag names must be unique.
* Expected price must be greater than zero.
* Selling price cannot be negative.
* Selling price cannot be lower than 90% of the expected price, except when it is zero.
* A cancelled property cannot be sold.
* A sold property cannot be cancelled.
* A property cannot have more than one accepted offer.

## Odoo Concepts Demonstrated

This project was built to practice:

* Odoo ORM
* Models and fields
* `Many2one`, `One2many`, and `Many2many` relationships
* Computed fields
* `@api.depends`
* Constraints and validation
* Business methods
* Model inheritance
* XML views
* Form, List, and Kanban views
* Menus and actions
* Access control lists
* Chatter
* Module dependencies
* Integration with Odoo Accounting

## Project Structure

```text
Odoo-Estate-Workshop/
│
├── estate/
│   ├── models/
│   ├── views/
│   ├── security/
│   ├── __init__.py
│   └── __manifest__.py
│
├── estate_accounts/
│   ├── models/
│   ├── views/
│   ├── security/
│   ├── __init__.py
│   └── __manifest__.py
│
├── .gitignore
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/MahmoudAlQataa/Odoo-Estate-Workshop.git
```

2. Copy the `estate` and `estate_accounts` directories into an Odoo custom addons directory.

3. Make sure the custom addons directory is included in your Odoo `addons_path`.

4. Restart Odoo.

5. Enable developer mode and update the Apps list.

6. Install the **Real Estate** module.

The `estate_accounts` module depends on both `account` and `estate`.

## Technologies

* Python
* XML
* Odoo
* Odoo ORM
* PostgreSQL

## Status

Workshop project / learning project.

The project was developed to practice Odoo module development and explore the implementation of a real estate management system.

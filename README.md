# FastAPI E-Commerce Assignmnet

## Introduction
This repository contains the implementation of an E-Commerce API using FastAPI, along with additional features and endpoints as part of an assignment.

## Features Implemented
1. **Unique Username Dependency**: Implemented a dependency to ensure that usernames are unique when creating a customer.
2. **Edit Customers Endpoint**: An endpoint that edit customer information.
3. **Edit Product Information Endpoint**: An endpoint that edit product information.
4. **Status Attribute for Orders**: A status attribute to the Order entity with a default value of "pending".
5. **Checkout Order Endpoint**: Implemented an endpoint to change the status of an order from "pending" to "completed".

## File Structure
The project is structured as follows:
- `main.py`: Contains the main FastAPI application setup and routing.
- `middleware.py`: Middleware for logging and error handling.
- `routers/`: Folder containing router modules for different entities.
  - `customer.py`: Router module for customer-related endpoints.
  - `product.py`: Router module for product-related endpoints.
  - `order.py`: Router module for order-related endpoints.
- `schema/`: Folder containing Pydantic models for data validation.
  - `customer.py`: Pydantic models for customers.
  - `product.py`: Pydantic models for products.
  - `order.py`: Pydantic models for orders.
- `services/`: Folder containing service modules for business logic.
  - `order.py`: Service module for order-related logic.
- `logger.py`: Logging configuration module.
- `app.log`: Log file for application logs.
- `illustration.py`: Placeholder file for illustration purposes.

## Setup Instructions
1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Run the FastAPI application using `uvicorn main:app --reload`.

## Usage
- Use the provided endpoints to interact with the E-Commerce API:
  - `/customers`: CRUD operations for customers.
  - `/products`: CRUD operations for products.
  - `/orders`: CRUD operations for orders.
  - `/orders/checkout/{order_id}`: Checkout an order.

from fastapi import APIRouter, Depends, HTTPException
from schema.order import Order, OrderCreate, orders
from services.order import order_service

order_router = APIRouter()

# list all order
# create an order 

@order_router.get('/', status_code=200)
def list_orders():
    response = order_service.order_parser(orders)
    return {'message': 'success', 'data': response}

@order_router.post('/', status_code=201)
def create_order(payload: OrderCreate = Depends(order_service.check_availability)):
    customer_id: int = payload.customer_id
    product_ids: list[int] = payload.items
    # get curr order id
    order_id = len(orders) + 1
    new_order = Order(
        id=order_id,
        customer_id=customer_id,
        items=product_ids,
    )
    orders.append(new_order)
    return {'message': 'Order created successfully', 'data': new_order}

@order_router.put('/checkout/{order_id}', status_code=200)
def checkout_order(order_id: int):
    for order in orders:
        if order.id == order_id:
            if order.status == "completed":
                raise HTTPException(status_code=400, detail="Order has already been checked out")
            order.status = "completed"
            return {'message': 'Order checked out successfully', 'data': order}
    raise HTTPException(status_code=404, detail="Order not found")
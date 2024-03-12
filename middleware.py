import time
from fastapi import Request, HTTPException
from logger import logger
from schema.customer import customers
from schema.customer import CustomerCreate

async def ecommerce_middleware(request: Request, callnext):
    logger.info("Starting ................")
    start_time = time.time()
    try:
        response = await callnext(request)
        process_time = time.time() - start_time
        response.headers["X-Process-Time"] = str(process_time)
        logger.info(f"ended. process_time: {process_time}")
    except Exception as e:
        logger.error("An error occurred while processing")
    return response

async def check_unique_username(payload: CustomerCreate):
    username = payload.username
    for customer in customers:
        if customer.username == username:
            raise HTTPException(status_code=400, detail="Username already exists")
    return payload
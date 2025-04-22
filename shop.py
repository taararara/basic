import decimal, logging
from pywebio.input import slider, FLOAT, NUMBER
from pywebio.input import input as pw_input
from pywebio.output import put_html, put_success

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("shop.log"), logging.StreamHandler()],
)


# HEAD
put_html("<h1>Ласкаво просимо до нашого магазину</h1>")


# PRICE
APPLE_PRICE = decimal.Decimal(52.75)
BANANA_PRICE = decimal.Decimal(81.40)

# LOG
logging.info("info")

# WEIGHT
apple_weight = slider(
    "Яблучка", type=FLOAT, min_value=0, max_value=5, value=0.01, required=True
)
apple_weight = decimal.Decimal(apple_weight).quantize(
    decimal.Decimal("0.000"), rounding=decimal.ROUND_HALF_UP
)
logging.info(f"The consumer bought {apple_weight} kilograms of apples")


banana_weight = pw_input(
    "Бананчики", type=NUMBER, min=1, max=10, value=5, required=True
)
banana_weight = decimal.Decimal(banana_weight).quantize(
    decimal.Decimal("0.000"), rounding=decimal.ROUND_HALF_UP
)
logging.info(f"The consumer bought {banana_weight} kilograms of bananas")


# COST
apple_cost = (APPLE_PRICE * apple_weight).quantize(
    decimal.Decimal("0.00"), rounding=decimal.ROUND_HALF_UP
)
banana_cost = (BANANA_PRICE * banana_weight).quantize(
    decimal.Decimal("0.00"), rounding=decimal.ROUND_HALF_UP
)
total_cost = apple_cost + banana_cost


put_success(
    f"За {apple_weight} Кг яблучок, Вартість буде: {apple_cost}",
    f"За {banana_weight} Кг бананчиків, Вартість буде: {banana_cost}",
    f"Ціла вартість за фрукти: {total_cost}",
)
pass

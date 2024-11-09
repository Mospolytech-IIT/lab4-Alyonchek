from store_operations import check_stock, calculate_shipping, cancel_order, OutOfStockException, UnauthorizedActionException

# Функция для демонстрации проверки остатков (Шаг 8)
def demo_check_stock():
    try:
        check_stock("apple", 10)
    except OutOfStockException as e:
        print(f"Ошибка проверки остатков: {e}")

# Функция для демонстрации расчета доставки (Шаг 8)
def demo_shipping():
    try:
        calculate_shipping(1500)
    except ValueError as e:
        print(f"Ошибка расчета доставки: {e}")

# Функция для демонстрации отмены заказа (Шаг 8)
def demo_cancel_order():
    try:
        cancel_order("12345", "user")
    except UnauthorizedActionException as e:
        print(f"Ошибка отмены заказа: {e}")

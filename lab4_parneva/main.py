from store_operations import (
    check_stock,
    calculate_shipping,
    apply_discount,
    create_order,
    check_delivery_zone,
    pay_order,
    cancel_order,
)
from demo_functions import demo_check_stock, demo_shipping, demo_cancel_order

def run_all_operations():
    """Запускает все функции для демонстрации их работы и обработки исключений (Шаг 9)."""
    try:
        check_stock("banana", 2)
        calculate_shipping(500)
        apply_discount(100, 20)
        create_order("apple", 3, "customer")
        check_delivery_zone("12345")
        pay_order(200, 250)
        cancel_order("12345", "admin")
        demo_check_stock()
        demo_shipping()
        demo_cancel_order()
        
    except Exception as e:
        print(f"Необработанное исключение: {e}")

if __name__ == "__main__":
    run_all_operations()

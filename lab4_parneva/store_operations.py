# Пользовательские исключения (Шаг 6)
class OutOfStockException(Exception):
    """Возникает, если товара нет на складе или его недостаточно"""
    pass

class InvalidDiscountException(Exception):
    """Возникает, если применена некорректная скидка"""
    pass

class UnauthorizedActionException(Exception):
    """Возникает, если неавторизованный пользователь пытается выполнить действие"""
    pass

# Функция для проверки наличия товара на складе (Шаг 1)
def check_stock(item, quantity):
    """
    Проверяет наличие товара на складе.
    Возникает исключение, если товара нет или его недостаточно.
    """
    stock = {"apple": 5, "banana": 3}
    if item not in stock or stock[item] < quantity:
        raise OutOfStockException(f"{item} отсутствует или недостаточное количество на складе.")
    print(f"{quantity} {item} доступно на складе.")

# Функция для расчета стоимости доставки (Шаг 1)
def calculate_shipping(distance):
    """
    Вычисляет стоимость доставки.
    Возникает исключение, если расстояние превышает допустимое.
    """
    if distance > 1000:
        raise ValueError("Мы не доставляем заказы на расстояние более 1000 км.")
    cost = distance * 0.5
    print(f"Стоимость доставки: {cost}")

# Функция для применения скидки (Шаг 2)
def apply_discount(price, discount):
    """
    Применяет скидку.
    Возникает исключение, если скидка некорректная.
    """
    try:
        if discount < 0 or discount > 50:
            raise InvalidDiscountException("Скидка должна быть в пределах от 0% до 50%.")
        discounted_price = price * (1 - discount / 100)
        print(f"Цена со скидкой: {discounted_price}")
    except Exception as e:
        print(f"Ошибка при применении скидки: {e}")

# Функция для создания заказа (Шаг 3)
def create_order(item, quantity, user_role):
    """
    Создаёт заказ.
    Возникает исключение, если пользователь не авторизован для создания заказа.
    """
    try:
        if user_role != "customer":
            raise UnauthorizedActionException("Только клиенты могут создавать заказы.")
        print(f"Заказ на {quantity} {item} был создан.")
    except Exception as e:
        print(f"Ошибка создания заказа: {e}")
    finally:
        print("Процесс создания заказа завершен.")

# Функция для проверки зоны доставки (Шаг 4)
def check_delivery_zone(postal_code):
    """
    Проверяет, доступна ли доставка по указанному почтовому коду.
    Возникают различные исключения при некорректном формате кода.
    """
    try:
        if not isinstance(postal_code, str):
            raise TypeError("Почтовый код должен быть строкой.")
        if len(postal_code) != 5:
            raise ValueError("Почтовый код должен содержать ровно 5 символов.")
        if postal_code.startswith("9"):
            raise OutOfStockException("Доставка недоступна в указанную зону.")
        print("Доставка доступна в вашу зону.")
    except TypeError as te:
        print(f"Ошибка типа: {te}")
    except ValueError as ve:
        print(f"Ошибка значения: {ve}")
    except OutOfStockException as ose:
        print(f"Исключение доставки: {ose}")
    finally:
        print("Проверка зоны доставки завершена.")

# Функция для оплаты заказа (Шаг 5)
def pay_order(order_total, balance):
    """
    Обрабатывает оплату заказа.
    Возникают исключения при недостаточном балансе или некорректной сумме.
    """
    try:
        if order_total <= 0:
            raise ValueError("Сумма заказа должна быть положительной.")
        if balance < order_total:
            raise OutOfStockException("Недостаточно средств для оплаты заказа.")
        new_balance = balance - order_total
        print(f"Оплата прошла успешно. Оставшийся баланс: {new_balance}")
    except ValueError as ve:
        print(f"Ошибка оплаты: {ve}")
    except OutOfStockException as obe:
        print(f"Ошибка баланса: {obe}")
    finally:
        print("Процесс оплаты завершен.")

# Функция для отмены заказа (Шаг 7)
def cancel_order(order_id, user_role):
    """
    Отменяет заказ.
    Возникает исключение, если пользователь не имеет прав на отмену заказа.
    """
    try:
        if user_role != "admin":
            raise UnauthorizedActionException("Только администраторы могут отменять заказы.")
        print(f"Заказ {order_id} был отменен.")
    except UnauthorizedActionException as uae:
        print(f"Исключение отмены заказа: {uae}")
    finally:
        print("Процесс отмены заказа завершен.")

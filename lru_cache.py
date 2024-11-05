import time
# Функция для проверки почты
from functools import lru_cache
@lru_cache
def is_valid_email(email):
    # Фиктивно замедляем функцию
    time.sleep(2)

    if email.count("@") != 1:
        return False
    local_part, domain_part = email.split("@")
    if not local_part or not domain_part:
        return False
    if domain_part.count(".") != 1:
        return False

    return True

start_time = time.time()
test_email = "example@example.com"
test_size = 10
for _ in range(test_size):
   result = is_valid_email(test_email)
   # И дальше пошли бы необходимые операции
   ...
print('Total time: {}'.format(time.time()- start_time))
# Total time: 20.071501970291138
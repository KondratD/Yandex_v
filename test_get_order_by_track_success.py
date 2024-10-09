# Дмитрий Кондрат, 22А-я когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request

def test_response_200():
    order_response = sender_stand_request.get_info_order()
    assert order_response.status_code == 200

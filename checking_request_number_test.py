# Дмитрий Кондрат, 22А-я когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request


def test_get_order_by_track_success():
    response = post_new_order(data.order_body)
    track_number = str(response.json()["track"])
    order_info_response = get_info_order(track_number)
    assert order_info_response.status_code == 200
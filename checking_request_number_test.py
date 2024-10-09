import data
import sender_stand_request

def test_get_order_by_track_success():
    # Создаем новый заказ и получаем трек-номер
    response = sender_stand_request.post_new_order(data.order_body)
    track_number = str(response.json()["track"])

    # Получаем информацию о заказе по трек-номеру
    order_response = sender_stand_request.get_info_order(track_number)

    # Проверяем код ответа
    assert order_response.status_code == 200

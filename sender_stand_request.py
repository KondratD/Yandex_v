# Дмитрий Кондрат, 22А-я когорта — Финальный проект. Инженер по тестированию плюс

import configuration
import requests
import data

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body,
                         headers=data.headers)

def get_info_order(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.INFO_ORDER + track_number)
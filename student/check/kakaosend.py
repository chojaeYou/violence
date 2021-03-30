import sys
import os
import json
import requests
from . import auth
from . import config


from_number = '01036431761'
pfid = 'KA01PF200214032038938mhZXTqnPTDi'
templateId = 'KA01TP210329181401917KRU0ER0gKGz'


def send_kakao(text, phone):
    data = {
        'message': {
            'to': phone,
            'from': from_number,
            'text': text,
            'kakaoOptions': {
                'pfId': pfid,       # PFID 입력
                'templateId': templateId  # 템플릿아이디 입력
            }
        }
    }
    res = requests.post(config.getUrl('/messages/v4/send'),
                        headers=auth.get_headers(config.apiKey, config.apiSecret), json=data)
    print(json.dumps(json.loads(res.text), indent=2, ensure_ascii=False))


# 알림톡 단건 발송

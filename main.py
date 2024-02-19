import deepl
auth_key = "878b24ac-401e-6800-d77c-29a8cae4aac7:fx"

def translation(msg: str, auth_key: str, src: str, trg: str):
    """
    :param msg: input sentence for translation
    :param auth_key: personal authentication_key
    :param src: source_language
    :param trg: target_laguage
    :return: translated sentence
    """

    translator = deepl.Translator(auth_key=auth_key)

    # 결과
    """
        - target_lang
            1. EN-US : American
            2. KO : Korean
            3. JA - Japanese
            4. EN-GB : British
            5. FI - Finnish
        - source_lang
            1. EN : English
            2. KO : Korean
            3. JA - Japanese
            4. FI - Finnish
    """

    res = translator.translate_text(msg, source_lang=src, target_lang=trg)

    return res

def Table2Stirng(table: list, auth_key: str, src: str, trg: str):
    """

    :param table: 2-dim table data
    :return: transformed string data
    """

    transformed_sentence = ''

    for row in table:
        for cell in row:
            transformed_sentence += f'|{cell}'
        transformed_sentence += '|,\n'

    res = translation(msg=transformed_sentence[:-2], auth_key=auth_key, src=src, trg=trg)

    return res + '|'

def SelectFunction(msg: str, auth_key: str, src: str, trg: str):
    data_type = type(msg)

    if data_type == 'str':
        result = translation(msg=msg2, auth_key=auth_key, src=src, trg=trg)
        print(result)

    elif data_type == type([[]]):
        result = Table2Stirng(table=msg2, auth_key=auth_key, src=src, trg=trg)
        print(result)


msg = '위의 표를 보고 답을 구하세요. 키가 150cm를 넘는 사람의 나이 평균과 몸무게가 20kg 이하인 사람의 키 평균을 곱해서 답을 구하세요.'
msg2 = [['이름', '나이', '성별', '키', '몸무게', '특이사항'],
        ['김길동', '12', '남', '157cm', '58kg', '키가 190cm 이상이고 몸무게가 100kg 이상인 사람을 보면 겁에 질림'],
        ['박주먹', '44', '남', '10cm', '45kg', '없음'],
        ['이미나', '45', '여', '188cm', '77kg', '키가 150cm를 넘는 사람의 나이 평균과 몸무게가 20kg 이하인 사람의 키 평균을 곱하는 것을 좋아함'],
        ['현지', '78', '여', '190cm', '100kg', '손가락 길이가 15피트 미만이거나 50피트 이상인 사람을 보면 겁에 질림'],
        ]

SelectFunction(msg2, auth_key=auth_key, src='KO', trg='EN-US')
# result = translation(msg=msg2, auth_key=auth_key, src='KO', trg='EN-US')
# print(result)
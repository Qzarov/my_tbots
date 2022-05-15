import random

def get_rand_stic_id(pack):
    stic_id = pack[random.randint(0, len(pack)-1)]
    return stic_id

bot_info = \
    "DeScienz - децентрализованная система, которая будет состоять "\
    "из следующих компонентов:"\
    "\n- Социальная сеть;"\
    "\n- Децентрализованные автономные организации, аналог журналов, "\
    "которые будут создаваться пользователями"\
    "\n- База данных, хранящая научные знания"\
    "\n\nПроект призван дать свободу выражения и открыть возможности "\
    "монетизации научных знаний. Благодаря использованию блокчейн-технологий "\
    "становится возможным создание ДАО - научных сообществ, "\
    "где решение о важности того или иного труда принимается на основе "\
    "консенсуса участников сообщества - демократии в исконном ее понимании"

uchoniy_pic = [
    'resourсes/super-puper-uchoniy.jpg',
    'resourсes/uchoniy.jpg'
]

hi_stics = [
    "CAACAgIAAxkBAAEEvNFigYCp-lZ9YempUhrDIWI_e3oYDAACAQIAAsVnCAABoMsdsO1D9DQkBA"
    "CAACAgIAAxkBAAEEvNFigYCp-lZ9YempUhrDIWI_e3oYDAACAQIAAsVnCAABoMsdsO1D9DQkBA"
    "CAACAgIAAxkBAAEEvJtigXqpKk5ZwkEpijPXQWYg9O0ySgACaRUAAsEEoEt6ScKc2Q3atSQE",
    "CAACAgUAAxkBAAEEvJxigXqpZxbPAirghxj_Px5p047dsgACbwMAAukKyAOvzr7ZArpddCQE",
    "CAACAgIAAxkBAAEEvJ1igXqpmVotJSJvp57gT-S8XQk1hQACTgADIkwPDDTObKcClUH-JAQ",
    "CAACAgIAAxkBAAEEvJ5igXqp4RLsO6U8sUI-ha_zk6TX1AACawMAAm2wQgMBxrMf3Ej7GiQE",
    "CAACAgIAAxkBAAEEvJ9igXqpJnErX6ehGQfisma92JSrVQAC5w0AAkwAAalLKPSbhF1cTYkkBA",
    "CAACAgIAAxkBAAEEvKBigXqpFVFjgCVlX-9tJ0xNdlgJ3AACqAADV08VCDZy7wsH5feJJAQ",
    "CAACAgQAAxkBAAEEvKFigXqpEOXNagAB2hnPZOr2IRl8weMAAnYAAy_f-Al28b_cVkJiOCQE",
    "CAACAgIAAxkBAAEEvKJigXqpy_R-9EubxrOo8LKS904FzAAClwYAAvoLtgiTap3uNdUieCQE",
    "CAACAgIAAxkBAAEEvKNigXqpSw8-o4HOijQJrcRGKSbk8QACTwQAAs7Y6AvzJpv-wQRWsyQE"
]

thinking_stics = [
    "CAACAgUAAxkBAAEEvNNigYFrfmzxELlZpUjhaqxlhgnaiwACYgIAAnCZOFecbpQSD3AavSQE",
    "CAACAgUAAxkBAAEEvNRigYFrloiTAAHbVw93KnmRktr95RUAAn4DAALpCsgDMrYcdMEwyQwkBA",
    "CAACAgUAAxkBAAEEvNVigYFrkT8QcUZrPznGfrtvxynWUQACeAIAAtmbOVeM1KnfzZwDPCQE",
    "CAACAgQAAxkBAAEEvNZigYFrlSeD7Pbk_6_f7T3KkKuvFwACVwADL9_4CaN5x2wZAAFVcCQE",
    "CAACAgIAAxkBAAEEvNdigYFrjcIlY3K5xAqekdKvbTlHQwACOwMAAm2wQgMDgo__5XFPdSQE",
    "CAACAgIAAxkBAAEEvNhigYFrTlmF8XBBJxJl3JoCZ3uzegACfQoAAi8P8AaLySJME1359iQE",
    "CAACAgUAAxkBAAEEvN9igYMWKZ3CF0r_q3PIJObEjq9XvQACwwEAAiE_QVcVN518cA-OyCQE",
    "CAACAgUAAxkBAAEEvOBigYMWif7qDZoa0wABUzgxs3mrlvUAAn0DAALpCsgDrQPSy3Fi_aYkBA",
    "CAACAgUAAxkBAAEEvOFigYMWy-2YPItmoKPqVdKIqnN6wAACFgIAAr5oOFfAu1-WAprbCCQE",
    "CAACAgUAAxkBAAEEvOJigYMWk0bHF23cglbQFYg1nDckRAAC5gMAAhR_OVd_59aWLM1_hiQE"
]

keep_it_up_stics = [
    "CAACAgIAAxkBAAEEvQhigYTchnr7xSmTsfrHICxZdufbRQACagADwZxgDCHf0XJEvU3QJAQ",
    "CAACAgUAAxkBAAEEvQligYTcfY8ntsqYYfVi4muBw2h0OwACdQMAAukKyAPh87nO7IZtBCQE",
    "CAACAgUAAxkBAAEEvQpigYTcTLJK-OPXL_4fpxclPvEcywACKgIAAgkjQFdzi9QXxelBOCQE",
    "CAACAgUAAxkBAAEEvQtigYTctwrDVQ_w0_pEEkx36qf40QACuwMAAukKyAPtaUDZ4qsT3yQE",
    "CAACAgUAAxkBAAEEvQxigYTc7d8ISyqta3DXBaPh1TYdZAACcAMAAukKyAPWBlQ0Pz2tpCQE",
    "CAACAgUAAxkBAAEEvQ1igYTcT4AxAif4H72lM1zMynQ0NwACeQMAAukKyAOR2oP4lfTVoCQE",
    "CAACAgIAAxkBAAEEvQ5igYTc19Wprrp19sddk3wkGQEmJwACEAADIkwPDALjWI3RSF7gJAQ",
    "CAACAgUAAxkBAAEEvQ9igYTc2XS3au_NqotokQ4JymW49gAC7gEAAsTaQFeuaU0NcCiT7SQE",
    "CAACAgIAAxkBAAEEvRBigYTcIiHKrAnC0hEj7nBI5KyjuwAC7BUAAsymwUuIP6qzCm_qWSQE"
]

love_it_stics = [
    "CAACAgIAAxkBAAEEvVZigYaqspLumeLrpYLuBTUmKAyqdwACSwMAArVx2gZu3ktViH-zcCQE",
    "CAACAgIAAxkBAAEEvVdigYaq_4ROTBy6xAdLtl4gX6oiVwACMAADIPJCGiRTN4DQ01MrJAQ",
    "CAACAgIAAxkBAAEEvVhigYaqd68-GimKBv6DZTtnSrbEygACGQADwDZPE9BDgPYgVxRLJAQ",
    "CAACAgIAAxkBAAEEvVligYaql3NnKmufHAPGKDXJFjUsvAACdwQAAs7Y6AtHPqfiR1RcRCQE",
    "CAACAgIAAxkBAAEEvVpigYaqdqlW5UhefqwWiQABKRgGSBkAAjUAA61lvBT1pXFcxTDl4CQE",
    "CAACAgIAAxkBAAEEvVtigYaqmtJX142J0ehFpgVdez1F7wACngADO2AkFNykvYmpOKxXJAQ"
]

congrats_stics = [
    "CAACAgIAAxkBAAEEvZtigYnDS2atkYwXsJpPjxN66klqTQACWBQAAjBE-EjwNbvNCZ7aECQE",
    "CAACAgIAAxkBAAEEvZ1igYnD-YbNeVnezMwRFI4J9x3l9gAC0gEAAsVnCAABgpzLsIjCkgckBA",
    "CAACAgUAAxkBAAEEvZ5igYnDRcxK_iDI6OYbC_NwYzgpGQACbgMAAukKyAN8NA8_2uwEbSQE",
    "CAACAgUAAxkBAAEEvaBigYnDZfY7TDpBM3ZkuRp8zI0qlwACpgMAAukKyAN5s5AIa4Wx9CQE",
    "CAACAgIAAxkBAAEEvZxigYnDYkPtZRnbyGbuzU7Uod6iywACCwMAAm2wQgN_tBzazKZEJSQE",
    "CAACAgUAAxkBAAEEvZ9igYnDIIMAAfpIlshncLmuuxQaCLwAAtIBAAIBwkFXf1W_lDTdkz4kBA",
    "CAACAgIAAxkBAAEEvaFigYnD-6VOodoF8GOyOBzR52Ci4gACfQMAAm2wQgO9Ey75tk26UyQE",
    "CAACAgEAAxkBAAEEvaJigYnDXWhKPwzBu71Ia372Yykt4gACTAIAAtg_5wkagP3RTbpZniQE",
    "CAACAgEAAxkBAAEEvaNigYnDYTQpvO1rLwGO2BsEifrxSQACSggAAtg_5wmyz2_igsF_CSQE",
    "CAACAgIAAxkBAAEEvaRigYnDwontuv_9A_dYugsya9mCggACWAQAAs7Y6Ats9xlkvLIcBiQE",
    "CAACAgIAAxkBAAEEvaVigYnDrckuuCuohdYjaBTKC9tAKgACrwkAAnlc4gnWRLT5upgg-iQE",
    "CAACAgIAAxkBAAEEvZpigYnDNzC_JzHrqlxHTJYyNzr6OgACHw4AAupQ-Ehu3Fz52zoO2yQE",
    "CAACAgIAAxkBAAEEvZligYnDPCuFAVL_dsbEr5ywKY1NzwACog8AAiFQ-Ehdi-Xqd2-fhCQE",
    "CAACAgIAAxkBAAEEvZhigYnDbLPLMldVvwdBgEp8sCB06AACZwADvN1PET-vmFpxXizRJAQ",
    "CAACAgIAAxkBAAEEvZdigYnDww3xA6iHGrDg-JZyz1HUHAAC5gEAAsVnCAABesLXl7Vjc88kBA",
    "CAACAgIAAxkBAAEEvZZigYnDZcphnL40ZCP1bAlykSkHkAACVwADwZxgDMYC_bNUm6Y0JAQ"
]

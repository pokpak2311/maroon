def comeXpayY(come_x, pay_y, per_head, pax):
    """
    มา x จ่าย y เช่น มา 4 จ่าย 3
    :param come_x: มา
    :param pay_y: จ่าย
    :param per_head: ค่าอาหารต่อหัว
    :param pax: จำนวนลูกค้าในโต๊ะ
    :return: ค่าอาหาร
    """
    return (pax // come_x) * (pay_y * per_head) + (pax % come_x) * per_head

if __name__ == '__main__':
    print(comeXpayY(4, 3, 100, 5))


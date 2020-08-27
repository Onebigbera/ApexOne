# -*-coding:utf-8 -*-
"""
    Index test data
"""
# 可以分的更细致
"""
    1.航班不存在
    2.航班信息存在，不存在物流信息
    3.航班信息存在，物流信息存在
"""
indexPage_data = [
    {'hawb': 'dasd23213124543', 'tip': 'This shipment doesn’t exist'},
    {'hawb': 'LAXTS01695', 'tip': 'No logistics information for this shipment yet'}
]
shipment_not_exist = [
    {'hawb': 'dasd23213124543', 'tip': 'This shipment doesn’t exist'},
    {'hawb': 'dasd23213124544', 'tip': 'This shipment doesn’t exist'},
    {'hawb': 'dasd23213124545', 'tip': 'This shipment doesn’t exist'},
    {'hawb': 'dasd23213124546', 'tip': 'This shipment doesn’t exist'},
    {'hawb': 'dasd23213124547', 'tip': 'This shipment doesn’t exist'}
]

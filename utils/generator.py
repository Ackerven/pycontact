# @Author: Ackerven
# @Mail: ackerven@cxmail.org
# @Time: 14/11/2021 17:40
# @File: generator.py
# OS: Ubuntu 20.04 LTS
# SoftWare: PyCharm
# @Copyright Copyright(C) 2021 Ackerven All rights reserved.

from faker import Faker
from model.contact import Contact
import random

fake = Faker(locale='zh_CN')


def contact_generator(number):
    contact_list = []
    for i in range(number):
        contact_list.append(Contact(fake.name(),
                                    'Male' if random.randint(0, 1) > 0 else 'Female',
                                    fake.phone_number(),
                                    fake.first_romanized_name())
                            )
    return contact_list[:]

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 13:55:17 2024

@author: mike
"""
import io
from booklet import Booklet
from tempfile import NamedTemporaryFile
import concurrent.futures

##############################################
### Parameters



##############################################
### Functions


def set_item(f, key, value):
    f[key] = value

    return key


##############################################
### Tests

tf = NamedTemporaryFile()
file_path = tf.name

data_dict = {key: list(range(key)) for key in range(2, 20)}

def test_threading():
    with Booklet(file_path, 'n', key_serializer='uint1', value_serializer='msgpack') as f:
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            futures = []
            for key, value in data_dict.items():
                future = executor.submit(set_item, f, key, value)
                futures.append(future)
    
        results = concurrent.futures.wait(futures)

    f = Booklet(file_path)

    assert f[10] == list(range(10))


# f = Booklet(file_path)
# f2 = Booklet(file_path, 'w')



















































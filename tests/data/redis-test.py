#!/usr/bin/env python
# encoding: utf-8

import redis

redis = redis.Redis(host='localhost', port='6379')
redis.set('mike', 'mikei')
assert redis.get('mike') == 'mike'

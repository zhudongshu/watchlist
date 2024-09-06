# -*- coding:utf-8 -*-

"""
# Time: 2024/9/6 09:53
# Author: Zhu, Dongshu
# File: wsgi.py
# Version: python 3.9.13
# Description: 
"""
import os
from dotenv import load_dotenv


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

from watchlist import app

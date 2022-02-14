# -*- coding: utf-8 -*-
"""This module contains a template MindMeld application"""
from mindmeld import Application
from secret_santa.root import app
from secret_santa.handlers import general, santa, work, personal, play, carol

__all__ = ['app']
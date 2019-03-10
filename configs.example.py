#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
Life's pathetic, have fun ("▔□▔)/hi~♡ Nasy.

Excited without bugs::

    |             *         *
    |                  .                .
    |           .
    |     *                      ,
    |                   .
    |
    |                               *
    |          |\___/|
    |          )    -(             .              ·
    |         =\ -   /=
    |           )===(       *
    |          /   - \
    |          |-    |
    |         /   -   \     0.|.0
    |  NASY___\__( (__/_____(\=/)__+1s____________
    |  ______|____) )______|______|______|______|_
    |  ___|______( (____|______|______|______|____
    |  ______|____\_|______|______|______|______|_
    |  ___|______|______|______|______|______|____
    |  ______|______|______|______|______|______|_
    |  ___|______|______|______|______|______|____

author   : Nasy https://nasy.moe
date     : Mar 10, 2019
email    : Nasy <nasyxx+python@gmail.com>
filename : config.py
project  : douban_reviews
license  : GPL-3.0+

There are more things in heaven and earth, Horatio, than are dreamt.
 --  From "Hamlet"
"""
id_ = "26235354"
headers = {
    "cookie": "",  # change it
    "referer": "https://movie.douban.com/subject/3016187/reviews",
    "connection": "keep-alive",
    "x-requested-with": "XMLHttpRequest",
    "cache-control": "no-cache",
    "accept": "application/json, text/javascript, */*; q=0.01",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36",
    "accept-language": "en,zh-CN;q=0.9,zh;q=0.8",
    "accept-encoding": "gzip, deflate, br",
    "dnt": "1",
    "pragma": "no-cache",
}

idheaders = {
    "cookie": "",  # change it
    "accept-language": "en,zh-CN;q=0.9,zh;q=0.8",
    "accept-encoding": "gzip, deflate, br",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,"
    "image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "dnt": "1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36",
    "upgrade-insecure-requests": "1",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "connection": "keep-alive",
}

__all__ = ["headers", "id_", "idheaders"]

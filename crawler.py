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
filename : crawler.py
project  : douban_reviews
license  : LGPL-3.0+

There are more things in heaven and earth, Horatio, than are dreamt.
 --  From "Hamlet"
"""
# Standard Library
import re
from typing import Dict, List, Iterable, NamedTuple

# Prelude
from nalude import flatten

# Web Packages
from requests_html import HTML

# Other Packages
from nacf import css, get, json, urls, parallel
from nacf.types import Eles, Json

from configs import id_, headers, idheaders

IDURL = f"https://movie.douban.com/subject/{id_}/reviews?start="
ReviewURL = "https://movie.douban.com/j/review/{rid}/full"

Review = NamedTuple(
    "Review",
    [
        ("id", str),
        ("name", str),
        ("title", str),
        ("star", str),
        ("useful", str),
        ("useless", str),
        ("content", str),
    ],
)

NL = re.compile(r"(\n+|</\w+?>)")
RP = re.compile(r"(</>)+")


@get(IDURL + "0", headers=idheaders)
@css(".paginator a")
def pages(res: Eles) -> int:
    """Get page numbers of movie id."""
    return int(res[-2].text)


@urls([IDURL + str(i) for i in range(0, pages() * 20, 20)])
@parallel(4)
@get(headers=idheaders)
@css("div.review-item")
def getbase(eles: Eles) -> Iterable[Review]:
    """Get base information."""
    return map(
        lambda ele: Review(
            id=ele.attrs.get("id"),
            name=ele.find(".name", first=True)
            and ele.find(".name", first=True).text
            or "",
            title=ele.find("h2", first=True).text,
            star=ele.find(".main-title-rating", first=True)
            and ele.find(".main-title-rating", first=True)
            .attrs.get("class")[0]
            .lstrip("allstar")
            or "",
            useful="",
            useless="",
            content="",
        ),
        eles,
    )


def more(reviews: List[Review]) -> Iterable[Review]:
    """More information."""

    @urls(
        (
            ReviewURL.format(rid=e.id)
            for e in flatten(reviews, ignore=(Review,))
        )
    )
    @parallel(4)
    @get(headers=headers)
    @json
    def _(res: Json) -> Dict[str, str]:
        """_"""
        return {
            "useful": str(res.get("votes", {}).get("useful_count", "")),
            "useless": str(res.get("votes", {}).get("useless_count", "")),
            "content": RP.sub(
                "</>", NL.sub("</>", HTML(html=res.get("html", "")).text)
            ).replace("\t", "<>"),
        }

    return (
        Review(**{**review._asdict(), **r})
        for review, r in zip(reviews, flatten(_()))
    )


def write(reviews: Iterable[Review]) -> None:
    """Write out to name."""
    with open(id_, "w") as f:
        f.write("\n".join(map(lambda r: "\t".join(r), reviews)))


if __name__ == "__main__":
    write(
        flatten(
            more(list(flatten(getbase(), ignore=(Review,)))), ignore=(Review,)
        )
    )

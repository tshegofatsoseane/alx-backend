#!/usr/bin/env python3
"""A pagination helper function.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Retrieves an index range from a page and the page size.
    """

    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)

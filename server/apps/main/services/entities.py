'''
Business entities used in the service layer.
'''

from typing import final, NamedTuple



@final
class AttractionPreview(NamedTuple):
    attraction_id: int
    name: str
    short_info: str
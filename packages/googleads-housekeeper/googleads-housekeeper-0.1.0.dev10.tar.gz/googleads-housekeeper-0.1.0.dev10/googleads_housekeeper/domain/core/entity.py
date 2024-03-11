from __future__ import annotations

from gaarf.base_query import BaseQuery


class ExcludableEntity(BaseQuery):

    base_query_text = ''

    def __init_subclass__(cls):
        required_fields = (
            'criterion_id',
            'placement_type',
            'placement',
        )
        super().__init_subclass__()
        if not all(requred_field in cls.base_query_text
                   for requred_field in required_fields):
            raise ValueError(
                'query_text does not contain all required fields: '
                f'{required_fields}'
            )

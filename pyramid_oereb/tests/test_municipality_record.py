# -*- coding: utf-8 -*-
import pytest
import shapely.wkt
import shapely.geometry

from pyramid_oereb.lib.records.logo import LogoRecord
from pyramid_oereb.lib.records.municipality import MunicipalityRecord


def test_get_fields():
    expected_fields = [
            'fosnr',
            'name',
            'published',
            'logo',
            'geom'
        ]
    fields = MunicipalityRecord.get_fields()
    assert fields == expected_fields


def test_mandatory_fields():
    with pytest.raises(TypeError):
        MunicipalityRecord()


def test_init():
    logo = LogoRecord('abcde')
    geometry = shapely.wkt.loads('MULTIPOLYGON(((123 456, 456 789, 789 123, 123 456)))')
    record = MunicipalityRecord(
        969,
        u'FantasyMunicipality',
        True,
        logo,
        geom=geometry
    )
    assert isinstance(record.fosnr, int)
    assert isinstance(record.name, unicode)
    assert isinstance(record.published, bool)
    assert isinstance(record.logo, LogoRecord)
    assert isinstance(record.geom, shapely.geometry.multipolygon.MultiPolygon)

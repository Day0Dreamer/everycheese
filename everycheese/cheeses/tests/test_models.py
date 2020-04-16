import pytest
from ..models import Cheese

# Connect out juices to the DB
pytestmark = pytest.mark.django_db


def test__str__():
    cheese = Cheese.objects.create(
        name='Gazbaccho',
        description='Very italian Spain cheese',
        firmness=Cheese.Firmness.SOFT,
    )
    assert cheese.__str__() == 'Gazbaccho'
    assert str(cheese) == 'Gazbaccho'

from unittest.mock import MagicMock
import pytest
from sqlalchemy.orm import Session
from pydantic_geojson import PolygonModel
from api.models.kingdom import Kingdom
from api.routes.kingdom import create_kingdom, read_kingdom, get_kingdoms, update_kingdom

@pytest.fixture
def mock_db_session():
    return MagicMock(spec=Session)

@pytest.fixture
def test_kingdom():
    return Kingdom(
        name='Test Kingdom',
        king='Test King',
        description='Test Description',
        territory=PolygonModel(
                type='Polygon',
                coordinates=[[[0, 0], [0, 1], [1, 1], [1, 0], [0, 0]]]
            )
        )

@pytest.mark.asyncio
async def test_create_kingdom(mock_db_session, test_kingdom):
    created_kingdom = await create_kingdom(test_kingdom, db_session=mock_db_session)
    mock_db_session.add.assert_called_once()
    mock_db_session.commit.assert_called_once()
    mock_db_session.refresh.assert_called_once()
    assert created_kingdom.name == test_kingdom.name
    assert created_kingdom.king == test_kingdom.king
    assert created_kingdom.description == test_kingdom.description

@pytest.mark.asyncio
async def test_read_kingdom(mock_db_session, test_kingdom):
    mock_db_session.query.return_value.filter.return_value.first.return_value = test_kingdom
    result = await read_kingdom(test_kingdom.id, db_session=mock_db_session)
    assert result == test_kingdom

@pytest.mark.asyncio
async def test_get_kingdoms(mock_db_session, test_kingdom):
    mock_db_session.query.return_value.all.return_value = [test_kingdom]
    result = await get_kingdoms(db_session=mock_db_session)
    assert result == [test_kingdom]

@pytest.mark.asyncio
async def test_update_kingdom(mock_db_session, test_kingdom):
    mock_db_session.query.return_value.filter.return_value.first.return_value = test_kingdom
    updated_kingdom = Kingdom(name='Updated Kingdom')
    result = await update_kingdom(test_kingdom.id, updated_kingdom, db_session=mock_db_session)
    mock_db_session.commit.assert_called_once()
    mock_db_session.refresh.assert_called_once()
    assert result.name == 'Updated Kingdom'

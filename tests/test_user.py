import pytest
import pytest_asyncio
import starlette
from httpx import ASGITransport, AsyncClient

from api.main import app


@pytest_asyncio.fixture()
async def async_client() -> AsyncClient:
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as client:
        yield client


@pytest.mark.asyncio()
async def test_list_users(async_client: AsyncClient) -> None:
    response = await async_client.get("/users")
    assert response.status_code == starlette.status.HTTP_200_OK


@pytest.mark.asyncio()
async def test_create_and_read_and_delete_user(async_client: AsyncClient) -> None:
    response = await async_client.post("/users", json={"user_name": "UserName1"})
    assert response.status_code == starlette.status.HTTP_200_OK
    response_obj = response.json()
    assert response_obj["user_name"] == "UserName1"

    response = await async_client.get("/users")
    assert response.status_code == starlette.status.HTTP_200_OK
    response_obj = response.json()
    assert len(response_obj) == 1
    assert response_obj[0]["user_name"] == "UserName1"

    response = await async_client.delete("/users/1")
    assert response.status_code == starlette.status.HTTP_200_OK

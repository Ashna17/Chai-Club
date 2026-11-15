import pytest
from fastapi.testclient import TestClient

from matching_service.domain.match import MatchRequest
from matching_service.main import app

client = TestClient(app)


def test_health_check() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_match_request_validates_role_and_required_fields() -> None:
    request = MatchRequest(
        user_id="user-1",
        role="host",
        topic="chai",
        latitude=48.1,
        longitude=11.5,
        max_distance_meters=5000,
    )

    assert request.role == "host"


def test_match_request_rejects_unknown_role() -> None:
    with pytest.raises(ValueError):
        MatchRequest(
            user_id="user-1",
            role="member",
            topic="chai",
            latitude=48.1,
            longitude=11.5,
            max_distance_meters=5000,
        )

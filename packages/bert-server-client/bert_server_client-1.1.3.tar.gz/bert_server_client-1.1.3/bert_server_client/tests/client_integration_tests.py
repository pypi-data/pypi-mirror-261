import json
import uuid
from dataclasses import asdict

import pytest
from bert_server_client.client import BertClient
from bert_server_client.schema.embedding import EmbeddingRequest, EmbeddingResponse
from bert_server_client.schema.health_check import HealthCheck


@pytest.fixture
def bert_client():
    host = "tcp://localhost:5555"
    client = BertClient(host)
    yield client
    client.close()


def test_request_to_bert_server(bert_client):
    request = EmbeddingRequest(
        input=['I like icecream', 'geopolitical policy', 'what is this thing here', 'no thats wrong'],
        model="test_model", user=uuid.uuid4())
    response = bert_client.send_embedding_request(request)

    assert response is not None
    assert isinstance(response, EmbeddingResponse)
    print(json.dumps(asdict(response), indent=4))


def test_health_check(bert_client):
    response = bert_client.send_health_check_request()

    assert response is not None
    assert isinstance(response, HealthCheck)
    print(json.dumps(asdict(response), indent=4))

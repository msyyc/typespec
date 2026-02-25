from azure.core.rest import HttpRequest
from azure.core import PipelineClient
import json
import io

BASE_URL = "http://localhost:3000"
URL = f"{BASE_URL}/type/file/body/request/json-content-type"
BODY = json.dumps({"message": "test file content"}, separators=(",", ":"))

with PipelineClient(base_url=BASE_URL) as client:
    # Test 1: bytes content
    request = HttpRequest(
        method="POST",
        url=URL,
        headers={"Content-Type": "application/json"},
        content=BODY.encode("utf-8"),
    )
    response = client.send_request(request)
    response.raise_for_status()
    assert response.status_code == 204
    print("Test 1 (bytes) passed! Status:", response.status_code)

    # Test 2: TextIO (StringIO) content
    text_stream = io.StringIO(BODY)
    request = HttpRequest(
        method="POST",
        url=URL,
        headers={"Content-Type": "application/json"},
        content=text_stream,
    )
    response = client.send_request(request)
    response.raise_for_status()
    assert response.status_code == 204
    print("Test 2 (StringIO / TextIO) passed! Status:", response.status_code)

    # Test 3: BinaryIO (BytesIO) content
    binary_stream = io.BytesIO(BODY.encode("utf-8"))
    request = HttpRequest(
        method="POST",
        url=URL,
        headers={"Content-Type": "application/json"},
        content=binary_stream,
    )
    response = client.send_request(request)
    response.raise_for_status()
    assert response.status_code == 204
    print("Test 3 (BytesIO / BinaryIO) passed! Status:", response.status_code)


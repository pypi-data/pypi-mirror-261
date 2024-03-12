# test_datafog.py
import pytest
import requests

from datafog import DataFog


@pytest.fixture
def datafog():
    return DataFog()


def test_call_with_redact(datafog):
    url = "https://gist.githubusercontent.com/sidmohan0/1aa3ec38b4e6594d3c34b113f2e0962d/raw/42e57146197be0f85a5901cd1dcdd9ad15b31bab/sotu_2023.txt"
    privacy_operation = "redact"

    result = datafog(url, privacy_operation)

    assert "[REDACTED]" in result
    assert "Joe Biden" not in result


def test_call_with_annotate(datafog):
    file_path = "sotu_2023.txt"
    url = "https://gist.githubusercontent.com/sidmohan0/1aa3ec38b4e6594d3c34b113f2e0962d/raw/42e57146197be0f85a5901cd1dcdd9ad15b31bab/sotu_2023.txt"
    file_content = requests.get(url).text
    with open(file_path, "w") as file:
        file.write(file_content)
    privacy_operation = "annotate"

    result = datafog(str(file_path), privacy_operation)

    assert "[ORG]" in result
    assert "Joe Biden" not in result


def test_call_with_unsupported_input_type(datafog):
    input_source = 123  # Invalid input type
    privacy_operation = "redact"

    with pytest.raises(ValueError, match="Unsupported input source type"):
        datafog(input_source, privacy_operation)


def test_call_with_unsupported_privacy_operation(datafog):
    url = "https://gist.githubusercontent.com/sidmohan0/1aa3ec38b4e6594d3c34b113f2e0962d/raw/42e57146197be0f85a5901cd1dcdd9ad15b31bab/sotu_2023.txt"
    privacy_operation = "invalid_operation"

    with pytest.raises(
        ValueError, match=f"Unsupported privacy operation: {privacy_operation}"
    ):
        datafog(url, privacy_operation)

def test_scan_functionality(datafog):
    text = "John Doe's email is john@example.com and his phone number is (123) 456-7890."
    results = datafog(text, "scan")
    privacy_operation = "scan"
    result = datafog(text, privacy_operation)

    assert any(result == "PERSON" in result )
    assert any(result == "EMAIL" in result )
    assert any(result == "PHONE" in result )

# def test_scan_no_entities(datafog):
#     text = "This text does not contain any PII entities."
#     results = datafog(text, "scan")

#     assert len(results) == 0

# def test_annotate_functionality(datafog):
#     text = "John Doe's email is john@example.com and his phone number is (123) 456-7890."
#     annotated_text = datafog(text, "annotate")

#     assert "[PERSON]" in annotated_text
#     assert "[EMAIL]" in annotated_text
#     assert "[PHONE]" in annotated_text

# def test_annotate_no_entities(datafog):
#     text = "This text does not contain any PII entities."
#     annotated_text = datafog(text, "annotate")

#     assert annotated_text == text

# def test_scan_and_annotate_with_deny_list(datafog):
#     text = "John Doe works at Acme Inc."
#     deny_list = ["Acme Inc."]

#     results = datafog.scan(text, deny_list=deny_list)
#     assert len(results) == 2
#     assert any(result.entity_type == "PERSON" for result in results)
#     assert any(result.entity_type == "ORG" for result in results)

#     annotated_text = datafog.annotate(text, results)
#     assert "[PERSON]" in annotated_text
#     assert "[ORG]" in annotated_text

# def test_invalid_privacy_operation(datafog):
#     text = "Some sample text"
#     with pytest.raises(ValueError) as excinfo:
#         datafog(text, "invalid_operation")
#     assert "Unsupported privacy operation" in str(excinfo.value)
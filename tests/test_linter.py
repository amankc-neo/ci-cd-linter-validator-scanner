import pytest
from scanner.utils import find_issues

def test_detect_latest_tag():
    sample = {
        "jobs": {
            "build": {
                "steps": [
                    {"uses": "docker/build-push-action@latest"}
                ]
            }
        }
    }
    issues = find_issues(sample)
    assert any("latest" in i for i in issues)

def test_missing_permissions():
    sample = {
        "jobs": {
            "build": {
                "steps": []
            }
        }
    }
    issues = find_issues(sample)
    assert any("permissions" in i for i in issues)

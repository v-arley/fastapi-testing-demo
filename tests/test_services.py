import pytest

from app.service import calculate_note_priority, validate_color


@pytest.mark.parametrize(
    "title, content, expected_priority",
    [
        ("Short", "Small content", "low"),
        ("A" * 50, "B" * 60, "medium"),
        ("A" * 100, "B" * 101, "high"),
    ]
)
def test_calculate_note_priority_returns_expected_priority(title, content, expected_priority):
    # Arrange

    # Act
    result = calculate_note_priority(title, content)

    # Assert
    assert result == expected_priority


@pytest.mark.parametrize(
    "color",
    ["yellow", "blue", "red", "green", "purple"]
)
def test_validate_color_returns_true_when_color_is_allowed(color):
    # Arrange

    # Act
    result = validate_color(color)

    # Assert
    assert result is True


@pytest.mark.parametrize(
    "color",
    ["black", "orange", "", "white"]
)
def test_validate_color_returns_false_when_color_is_not_allowed(color):
    # Arrange

    # Act
    result = validate_color(color)

    # Assert
    assert result is False
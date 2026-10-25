from datetime import date
import logic


def get_dummy_concerts():
    # Reset the global ID so tests are isolated and repeatable
    logic.concert_id = 0
    return [
        logic.create_concert("Band A", "Berlin", date(2026, 9, 10), 50.0),
        logic.create_concert("Band A", "Paris", date(2026, 9, 12), 70.0),
        logic.create_concert("Band B", "Berlin", date(2026, 9, 12), 120.0),
        logic.create_concert("Band A", "Berlin", date(2026, 9, 15), 60.0),
        logic.create_concert("Band C", "London", date(2026, 9, 11), 40.0)
    ]


def test_report_average_price_for_artist():
    concerts = get_dummy_concerts()

    # 1. Test the happy path
    assert logic.report_average_price(concerts, "Band A") == 60.0

    # 2. Test the exception path (TDD requires testing that validations trigger properly)
    try:
        logic.report_average_price(concerts, "Unknown")
        assert False, "Should have raised ValueError for unknown artist"
    except ValueError:
        assert True  # The exception was successfully caught


def test_report_concerts_per_city():
    concerts = get_dummy_concerts()
    counts = logic.report_concerts_per_city(concerts)

    # 1. Test the happy path
    # Berlin: 3, Paris: 1, London: 1
    assert counts["Berlin"] == 3
    assert counts["Paris"] == 1
    assert counts["London"] == 1
    assert "Rome" not in counts

    # 2. Test the exception path
    try:
        logic.report_concerts_per_city([])
        assert False, "Should have raised ValueError for empty list"
    except ValueError:
        assert True


def test_report_concerts_in_interval_sorted():
    concerts = get_dummy_concerts()
    start = date(2026, 9, 11)
    end = date(2026, 9, 13)

    # 1. Test the happy path
    result = logic.report_concerts_in_interval(concerts, start, end)

    # Should include Band C (40.0), Band A (70.0), Band B (120.0) in ascending price order
    assert len(result) == 3
    assert logic.get_artist(result[0]) == "Band C"
    assert logic.get_artist(result[1]) == "Band A"
    assert logic.get_artist(result[2]) == "Band B"

    # 2. Test the exception path (Start date after end date)
    try:
        logic.report_concerts_in_interval(concerts, end, start)
        assert False, "Should have raised ValueError for invalid date order"
    except ValueError:
        assert True


def test_report_concerts_in_city_and_interval():
    concerts = get_dummy_concerts()
    start = date(2026, 9, 11)
    end = date(2026, 9, 13)

    # Fixed the function name and argument order to match logic.py
    result = logic.report_concerts_in_city_and_interval(concerts, "Berlin", start, end)

    # Only Band B is in Berlin between 11/09 and 13/09
    assert len(result) == 1
    assert logic.get_artist(result[0]) == "Band B"
    assert logic.get_city(result[0]) == "Berlin"


if __name__ == "__main__":
    test_report_average_price_for_artist()
    test_report_concerts_per_city()
    test_report_concerts_in_interval_sorted()
    test_report_concerts_in_city_and_interval()
    print("All report tests passed successfully!")
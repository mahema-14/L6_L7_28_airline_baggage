
import pytest
from airline_baggage import baggage_fee, carry_on_ok, check_in_status


# BAGGAGE FEE - ALL DECISION BRANCHES

def test_unknown_cabin():
    with pytest.raises(ValueError):
        baggage_fee("first", 20, "domestic", False)


def test_negative_weight():
    with pytest.raises(ValueError):
        baggage_fee("economy", -5, "domestic", False)


def test_member_economy():
    assert baggage_fee("economy", 30, "domestic", True) == 100


def test_non_member():
    assert baggage_fee("economy", 20, "domestic", False) == 100


def test_business_member():
    assert baggage_fee("business", 50, "domestic", True) == 200


def test_no_excess():
    assert baggage_fee("business", 30, "domestic", False) == 0


def test_domestic_route():
    assert baggage_fee("economy", 40, "domestic", False) == 1000


def test_international_route():
    assert baggage_fee("economy", 40, "international", False) == 2500


def test_excess_above_20_international():
    assert baggage_fee("economy", 36, "international", False) == 2100


# CARRY ON - ALL DECISION BRANCHES

def test_infant_allowed():
    assert carry_on_ok(10, 2, True) is True


def test_infant_not_allowed():
    assert carry_on_ok(10, 3, True) is False


def test_non_infant_weight_allowed():
    assert carry_on_ok(7, 1, False) is True


def test_non_infant_weight_exceeded():
    assert carry_on_ok(8, 1, False) is False


def test_non_infant_item_limit_exceeded():
    assert carry_on_ok(5, 2, False) is False


# CHECK-IN - ALL DECISION BRANCHES

def test_checkin_with_baggage():
    assert check_in_status(60, True, False) == "open"


def test_checkin_without_baggage():
    assert check_in_status(45, False, False) == "open"


def test_checkin_international():
    assert check_in_status(105, False, True) == "open"


def test_checkin_late():
    assert check_in_status(35, False, False) == "late"


def test_checkin_closed():
    assert check_in_status(20, False, False) == "closed"


def test_checkin_international_late():
    assert check_in_status(90, False, True) == "late"

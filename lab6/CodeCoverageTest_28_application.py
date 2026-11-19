
import pytest
from airline_baggage import baggage_fee, carry_on_ok, check_in_status


# ---------------- BAGGAGE FEE TESTS ----------------

def test_within_allowance():
    assert baggage_fee("economy", 10, "domestic", False) == 0


def test_unknown_cabin():
    with pytest.raises(ValueError, match="unknown cabin"):
        baggage_fee("first", 20, "domestic", False)


def test_negative_weight():
    with pytest.raises(ValueError, match="invalid weight"):
        baggage_fee("economy", -5, "domestic", False)


def test_member_discount():
    assert baggage_fee("economy", 30, "domestic", True) == 100


def test_business_member():
    assert baggage_fee("business", 50, "domestic", True) == 200


def test_domestic_excess():
    assert baggage_fee("economy", 30, "domestic", True) == 100


def test_international_excess():
    assert baggage_fee("economy", 20, "international", False) == 225


def test_excess_above_20_domestic():
    assert baggage_fee("economy", 40, "domestic", False) == 1000


def test_excess_above_20_international():
    assert baggage_fee("economy", 40, "international", False) == 2500


# ---------------- CARRY ON TESTS ----------------

def test_infant_allowed():
    assert carry_on_ok(10, 2, True) is True


def test_infant_too_many_items():
    assert carry_on_ok(10, 3, True) is False


def test_non_infant_allowed():
    assert carry_on_ok(7, 1, False) is True


def test_non_infant_too_heavy():
    assert carry_on_ok(8, 1, False) is False


def test_non_infant_too_many_items():
    assert carry_on_ok(5, 2, False) is False


# ---------------- CHECK IN STATUS TESTS ----------------

def test_checkin_open():
    assert check_in_status(100, False, False) == "open"


def test_checkin_late():
    assert check_in_status(35, False, False) == "late"


def test_checkin_closed():
    assert check_in_status(20, False, False) == "closed"


def test_checkin_with_baggage():
    assert check_in_status(60, True, False) == "open"


def test_checkin_international():
    assert check_in_status(120, False, True) == "open"


def test_checkin_international_late():
    assert check_in_status(90, False, True) == "late"

# test_processor.py
from processor import process_transaction

def test_successful_transaction():
    """
    This test only checks the happy path.
    It triggers the Green and half of the Yellow logic.
    """
    result = process_transaction(100, "SUCCESS")
    assert result == "Transaction Complete"
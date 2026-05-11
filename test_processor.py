from processor import process_transaction

def test_successful_transaction():
    """
    This test only checks the happy path.
    It triggers the Green and half of the Yellow logic.
    """
    result = process_transaction(100, "SUCCESS")
    print(result)
    assert result == "Transaction Complete"

def test_failed_transaction():
    assert process_transaction(100, "FAILED") == "Transaction Error"
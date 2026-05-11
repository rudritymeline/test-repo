# processor.py

def process_transaction(amount, status):
    # 🟢 GREEN: Fully Covered
    # We will pass a positive amount in our test.
    if amount > 0:
        print(f"Processing transaction: ${amount}")
        
    # 🟡 YELLOW: Partial Coverage
    # We will test 'SUCCESS', but NOT 'FAILED'. 
    # The 'else' block will stay "Red/Uncovered", making this line Yellow.
    if status == "SUCCESS":
        return "Transaction Complete"
    else:
        return "Transaction Error"

def unused_emergency_stop():
    # 🔴 RED: Entirely Uncovered
    # We won't call this at all. 
    # It shows as a "Dark Corner" in your Codecov report.
    print("EMERGENCY STOP ACTIVATED")
    return False

def new_untested_feature():
    print("This is a new feature with no tests!")
    return True
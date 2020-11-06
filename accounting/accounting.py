from user.authentication import *
from transactions.journal import *
import banking.reconciliation
import sys

# help("modules")

if __name__ == "__main__":
    
    authenticate_user()
    receive_income(100)
    pay_expense(100)
    # banking.reconciliation.do_reconciliation()
    # banking.fvb.reconciliation.do_reconciliation()
    # banking.ubsa.reconciliation.do_reconciliation()
    if len(sys.argv) > 1:
        print("\n".join(sys.argv[1:]))
    # banking.online.reconciliation.do_reconciliation()
    banking.fvb.reconciliation.do_reconciliation()
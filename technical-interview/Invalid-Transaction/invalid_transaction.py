from typing import List

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        checker = {}
        invalid = []

        for transaction in transactions:
            name, time, amount, city = transaction.split(',')
            time, amount = int(time), int(amount)
            
            if amount > 1000:
                invalid.append(transaction)
            
            if name not in checker:
                checker[name] = []
            
            for prev_transaction in checker[name]:
                prev_time, prev_city = prev_transaction
                if abs(prev_time - time) <= 60 and city != prev_city:
                    invalid.append(transaction)
                    invalid.append(f"{name},{prev_time},{amount},{prev_city}")
            
            checker[name].append((time, city))
        
        return list(set(invalid))
import sqlite3

conn = sqlite3.connect("churn.db")
cursor = conn.cursor()

query = """
SELECT 
    ROUND(
        COUNT(*) * 100.0 /
        (SELECT COUNT(*) FROM customer_churn WHERE Churn_Label='Yes'),
    2)
FROM customer_churn
WHERE Churn_Label='Yes'
AND Contract='Month-to-month'
AND Tenure_Months < 3;
"""

cursor.execute(query)

result = cursor.fetchone()

print("Churn Insight %:", result[0])

conn.close()
month_Sales = [1200, 1300, 1450, 2000, 1250]
month_Sales.sort(reverse=True)
threshold = 1350

for(index, sales) in enumerate(month_Sales, start=1):
    if sales < threshold:
        print(f"Sales less than threshold in month {index}: {sales}")
        break
    else:
        print(f"Sales in month {index}: {sales}")
def calculate_fine(book_title, days_overdue, daily_rate=5, max_fine=150):
    fine= days_overdue*daily_rate
    fine=min(fine,max_fine)
    return fine

book_title=input()
days_overdue=int(input())
fine=calculate_fine(book_title,days_overdue)
print(f"Book: {book_title}")
print(f"Days overdue: {days_overdue}")
print(f"Fine: Rs. {fine}")

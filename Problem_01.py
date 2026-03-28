def calculate_fine(book_title, days_overdue, daily_rate=5.0, max_fine=150.0):
    """
    Calculate the overdue fine for a book.

    Parameters:
    book_title (str): Title of the book.
    days_overdue (int): Number of overdue days.
    daily_rate (float): Fine charged per day | Default=5.0.
    max_fine (float): Maximum fine limit | Default=150.0.

    Returns:
    float:  Fine after applying the maximum cap.
    """
    fine= days_overdue*daily_rate
    fine=min(fine,max_fine)
    return fine

book_title=input()
days_overdue=int(input())
fine=calculate_fine(book_title,days_overdue)
print(f"Book: {book_title}")
print(f"Days overdue: {days_overdue}")
print(f"Fine: Rs. {fine}")

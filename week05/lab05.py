def calculate_average_age(users):
    """Return the average numeric age, or 0.0 when none are valid."""
    valid_ages = []

    for user in users:
        age = user.get("age")
        if isinstance(age, (int, float)) and not isinstance(age, bool):
            valid_ages.append(age)

    if not valid_ages:
        return 0.0

    return sum(valid_ages) / len(valid_ages)


def get_active_user_emails(users):
    """Return email addresses belonging to active users."""
    emails = []

    for user in users:
        is_active = user.get("is_active")
        email = user.get("email")

        if is_active and email:
            emails.append(email)

    return emails

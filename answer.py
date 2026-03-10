def find_duplicate_emails(file_path):
    SeenEmails = set()
    duplicates = set()

    with open(file_path, "r") as file:
        for line in file:
            email = line.strip()

            if email in SeenEmails:
                duplicates.add(email)
            else:
                SeenEmails.add(email)

    return duplicates


if __name__ == "__main__":
    file_path = "emails.txt"

    duplicate_emails = find_duplicate_emails(file_path)

    print("Duplicate Emails:")
    for email in duplicate_emails:
        print(email)

    print(f"\nTotal duplicates found: {len(duplicate_emails)}")
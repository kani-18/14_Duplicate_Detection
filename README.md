# Duplicate Email Detection using Python

## Problem Statement

You are given a file containing **100 million email addresses**, where some emails may appear multiple times.
The goal is to **efficiently detect duplicate email addresses** while handling large data.

---

# Algorithm

1. Open the file containing email addresses.
2. Read the file **line by line** to avoid loading the entire file into memory.
3. Maintain a **set called `seen_emails`** to store unique email addresses.
4. Maintain another **set called `duplicates`** to store duplicate email addresses.
5. For each email in the file:

   * If the email already exists in `seen_emails`, add it to `duplicates`.
   * Otherwise insert it into `seen_emails`.
6. After processing the file, output the duplicate email addresses.

---

# Python Implementation

```python
def find_duplicates(file_path):
    seen_emails = set()
    duplicates = set()

    with open(file_path, "r") as file:
        for line in file:
            email = line.strip()

            if email in seen_emails:
                duplicates.add(email)
            else:
                seen_emails.add(email)

    return duplicates


file_path = "emails.txt"
duplicates = find_duplicates(file_path)

print("Duplicate Emails:")
for email in duplicates:
    print(email)
```

---

# Data Structures Used

## 1. Python Set (`set`)

Used for storing unique email addresses.

**Advantages:**

* Fast lookup
* Average **O(1)** time complexity
* Prevents duplicate entries automatically

Example:

```
seen_emails = {
    "user1@gmail.com",
    "user2@yahoo.com",
    "user3@outlook.com"
}
```

---

## 2. Set for Duplicates

Stores duplicate emails without repetition.

Example:

```
duplicates = {
    "user1@gmail.com",
    "user5@gmail.com"
}
```

---

# Time Complexity

Let:

```
N = number of email addresses
```

Operations performed:

* Set lookup → **O(1) average**
* Set insertion → **O(1) average**

Total time complexity:

```
O(N)
```

Each email is processed only once.

---

# Space Complexity

Worst case scenario:

* All emails are unique.

Memory usage:

```
O(N)
```

Where **N = number of unique emails stored in the set**.

---

# Handling Extremely Large Data

If the dataset is too large to fit into memory, we can use:

### 1. Bloom Filter

A probabilistic data structure that detects duplicates using very little memory.

### 2. External Sorting

1. Sort the emails on disk.
2. Compare adjacent emails to detect duplicates.

### 3. Distributed Processing

Use frameworks such as:

* Apache Spark
* Hadoop MapReduce

These allow large-scale processing of datasets.

---

# Complexity Summary

| Metric           | Complexity |
| ---------------- | ---------- |
| Time Complexity  | **O(N)**   |
| Space Complexity | **O(N)**   |

---

# Technologies Used

* Python
* File Streaming
* Hash-based Data Structures (`set`)

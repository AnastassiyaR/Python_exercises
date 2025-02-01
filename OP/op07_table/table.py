import re


def create_table_string(text: str) -> str:
    """
    Create table string from the given logs.
    """
    times = get_times(text)
    usernames = get_usernames(text)
    errors = get_errors(text)
    addresses = get_addresses(text)
    endpoints = get_endpoints(text)

    # Convert times to 12-hour format
    formatted_times = []
    for hour, minute, utc_offset in times:
        utc_hour = (hour - utc_offset) % 24
        period = "AM" if utc_hour < 12 else "PM"
        if utc_hour == 0:
            utc_hour = 12
        elif utc_hour > 12:
            utc_hour -= 12
        formatted_times.append(f"{utc_hour}:{minute:02d} {period}")

    # Unique and sorted items
    formatted_times = sorted(set(formatted_times))
    usernames = sorted(set(usernames))
    errors = sorted(set(errors))
    addresses = sorted(set(addresses))
    endpoints = sorted(set(endpoints))

    # Create table rows
    table = []
    if formatted_times:
        table.append(f"time | {', '.join(formatted_times)}")
    if usernames:
        table.append(f"user | {', '.join(usernames)}")
    if errors:
        table.append(f"error | {', '.join(map(str, errors))}")
    if addresses:
        table.append(f"ipv4 | {', '.join(addresses)}")
    if endpoints:
        table.append(f"endpoint | {', '.join(endpoints)}")

    # Adjust the spacing for alignment
    max_length = max(len(row.split('|')[0]) for row in table) if table else 0
    aligned_table = []
    for row in table:
        category, items = row.split('|')
        aligned_table.append(f"{category.ljust(max_length)} | {items.strip()}")

    return "\n".join(aligned_table) if aligned_table else ""


def get_times(text: str) -> list[tuple[int, int, int]]:
    """
    Get times from text using the time pattern.
    """
    time_pattern = r'(\d{1,2})[^\d]*(\d{1,2})[^\d]*(UTC[-+]\d{1,2})'
    matches = re.findall(time_pattern, text)
    times = []

    for hour, minute, utc_offset in matches:
        hour, minute = int(hour), int(minute)
        if (0 <= hour < 24) and (0 <= minute < 60):
            offset = int(utc_offset[3:]) if utc_offset[3] != '-' else -int(utc_offset[4:])
            times.append((hour, minute, offset))

    return times


def get_usernames(text: str) -> list[str]:
    """Get usernames from text."""
    username_pattern = r'usr:([a-zA-Z0-9_]+)'
    return re.findall(username_pattern, text)


def get_errors(text: str) -> list[int]:
    """Get errors from text."""
    error_pattern = r'error\s*(\d{1,3})'
    return [int(code) for code in re.findall(error_pattern, text, re.IGNORECASE)]


def get_addresses(text: str) -> list[str]:
    """Get IPv4 addresses from text."""
    address_pattern = r'(\b(?:\d{1,3}\.){3}\d{1,3}\b)'
    return re.findall(address_pattern, text)


def get_endpoints(text: str) -> list[str]:
    """Get endpoints from text."""
    endpoint_pattern = r'(/[\w&=?%-]*)'
    endpoints = re.findall(endpoint_pattern, text)
    return sorted(set(endpoints))  # Return unique endpoints in sorted order


if __name__ == '__main__':
    logs = """
            [14?36 UTC+9] /tere eRRoR 418 192.168.0.255
            [8B48 UTC-6] usr:kasutaja
            """
    print(get_endpoints(f'/cfepechz /api/orders'))  # -> ['/cfepechz', '/api/orders']
    print(get_times("[-1b35 UTC+0"))  # -> []
    print(get_times("[10:53 UTC+3]"))  # -> [(10, 53, 3)]
    print(get_times("[1:43 UTC+0]"))  # -> [(1, 43, 0)]
    print(get_times("[14A3 UTC-4] [14:3 UTC-4]"))  # -> [(14, 3, -4), (14, 3, -4)]
    print(create_table_string(logs))
    # Expected Output:
    # time | 5:36 AM, 2:48 PM
    # user | kasutaja
    # error | 418
    # ipv4 | 192.168.0.255
    # endpoint | /tere
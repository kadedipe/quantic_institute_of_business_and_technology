import requests

def normalize_url(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        return "http://" + url
    return url

def check_website(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code < 400:
            return "up"
        else:
            return "down"
    except requests.RequestException:
        return "down"

def check_websites_from_file(filename):
    try:
        with open(filename, 'r') as file:
            addresses = file.readlines()
        
        for address in addresses:
            address = address.strip()
            if not address:
                continue  # Skip empty lines
            full_url = normalize_url(address)
            status = check_website(full_url)
            print(f"{address} is {status}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

# Run the function
check_websites_from_file("addresses.txt")

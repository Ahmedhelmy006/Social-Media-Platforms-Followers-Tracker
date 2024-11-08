import json

def clean_cookies(cookies):
    required_cookies = {"li_at", "li_rm", "JSESSIONID"}
    cleaned_cookies = []

    for cookie in cookies:
        if cookie["name"] in required_cookies:
            if cookie.get("sameSite") not in {"Strict", "Lax", "None"}:
                cookie["sameSite"] = "Lax"
            cookie["secure"] = True
            cookie["httpOnly"] = True if cookie["name"] in {"li_at", "li_rm"} else cookie["httpOnly"]
            cleaned_cookies.append(cookie)

    return cleaned_cookies

with open('cookies.json', 'r') as f:
    cookies = json.load(f)

cleaned_cookies = clean_cookies(cookies)

with open('cookies.json', 'w') as f:
    json.dump(cleaned_cookies, f, indent=4)

print("Cookies cleaned and saved successfully.")

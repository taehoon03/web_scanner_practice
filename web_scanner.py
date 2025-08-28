import requests

def result_line(name,status,detail=""):
    tag={"Pass":"✅","Warn":"\u26A0\uFE0F","Fail":"❌"}.get(status,"")
    return f"{tag}{name}:{status}" + (f"-{detail}" if detail else "")

def fetch(url:str)->requests.Response:
    headers = {"User-Agent":"Web scanner/1.0"}
    return requests.get(url,headers=headers,timeout=10,allow_redirects="True")

# 테스트
if __name__ == "__main__":
    print(result_line("HTTPS", "Pass"))
    print(result_line("Header", "Warn", "Missing CSP"))
    print(result_line("XSS", "Fail", "Reflected XSS detected"))

    resp = fetch("https://example.com")
    print("상태 코드:", resp.status_code)
    print("최종 URL:", resp.url)



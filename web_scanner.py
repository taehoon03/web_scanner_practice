import sys
import html
import re
from urllib.parse import urlparse ,urlencode, parse_qs,urlunparse
import requests

 # 유틸 
def result_line(name,status,detail=""):
    #상태는 pass / warn / Fail 중 하나 
    tag = {"Pass":"\u2705","Warn":"\u26A0","Fail":"\u274C"}.get(status,"")
    return f"{tag}{name}:{status}" + (f"-{detail}"if detail else "")

#fetch로 url을 받아 requests.Response로 반환
def fetch(url:str) -> requests.Response:
    header = {"User-Agent":"Webscanner/1.0"}
    return requests.get (url,headers=header,timeout=10,allow_redirects=True)

def check_https(resp: requests.Response):
   
   
    parsed = urlparse(resp.url) #받은 문자열(url)을 구조화해서 필요한 부분만 추출
    if parsed.scheme.lower() =="https": #url의 프로토콜(scheme, http/https)을 소문자로 변환해서 확인
        return result_line("HTTPS","Pass",f"Using HTTPS({parsed.netloc})")#URL의 도메인(네이버, 구글 같은 서버 주소)을 f-string 안에 삽입
    else:
        return result_line("HTTPS","Fail",f"Using HTTP({parsed.netloc})")
    
if __name__ == "__main__":
    print("[DEBUG] start")                      
    if len(sys.argv) < 2:
        print("Usage: python webscan.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    print("[DEBUG] arg:", url)                  
    try:
        resp = fetch(url)
        print("[DEBUG] status:", resp.status_code, "final:", resp.url)  
    except requests.exceptions.RequestException as e:
        print(result_line("Fetch","Fail",str(e)))
        sys.exit(2)

    print(check_https(resp))
    

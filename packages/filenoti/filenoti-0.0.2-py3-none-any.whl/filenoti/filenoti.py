from contextlib import contextmanager
import requests    

def key_searcher():
    pass
def line_request(content):
    global api_key  
    api_url = "https://notify-api.line.me/api/notify"
    headers = {'Authorization': 'Bearer ' + api_key}
    message = {"message": content}
    response = requests.post(api_url, headers=headers, data=message)
    return response


# 커스텀 print 함수
def noti_print(*args, **kwargs):
    global api_key  

    
    # args는 튜플 형태로 전달되므로, 이를 하나의 문자열로 변환
    output = ' '.join(map(str, args))
    
    try:
        response = line_request(output)  
        if response.status_code == 200:
            print(f"Request successful. Response code: {response.status_code}")
            
        else:
            print(f"Request failed with status code: {response.status_code}")
    except requests.exceptions.RequestException as e: 
        print(f"Request failed: {e}")
        
        
        
@contextmanager
def main(start_noti = True,sucess_message = 'Sucess',error_message= 'Error',start_message = "File start"):  
    global api_key  
    if start_noti:
        line_request(start_message)
    try:
        yield 
        line_request(sucess_message)
    except Exception as e:
        line_request(error_message)
        line_request(e)
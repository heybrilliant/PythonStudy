#2021.11.04 Progrmmers Python Basic <module 사용하기>

def get_web(url):
    """URL을 넣으면 페이지 내용을 올려주는 함수"""
    import urllib.request #urllib이라는 라이브러리 호출
    response = urllib.request.urlopen(url) #받은 url을 열고 
    data = response.read() #데이터를 읽어서 
    decoded = data.decode('utf-8') #사람이 읽을 수 있게 디코딩을 하고 
    return decoded # 돌려주는 함수 

url = input('웹 페이지 주소?')
content = get_web(url) 
print(content) #받은 url을 출력

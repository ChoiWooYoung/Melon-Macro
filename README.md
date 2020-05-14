# Melon-Macro
Selenium을 이용한 멜론 스트리밍 서비스 친밀도 상승용 공유 및 조회 매크로

## 환경
* Windows 10
* Linux (Ubuntu 18.04 LTS)
* Python 3.8.x

## 필요한 것들
* Python 3.8.x
* Selenium

## 사용법
* 앨범 URL, 카카오 ID, PW 설정, 해당 앨범에 있는 곡 수 (albumcnt) 설정 후 사용바람
* Song_Share.py 이용

## 주의사항
* 타기기로 스트리밍중 매크로 사용 시, 동영상 조회 과정에 오류가 발생할 수 있음
* friend_template.py, tweet_template.py 는 조회에 반영이 안됨
* webdriver path 를 변경 해주어야함 (기본값 /usr/local/bin/chromedriver)
## Extra
* Windows 환경일 경우 Headless 사용시 더 편함 (Linux 환경에서는 Headless, No-Sandbox 필수)

```
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument("disable-gpu")
options.add_argument('lang=ko_KR')
driver = webdriver.Chrome('DRIVER PATH', chrome_options = options)
```
## 궁금한 것들
* Issues 탭에 남겨주길 바람

## 스크린샷
![initial](https://user-images.githubusercontent.com/11593330/81915006-f9074a80-960c-11ea-9e53-094242b49fa1.png)



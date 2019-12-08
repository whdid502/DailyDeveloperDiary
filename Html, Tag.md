# HTML

* web 페이지를 만드는 코드 : html
> html : 쉽고, 주요하다.(hyper text markup lauguage)

* web 은 public domain : 저작권이 없다.
> editor 로는 atom을 선정

##### client와 server
```
  client    -------------------request------------> server
  fornt end <------------------response-----------  backend
```

* web을 인터넷에 연결시키기
1) web sever가 돼서 연결하는법 : 너무 어렵다, 내가 상시 서버를 유지하고잇어야한다.
> web server은 제품군이다 제품에는 [Apachㄷ](https://www.apache.org/), IIS, [Nginx](https://www.nginx.com/)가 있다.  
  Apach의 경우 오픈소스에 무료이다. 언제나 1위이다.
2) web hosting은 호스트를 빌려주는 웹호스팅업체(서버의역할)가 많다. github도 여기에포함된다.
> 그외에 [bitballon](https://www.bitballoon.com/), [neocities](http://neocities.org/), [Amazon S3](https://aws.amazon.com/ko/s3/), [Google Cloud Storage](https://cloud.google.com/storage/?authuser=1&hl=ko), [Azure Blob](https://azure.microsoft.com/ko-kr/services/storage/blobs/) 들이 있다.

# TAG

* html tag
> 앞의 태그는 열리는태그, 뒤의 태그는 닫히는 태그 라고한다.  
> 태그는 쉽게 설명해준다!  
> 보통 평균적으로 28가지의 태그</>로 웹페이지는 만들어진다.(토탈 약 150개)  

* 왜 tag를 쓸까 : web이 가지고잇는 본래의 의미 정보란것을 더 탄탄하게 gui로 하는것보다 cli로 web page를 작성하면 보다 깔끔하게 만들어진다.

* 속성, attribute : 의미를 부여해주는 html태그의 세부사항을 조절해주는 것

* 부모태그,자식태그 
```
<parent>
  	<child></child>
 </parent>
```
> 이들의 위치는 항상바뀌지만, 고정돼잇는것도있다. 

#### 주요한 28가지의 TAG
```
* <strong>,</storng> : 굵게, 강조표시
```
```
* <u>,</u> : 밑줄
```
```
* <h1>,</h1> : headline, 제목표시(줄바꿈, 굵게), h1~h6까지 로 크기를 정한다. 1일수록 크다.
```
```
* <html>, </html> : 가장 통괄적으로 처음과 끝을 묶기.
```
```
* <head>, <head> : 머리묶기, 본문을 소개오후 하는것 
```
```
* <body>, </body> : 본문묶기
```
```
* <title>, </title> : 제목정하기
```
```
* <meta> 
> charset="" : 문자를 어떤 인코딩으로 읽을것인가.  
```
```
*  <div>, </div>s
```
```
* <a>, </a> : anchor닻을의미함, link 를 해준다.
> href="" : link 된 주사
>> target="_blank" : 새탭에서열기
>>> title="" : 주석
```
```
* <script>, </script>
```
```
* <link>, </link>
```
```
* <img> : 이미지삽입
> src="" : 어떤이미지?
>>widt="" : 크기는어떻게
```
```
* <span>, </span> : 그자체로는 아무것도 없지만, ssl 과 같이 사용한다면 공간을 지정해주는 의미로쓰여진다.
```
```
* <li>, </li> : 목록만들기
> <ul>,</ul> : li태그의 부모태그, 서로 반드시 잇어야한다. 목록을 그룹화하기위함. unoreder list
>> <os>, </os> : 같은 부모태그, ul과 다른점은 스스로 순서를 매겨준다. ordered list
```
```
* <style>, </style>
```
```
* <input>, </input>
```
```
* <form>, </form>
```
```
* <nav>, </nav>
```
```
* <header>, </headr>
```
```
* <footer>, </footer>
```
```
* <iframe>, </iframe>
```
```
* <button>, </button>
```
```
* <i>, </i>
```
```
* <br> : 줄바꿈, 닫힘태그가없다.
```
```
* <p>, </p> : 문단 구분 태그, > 정보로서 좀더 중요한 가치
```

# Shell

* Shell : 사람이 컴퓨터에게 명령을내리는 프로그램, shell의 종류로 bash, zbash, ksh, csh등이있음  
> * shell script : shell을 텍스트형식으로 작성해서 명령을내리는프로그램  

* Sh : 초기의 유닉스쉘,$   

* Bash : Sh와 호환됨 ,#  

* Bashrc : Bash가 참고할 사항을 정의해놓는 파일  

* Z Bash : Bash,Ksh,Tcsh 등의 기능을포함한 확장형 쉘  



# linux cmd

#### 예약어
* 이미 의미가 등록되있는말, 식별자로 예약어를 쓸순없다. 식별자란 쉽게말하자면 우리가 붙여주는 이름, 이는 키워드와 겹칠수없다.  

* `pwd` : 현재 dr 위치  

* `ls` : 현 dr 내용  
  `ls -alF` : 현 dr 내용 + 스캔 + 상세정보  
  `ls -l` : 자세히  
  `ls -al` : 숨김파일도  
  `ls -F` : dir은 끝을 / 표시  \>> alF와 al의 기능차이가 없는것은 명령의 내용을 포함하는 상위명령어가 있기 때문이다.    

* `mkdir 이름` : make directory, 현재 dr에 dr만들기  
  `mkdir -p 이름1/이름2..` : 마트료시카처럼 여러개만들기가능(~/Deskotp/이름1/이름2/이름3...)  

* `cd dr이름` : dr로 이동(cd만 치면 홈으로이동)  
  `cd .` : 현 dr  
  `cd ..` : 상위 (cd ../../ : 두단계상위dr로감)  
  `cd /` : 루트dr로감  

* `nano hello.txt` : 쉘 안의 간단한 텍스트편집기  
  
* `cat hello.txt` : 편집기 내용보기  

* `man 명령어` : 명령어의 도움말 및 상세설명을 본다.  

* `sudo 명령어 ~` : 관리자권한으로 명령어실행  
  `sudo -i` : 일시적으로 관리자가됨  
  `sudo exit` : 일반유저로복귀  

* `echo "내용"` : 내용을 화면에 출력  
  `echo "내용" > file.txt` : "내용"을 지는 file.txt를 생성  
  `echo "내용2" >> file.txt : file.txt에 "내용2"를 추가

* `cat <파일>` : 파일의 내용을 표시(긴파일을 끊어서 출력해줌)  

* `rm <파일>` : 파일삭제  
  `rm -rf <dr>` : 좀위험한 묻지마dr삭제   
  `rm -ir <dr>` : 물어보고 dr삭제   

* `mv <A> <B>` : A와 B가 같은 파일이면 이름변경  
                 A가 dir이고 B를 같은위치의 dir로지정하면 이름변경  
                 B가 A와 다른 위치의 dir이라면 위치이동  
                 
* `cp <a> <b>` : a를 b란이름으로 복사, `mv`의 경우와 같다.

### http

* http와 https : https는 네트워크프로토콜(통신규약)인 http프로토콜의 보안강화버전. https의 s는 secure즉 보안강화이다 https는 새로운 어플리케이션 (응용프로그램)의 계층이아니다
* https는 통신소켓의 부분을 ssl,tls로 대체한다, 직접 tcp(인터넷상에서 데이터를 메세지의형태로 보내기위해ip와 함께 사용하는 프로토콜)와 통신하지않는다. ssl은 http와 아예 독립된 프로토콜. tls도 ssl과 같은 암호화프로토콜. 


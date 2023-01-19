# Lab_share

## 소개

내가 만든 프로그램을 그룹원들과 공유하기 위해 만듬.

에러나 오류등에 대해서 말씀해 주시면 감사하겠습니다.


## 접근 & 권한
  다음 파일에 접근해야합니다.
* .bashrc

home에 다음 폴더를 만들어야 합니다.
* .rws


## 설치 방법
1. 본 git repositories를 개인 ubuntu에 clone합니다. (어디에 하던지 상관 없음.)

```
git clone https://github.com/johninkorea/lab_share.git
```
2. 해당 폴더 안으로 들어갑니다.
```
cd lab_share
```
3. 설치파일을 실행해 줍니다.
```
sh setup.sh
```
4. 터미널을 다시 시작합니다.

(설치후 clone 한 레파지토리는 삭제해도 됌)


## 사용 방법
* murnaghan fitting
1. 에너지 데이터가 저장되어있는 폴더로 들어갑니다. (ex 폴더 안에 에너지 파일 예시가 있음.)

2. 아래 명령어를 실행.
```
mplot
```
2. fitting을 하기 위한 데이터 파일을 번호를 입력하여 줍니다.
3. plot된 그림을 확인하고 출력된 결과를 POSCAR에 이용합니다.

* make surface for MD
1. 평면 구조를 만드려는 bulk 구조가있는 폴더로 이동.

2. 아래 명령어를 실행.
```
surface -in=./POSCAR
```
** 옵션

3. 결과 확인


* ~~mscp~~ (현재 사용할 수 없음)

~~scp를 할때 코드를 줄여준다.~~

~~scp해서 파일이 도착할 지점에서 다음 코드를 입력~~
```
mscp
```
~~slurm에서 파일의 주소를 입력한다. (pwd 사용)~~



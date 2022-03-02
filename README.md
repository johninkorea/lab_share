# Lab_share

## 소개

그룹원들과 프로그램을 공유하기 위해 만든 repository.


## 접근 & 권한
  다음 파일에 접근해야합니다.
* .bashrc

home에 다음 폴더를 만들어야 합니다.
* .rws


## 설치 방법
본 git repositories를 ***반드시*** 본인 ubuntu의 ***home*** 디렉토리에 clone 해야합니다.

home에서 아래 코드를 실행
```
git clone https://github.com/johninkorea/lab_share.git
```
해당 폴더 안으로 들어갑니다.
```
cd lab_share
```
setup.py를 실행해 줍니다.
```
python setup.py
```
터미널을 다시 시작합니다.

(설치후 clone 한 폴더는 삭제해도 됌)


## 사용 방법
* murnaghan
1. 에너지 데이터가 저장되어있는 폴더에서 아래 명어를 실행합니다.
  (ex 폴더 안에 에너지 파일 예시가있음.)
```
mplot
```
2. murnaghan fitting을 하기 위한 데이터 파일을 번호를 입력하여 줍니다.
3. plot된 그림을 확인하고 출력된 결과를 POSCAR에 이용합니다.


* mscp

scp를 할때 코드를 줄여준다.

scp해서 파일이 도착할 지점에서 다음 코드를 입력
```
mscp
```
slurm에서 파일의 주소를 입력한다. (pwd 사용)



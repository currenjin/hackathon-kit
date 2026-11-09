# 참가 방식과 본인 역할

공유 `hackathon.yaml`에는 `participation.mode`만 `individual / team / unknown`으로 저장한다. 팀의 각 응답자는 `members/<member-id>.yaml`에 본인의 주 역할과 확인 출처·시각을 기록한다. 역할은 작업 우선순위이며 담당 범위를 독점하거나 다른 역할 기여를 막지 않는다.

## 질문 화면

Claude에서는 `AskUserQuestion`, Codex에서는 현재 모드에 노출되고 호출 가능한 `request_user_input`을 사용한다. 참가 방식 응답을 받은 뒤 팀일 때만 역할을 묻는다. 도구가 없거나 현재 모드에서 사용할 수 없으면 제한을 짧게 알리고 같은 문구·선택지를 대화형으로 질문하며, 그 답변의 자유 서술도 받는다.

- 참가 방식: **이번 해커톤은 어떻게 참가하나요?** 선택지는 `개인` / `팀`, 단일 선택이다.
- 주 역할: **이번 팀에서 주로 맡을 역할은 무엇인가요?** 고정 선택지는 `프론트엔드 개발` / `백엔드 개발`이며 같은 질문의 native Other 자유 입력을 직접 입력으로 취급한다.
- `직접 입력`이라는 더미 선택지나 중복 Other를 추가하지 않고, 선택 후 별도의 역할 입력 질문도 만들지 않는다. host가 Other 라벨을 고정하면 사용자 정의 라벨을 강제할 수 있다고 설명하지 않는다.

Codex 선택지는 2–3개 범위를 지키고 host가 자동 추가하는 Other를 직접 넣지 않는다. 실제 회원 목록이 많으면 host 선택지 한도에 맞춰 페이지를 나누되, 기록 선택 질문에는 실제 `<member-id> (<main-role>)` 라벨과 `내 기록이 없어요`를 유지한다. 한도 때문에 필요한 다음 페이지 선택은 탐색용으로만 처리하고 회원으로 저장하지 않는다(예: 실제 기록 1개 + 내 기록이 없어요 + 다음 페이지).

취소·빈 응답·불명확한 선택은 답변이나 동의가 아니다. 역할 질문에서 native Other 또는 같은 응답의 자유 서술로 구체적인 역할을 답하면 그대로 사용하고, 모호한 “기타”만 있으면 확인한다. 모드 전환·전역 설정 변경·자동 선택으로 질문을 우회하지 않는다.

## 본인 확인과 세션

신규 등록 ID는 응답자가 본인 것이라고 확인한 비민감 GitHub handle을 소문자로 쓰거나, 인증 login을 쓸 수 없을 때 사용자가 명시 확인한 안전한 별칭을 사용한다. 인증 계정은 후보일 뿐 응답자라고 가정하지 않으며 git 이름·이메일을 ID로 쓰지 않는다. ID는 소문자 영문·숫자·단일 하이픈으로 1–39자, 시작과 끝은 영문·숫자이며 기존 ID와 대소문자만 다른 이름도 금지한다.

기존 기록을 본인 것으로 직접 선택한 응답은 그 ID의 의도적인 확인이다. 새 세션에는 `/onboard`에서 다시 선택하고, 같은 세션에도 사람이 바뀌거나 행사·URL·날짜가 달라지면 본인 선택을 다시 받는다. 현재 `(workspace, event.url, event.date, member-id)` 연결은 세션 안에서만 유지하며 공유 `current_member`나 포인터 파일을 만들지 않는다.

팀 행사의 매 command 시작에 현재 행사와 본인 연결을 확인하고 `members/<member-id>.yaml` 정본을 다시 읽는다. 연결이 없거나 오래됐거나 모호하면 추측하지 않고 `/onboard`의 본인 선택 절차를 적용하며, 역할 확인을 기다리는 동안 허용된 읽기 전용 브리핑은 계속할 수 있다. 정본이 없거나 ID가 일치하지 않으면 역할을 적용하지 않고 확인한다.

전체 제품 목표·공유 명세·통합 지점을 함께 읽고 본인 역할을 우선해 작업 순서를 정한다. 다른 역할 작업을 수행해도 저장된 주 역할을 자동 변경하지 않는다. 역할 수정은 본인의 명시적 요청·승인 때만 가능하며 다른 회원 파일을 고치지 않는다.

## 기존 행사와 읽기 전용 범위

`participation.mode` 누락·null·알 수 없는 값은 unknown이며 개인이나 팀으로 추론하지 않는다. 현재 행사의 작업에 필요하면 참가 방식 질문으로 확인하되 일괄 migration은 하지 않는다. `/onboard`의 읽기 전용 브리핑은 미확인 상태에서도 가능하며, mode 저장이 필요하면 현재 행사 `/init` 갱신 범위로 안내한다.

개인은 역할 질문·회원 등록을 건너뛰고 기존 흐름을 유지한다. 행사와 무관한 문서 작업에는 행사 선택이나 역할 등록을 새로 강제하지 않는다. 종료된 행사의 읽기 전용 열람에서는 등록 질문·회원 쓰기·세션 본인 연결 변경을 하지 않는다. `/onboard`의 쓰기 예외는 확인된 team 행사에서 응답자가 승인한 신규 본인 등록뿐이며 기존 기록 선택은 공유 행사·회원·evidence를 다시 쓰지 않는다.

## 실행 환경

팀 회원 저장 CLI는 macOS와 Linux에서 실행한다. Windows에서는 **WSL의 Linux 환경이 필요**하며 native Windows Python·PowerShell·Git Bash만으로는 이 CLI를 사용할 수 없다. 안전한 잠금과 no-follow 경로 검사를 생략해서 우회하지 않는다. Codex·Claude 자체가 native Windows에서 동작하는지와 이 저장 도구의 지원 범위는 별개다.

Windows 사용자는 PowerShell에서 `wsl --list --verbose`로 설치 상태를 확인한다. WSL이 없다면 [Microsoft 설치 안내](https://learn.microsoft.com/en-us/windows/wsl/install)를 보고 사용자가 설치·재시작을 승인한 뒤 준비한다. agent는 WSL이나 전역 설정을 자동 설치·변경하지 않는다. WSL 안에 Git과 Python 3가 준비된 뒤 아래처럼 **Linux 홈에 팀 저장소를 clone**하고 그 환경에서 kit을 연다. URL과 행사 경로는 실제 팀 값으로 바꾼다.

```sh
# WSL의 Linux 터미널에서 실행하는 예시
mkdir -p ~/work
cd ~/work
git clone https://github.com/your-org/your-team-kit.git team-kit
cd team-kit
python3 -B tools/member_records.py workspace/example-event list
```

이미 native Windows에서 kit을 열었다면 회원 CLI를 실행하기 전에 이 전제조건을 알리고 WSL 환경으로 안내한다. 실패한 등록을 완료로 표시하거나 다른 사람의 파일을 직접 편집하는 대체 경로는 사용하지 않는다. 개인 참가의 기존 흐름에는 이 회원 도구를 필수로 실행하지 않는다. 이 저장소의 macOS 테스트는 실제 Windows·WSL 실행 검증이 아니다.

## 등록·읽기·수정 실행

`/init`과 `/onboard`는 팀 역할 응답과 본인 확인 후 아래 CLI로 등록한다. [member_records.py](../tools/member_records.py)는 Python 표준 라이브러리로 동작하고 POSIX 파일 descriptor와 no-follow 열기로 symlink 경로를 거부한다. 다음의 행사 경로·ID·역할은 합성 예시이므로 실제 확인값으로 바꾸고 인수는 안전하게 인용한다.

```sh
python3 -B tools/member_records.py workspace/example-event list
python3 -B tools/member_records.py workspace/example-event register --member alice --identity alice --role '프론트엔드 개발' --identity-source github-confirmed --role-source native-choice --confirmed
python3 -B tools/member_records.py workspace/example-event read --member alice --identity alice
python3 -B tools/member_records.py workspace/example-event update --member alice --identity alice --role '백엔드 개발' --expected-role '프론트엔드 개발' --role-source native-choice --confirmed
```

`list`는 실제 기록만 반환하며 디렉터리가 없으면 빈 목록을 반환한다. 등록 전에도 이 목록을 읽고 본인 기존 기록이 있으면 새로 쓰지 않고 선택 경로로 돌아간다. `read`는 세션에서 확인된 ID를 `--member`와 `--identity`에 전달해 정본을 읽으며 파일을 변경하지 않는다.

`--confirmed`는 실제 응답·수정 승인 뒤에만 붙인다. 안전한 별칭은 `--identity-source safe-alias-confirmed`, native 자유 입력은 `--role-source native-freeform`, 도구 없는 대화형 답변은 `--role-source conversation`으로 남긴다. 취소·빈 답변이면 쓰기 CLI를 호출하지 않는다.

회원 파일은 JSON 문법의 YAML 부분집합으로 생성하며 `member_id`, `author`, `main_role`, `identity_source`, `role_source`, `confirmed_at`, `history`를 가진다. 수동 YAML 재포맷은 이 CLI가 지원하지 않으므로 생성 형식을 유지한다. 등록은 임시 파일 직렬화가 끝난 뒤 기존 대상을 덮어쓰지 않는 원자적 링크로 게시한다. 생성은 기존 파일·대소문자 충돌을 거부하고 수정은 이전 역할 일치 확인과 이력 보존 후 해당 회원 파일만 교체한다.

게시 직후 프로세스가 종료되어 `.member-*` 임시 별칭이 남아도 완전한 정본은 읽을 수 있다. 같은 회원 디렉터리의 생성된 별칭들이 정본과 같은 inode이고 모든 추가 링크가 그 안에서 확인되는 경우만 허용하며, 외부 hard link는 거부한다. 읽기·목록은 남은 별칭을 삭제하거나 기록을 변경하지 않는다. 이는 프로세스 종료 후 읽기 보존이며 전원 장애 내구성을 보장한다는 뜻은 아니다.

CLI는 본인 인증 서비스가 아니며 행사 참가 방식·종료 여부·작업 승인은 command가 먼저 검사한다. 역할 답변을 임의 코드나 셸 명령으로 해석하지 않는다. 오류가 나면 파일 직접 덮어쓰기로 우회하지 말고 해당 등록·수정을 멈춰 원인을 보고한다.

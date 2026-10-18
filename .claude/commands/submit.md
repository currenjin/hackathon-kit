---
description: 실제 제출 폼의 요구사항에 맞춰 검증 가능한 제출 문구와 링크를 만든다
---

> 추천 모델: [model-routing](../../references/model-routing.md)에서 이 command의 주도·검토 모델을 확인한다. 지금 세션이 추천 모델이 아니면 한 줄로 알리고 그대로 이어서 진행한다.

## 종료 게시 절차

종료 시 사용자 재승인 없이 상시 승인된 이번 command의 검증된 변경만 게시한다. kit 기록과 제품 repo를 분리하고 각 저장소의 명시 경로·hunk만 stage한 뒤 staged diff를 검수해 commit·push한다(`git add .`/`-A` 금지). 기존 index와 다른 스레드 작업, secret·개인정보·개인사진·권한 없는 원본·생성 캐시는 제외하며 분리할 수 없으면 보류한다. 변경이 없으면 빈 commit을 만들지 않는다. 제한·충돌·실패 시 변경을 보존하고 게시 대기 범위와 이유를 보고한다. 대상 remote branch SHA를 readback해 로컬 commit SHA와 대조하고 종료 보고에 저장소별 SHA·push 상태를 포함한다. tag, reset, force push, branch 생성·삭제, 공개 전환과 앱 복원은 별도 승인이 필요하다. 이 절차는 구현·외부 제출이나 다음 command 실행의 포괄 승인이 아니다.

## 실행 표시

흐름 첫 줄은 Markdown 인용문(`> `)으로 표시하고 코드 블록이나 인라인 코드로 감싸지 않는다. 실제 완료된 command만 굵게, 진행 중과 이후 command는 일반체로 쓴다. 아래는 형식 예시이며 실제 완료 여부는 행사 근거로 확인한다.

> **/init** → **/ideate** → /design (진행 중) → /demo


시작·중간 보고·종료 응답의 첫 줄은 command 단독이 아니라 준비 흐름 breadcrumb로 쓴다. 아래 시작/종료의 단독 command 템플릿은 breadcrumb로 대체하고 행사·범위·산출물·남은 조건은 그 뒤 또는 다음 줄에 보존한다.

전체 행사 흐름: [workflow 계약](../../references/workflow-policy.md)의 prebuild-permitted / on-site-build-only / restricted-preparation 분기를 따른다. /demo criteria → 제작 → /demo verify 순서이며 /replan 내부 init+ideate 조사만 자동실행금지의 명시적 예외다. 현재 사용자의 게시 금지·보호 경로는 종료 게시 절차보다 우선한다.

- 현재 단계와 앞뒤 단계를 포함한 연속 구간을 읽기 좋게 발췌한다. 양 끝에서는 가능한 이웃을 포함한다. 순서는 위치 안내이지 자동 다음 단계 실행 승인이 아니다.
- 굵게는 해당 행사·모드의 실제 완료 근거가 확인된 command에만 쓴다. 현재 단계에는 `(진행 중/선택 대기/초안/부분완료/실패/완료)` 등 실제 상태를 붙인다. 미래 단계는 일반체, unknown·기록 부재·근거 충돌은 `(미확인)`이다. 앞 단계라는 이유나 파일 존재만으로 완료를 추정하지 않는다. N/A는 공식 근거와 적용 이유가 확인된 경우에만 일반체로 표시한다.
- 조건부 예시: init과 ideate의 완료를 실제 확인한 경우에만 `**/init** → **/ideate** → /design (진행 중) → /demo(pre-event)`로 표시한다. 확인 전에는 `/init (미확인) → /ideate (미확인) → /design (진행 중) → /demo(pre-event)`다.
- slash 입력이 없는 자연어 요청도 실제 수행 내용과 입력/산출물 계약으로 단계를 매핑한다. 불명확하면 확인된 구간 또는 전체 흐름 뒤에 `| 현재 단계 확정못함 (미확인)`을 붙이고 확인 질문 후 대기한다. 표시를 생략하거나 임의의 현재 단계를 고르지 않는다.
- 아래 command별 완료 기준을 유지한다. 문서 초안만으로 /design·/prepare를 완료 또는 굵게 표시하지 않는다. 검토완료와 제품 PASS, 초안과 실제 제출은 구분하며 남은 조건과 실제 verdict를 숨기지 않는다.

“다음 작업 진행해줘” 같은 자연어 요청도 최신 대화와 현재 파일을 확인한다. 아래 개별 시작/종료 표시는 breadcrumb 뒤에 둘 부가정보와 상태 기준이며 첫 줄의 흐름을 대체하지 않는다. 미확정 상태도 위 breadcrumb 규칙으로 표시하고, 확인할 수 없으면 질문하고 대기로 종료한다. 단계를 지어내거나 완료로 승격하지 않는다. 표시만으로 작업 승인이나 다음 단계 실행 권한이 생기지 않는다. 흐름 breadcrumb를 생략한 응답·보고는 완료로 처리하지 않으며, 자연어 요청도 매핑을 생략하지 않는다.

`AGENTS.md`의 현재 해커톤 workspace 선택과 Command 입출력, Demo 계약을 따른다. 시작에 `/submit · 시작 | 행사 slug(미확정이면 행사 미확정) | 이번 작업 범위`, 종료에 `/submit · 실제 상태 | 행사 slug | draft/접수 근거 또는 없음 | 남은 검증/사용자 제출/다음 단계`를 표시한다. 기본 종료상태는 초안 작성 / 실제 제출 대기다. 사용자 제출의 접수 근거까지 확인한 경우에만 제출 확인을 덧붙인다. 일부만 마쳤으면 부분완료, 입력·승인 부족이면 대기, 작업 실패면 실패다. 문서 작성만으로 제출·공개·제품 구현 완료를 주장하지 않는다. 질문으로 멈출 때도 종료를 표시하며 도구 호출마다 반복하지 않는다. 다음 command는 안내만 하고 승인 없이 자동 실행하지 않는다.

현재 행사 workspace와 공식 제출 페이지를 읽고 submission draft를 만든다. build_policy의 submission 사전 작성 허용을 개별 확인한다. 금지·unknown이면 사전 작성하지 않는다. 최신 신규 출품물의 자격이 확인된 실제 evidence만 결과로 쓰며 과거/연습용 evidence로 대체하지 않는다.

순서는 draft → final `/preflight` → 실제 제출이다. 실제 제출은 사용자가 한다.

기본 형식을 먼저 정해 놓고 내용을 끼워 맞추지 않는다. 실제 제출 폼의 필드, character limit, 필수 링크를 먼저 확인한다.

## 1. 요구사항 수집

확인한다.

- project title
- one-line / tagline
- description
- problem
- how it works
- technologies / sponsor usage
- challenges
- accomplishments
- repository
- demo
- video
- slides
- cover image / thumbnail. 칸이 있으면 [model-routing](../../references/model-routing.md)의 시각 자산 행대로 GPT 이미지 생성 프롬프트를 만든다. 프롬프트에는 카피 원문, 실제 수치, 색, 참고할 실제 제품 렌더 경로, 쓰지 말 것을 넣고, 결과의 글자·숫자를 사실과 대조한다.
- team
- character limit
- 공개 범위
- 마감 시간과 timezone. `hackathon.yaml`의 `submission.deadline`과 공식 제출 페이지를 대조한다.

필드가 없으면 만들지 않는다. hosted app만 있는 제품에 저장소를 임의로 만들거나 URL을 지어내지 않는다. 공식 폼에서 repository가 필수라면 남은 제출 조건으로 알린다.

## 2. Source

아래에서만 사실을 가져온다.

- `hackathon.yaml`
- demo contract
- 실제 제품
- 실제 실행 evidence
- deck
- 공개 repository와 guide

결과와 수치는 demo contract의 PASS scenario에서만 가져온다. ORACLE INVALID, UNVERIFIED scenario는 성과로 쓰지 않는다. sponsor는 `AGENTS.md`의 Sponsor 사용 조건에 따라 채택 결정과 실제 사용 evidence를 모두 확인한다. `used: false`는 명시적 제외, null·누락·기존 의미 충돌은 미정이며 N/A가 아니다. `used: true`만으로 사용 실적을 쓰지 않는다. 제외·미검증 사용은 성과에서 빼되 required 실패·judged 영향은 숨기지 않는다.

서로 다른 숫자나 설명이 있으면 submission을 쓰기 전에 해결한다.

## 공통 사실과 증거 인계

[자료와 실행 기록 인계](../../references/delivery-handoffs.md)에 따라 기존 사실표와 기준별 증거를 읽고 실제 제출 필드에 필요한 claim만 사용한다. 별도 사실 원본을 만들지 않는다. 기록이 없으면 기존 명세·contract·실행 evidence를 연결한 최소 사실표를 남기고 경로를 인계한다. 공식 폼·원문·실제 결과가 우선하며 일치하지 않는 claim은 해결 전 성과에서 제외한다. 제작 이력과 starter 상속·실제 구현을 구분하고 인용한 자료 버전을 기록한다. 이미 제출한 문구와 접수 이력은 보존하며 사실표 갱신으로 과거 제출을 바꾸지 않는다.

## 3. 작성

짧은 필드는 먼저 결론을 쓴다.

sponsor usage는 폼에 필드가 있고 실제로 쓴 sponsor만 적는다. "used X"로 끝내지 않는다.

- 어디서 호출되는가
- 제품에서 어떤 역할인가
- 없으면 어떤 부분이 성립하지 않는가

차별점은 경쟁 도구의 이름만 나열하지 않고 동작 차이를 설명한다.

## 4. 언어

`hackathon.yaml`의 submission 언어를 따른다.

여러 언어가 필요하면 각 언어에서 자연스럽게 다시 작성한다. 한 언어의 문장 구조를 그대로 옮기지 않는다.

## 5. 링크 검증

제출 전 실제로 연다.

- repository
- demo
- video
- slides
- public guide

로그인하지 않은 상태에서 열려야 하는 링크는 public access를 확인한다.

## 6. 출력

`workspace/<event-slug>/output/submission/`에 draft로 저장한다. 미제출이면 `submission.status`를 `draft`로 두되 이미 submitted인 사실은 되돌리지 않고 수정 초안·정정 필요를 별도로 기록한다.

가능하면 실제 제출 필드 이름과 같은 heading을 사용한다. 복사해서 바로 제출할 수 있는 상태로 만든다.

사용자가 제출 완료를 보고했지만 접수 화면·메일·레코드에 접근하지 못하면 `submission.status: submitted_user_confirmed`로 기록한다. 직접 접수 근거를 확인하면 `submitted`로 기록하며 보고와 직접 검증을 구분한다. 완료 보고도 근거도 없을 때만 draft를 유지하고, 과거 submitted 사실이나 원래 draft는 지우지 않는다. 제출 시각 또는 시각 미확인, 근거, 실제 제출 문구·당시 build를 연결한다. [상태 계약](../../references/field-status-and-closeout.md#확인-출처와-제출-상태)에 따라 수정 초안과 접수 실패·미접근도 분리한다. 실제로 공개·접수 확인된 URL만 public_links에 기록하며 사용자 보고인지 직접 확인인지 근거를 함께 남긴다.

---
description: 행사 workspace를 초기화하거나 같은 행사의 공식 조건을 재확인·갱신한다
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

`AGENTS.md`의 현재 해커톤 workspace 선택과 Command 입출력, 사전 제작·작업 승인 경계를 따른다. 시작에 `/init · 시작 | 행사 slug(미확정이면 행사 미확정) | 이번 작업 범위`, 종료에 `/init · 실제 상태 | 행사 slug | 산출물 또는 없음 | 남은 확인/다음 단계`를 표시한다. 상태는 행사 기록을 마쳤으면 완료, 일부만 마쳤으면 부분완료, 입력·승인 부족이면 대기, 작업 실패면 실패로 쓴다. 질문으로 멈출 때도 종료를 표시하며 도구 호출마다 반복하지 않는다. 다음 command는 안내만 하고 승인 없이 자동 실행하지 않는다.

현재 행사 정보를 조사하고 `workspace/<event-slug>/`를 만든다.

## Event slug

`YYYY-<event-name>` 형태의 짧고 안정된 slug를 쓴다.

예:
`2026-daytona-hacksprint-seoul`

같은 이름의 다른 회차나 도시가 있으면 월이나 도시를 붙여 구분한다.

같은 slug 폴더가 이미 있으면 `hackathon.yaml`의 `event.url`, `event.date`를 비교한다. 일반 초기화는 같은 행사의 빈 항목만 채운다. 재확인 모드(직접 요청 또는 승인된 `/replan` 내부)는 빈칸만 채우는 규칙의 예외다. URL·날짜가 같은 현재 workspace를 유지하고 실제 확인된 변경값·이전값·출처·확인 시각·변경 이유를 notes/기존 sources에 보존하며 갱신한다. 미확인 새 값으로 기존 확인값을 덮지 않는다. 행사 식별 자체가 달라지면 확인 전 새 폴더나 행사로 전환하지 않는다. 다른 행사와 종료된 기록은 수정하지 않는다.

## 레퍼런스의 적용 범위

[조건부 스타터 목록](../../references/starter-references.md)은 공식 행사 규칙을 대신하지 않는다. sponsor의 공식 문서·인증·quota·발급 시점 조사 결과는 후속 /prepare가 [최초 호출 안내](../../references/delivery-handoffs.md)를 작성할 수 있게 현재 workspace에 출처와 확인 범위를 남긴다. 조사만으로 sponsor 채택·도구 설치·호출·제품 제작을 승인하지 않는다.

## 조사

1. 공식 event page와 rules를 우선한다.
   사전 제작·기존 제품·외부 코드/API 허용 범위를 원문으로 확인한다. `build_policy`에 모드, 공식 제작 시간·출처와 planning/design/prompt/data/criteria/code/deck/pitch/submission의 개별 사전 허용 여부를 기록한다. 모르면 unknown/null이며 허용 추론은 금지한다. 코드 재사용 자격은 별도로 확인한다. `/init`은 계정·앱·저장소 생성이나 제품 구현을 승인하지 않는다.
2. 새 공식 트랙, 필수·금지 기술, 심사 기준, sponsor, 사용 조건, hacking 시간, submission 마감, pitch 시간을 확인한다. 모든 관련 탭·첨부를 직접 읽고 접근 불가 범위는 남긴다. rules/출처 미확인이면 부분완료로 기록하되 가능한 비차단 조사는 수행한다.
   발표시간은 [발표 레퍼런스 가이드](../../references/presentation-reference-guide.md)의 공통 해석 규칙을 따른다. 공식 시간은 기존 `event.pitch_minutes`에만 기록하고 미확인은 `null`로 유지한다. 공식 미확인이라도 출처 있는 사용자 확인 시간·범위와 준비 목표가 있으면 보존한다. 공식값과 사용자 확인 시간이 모두 없을 때만 `presentation.effective_seconds: 60`, `source: user-default`, `timing_status: provisional`로 준비한다. 공식 확인 시 분을 초로 환산해 유효시간을 갱신하고 source에 공식 근거를 남긴다. Q&A 합산/별도/없음을 `qa_mode`에, 확인된 배정을 `qa_seconds`에 기록하며 모르면 `unknown`/`null`이다. 공식 또는 사용자 확인으로 Q&A가 없으면 `none`/`0`을 쓰고 notes에 출처를 official/user-confirmed로 구분한다. 새 행사는 확인 전 `unknown`/`null`을 유지한다. 원문·확인일·시간 범위는 notes에 남기고 발표 상태는 `pending`이다. 기존 행사 조건이 달라지면 `/adapt` 변경 경로를 안내하며 기존 workspace를 일괄 migration하지 않는다.
3. submission 마감은 timezone offset까지 적고 확인한 공식 링크를 `submission.source`에 남긴다. 행사 timezone은 `event.timezone`에 적는다.
4. sponsor 사용이 참가·수상 자격이나 심사 기준에 들어가는지 확인해 `sponsor_requirement`에 근거와 함께 적는다. sponsor별 요건이 다르면 `sponsors[].requirement`와 `requirement_source`를 적는다. 기준은 `AGENTS.md`의 Sponsor 사용 조건을 따른다.
5. sponsor마다 공식 문서에서 auth, pricing, quota, SDK/API, credential 발급 시점을 확인한다. 행사 기본값이 `none`이어도 개별 요건과 채택 결정을 먼저 확인한다. 미정 sponsor의 `used`는 null로 두며, 미정·unknown을 제외나 N/A로 보지 않는다.
6. 발표 언어와 청중 언어를 정한다.
7. `templates/hackathon.yaml`을 바탕으로 `workspace/<event-slug>/hackathon.yaml`을 채운다.
8. 아직 제품을 고르지 않는다. demo contract도 만들지 않는다.

정보가 없으면 지어내지 말고 확인할 항목으로 남긴다.

`templates/`, `products.md`, `references/`는 수정하지 않는다.

secret과 API key는 workspace에 적지 않는다.

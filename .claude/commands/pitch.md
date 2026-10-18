---
description: deck과 live demo를 제한 시간 안에 전달할 수 있는 실제 발표 대본으로 만든다
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

`AGENTS.md`의 현재 해커톤 workspace 선택과 Command 입출력, Demo 계약을 따른다. 시작에 `/pitch · 시작 | 행사 slug(미확정이면 행사 미확정) | 이번 작업 범위`, 종료에 `/pitch · 실제 상태 | 행사 slug | 대본/guide 또는 없음 | 남은 리허설/승인/다음 단계`를 표시한다. 본문의 산출물과 실제 리허설 조건까지 충족해야 완료다. 문서만 작성했으면 초안 작성, 일부만 마쳤으면 부분완료, 입력·승인 부족이면 대기, 작업 실패면 실패다. guide 작성은 공개가 아니며 문서 작성은 제품 구현 완료가 아니다. 질문으로 멈출 때도 종료를 표시하며 도구 호출마다 반복하지 않는다. 다음 command는 안내만 하고 승인 없이 자동 실행하지 않는다.

현재 행사 workspace의 `hackathon.yaml` 언어 설정, deck, demo contract, 실제 제품 결과를 읽고 presenter 언어로 발표 대본과 설정된 언어의 public guide를 만든다. sponsor 주장은 `AGENTS.md`의 Sponsor 사용 조건에 따라 채택 결정과 실제 사용 evidence를 모두 확인한다. 미정은 제외나 N/A로 보지 않는다.

목표는 deck의 문장을 읽는 대본이 아니다. 심사위원이 제품을 이해하는 순서와 실제 화면 전환을 맞추는 것이다. build_policy의 pitch 사전 작성 허용을 개별 확인하고 public guide·prompt·데이터 등도 해당 행위 허용을 확인한다. 금지·unknown이면 사전 작성하지 않는다. 최신 신규 출품물의 자격이 확인된 실제 evidence만 결과로 쓰며 과거/연습용 evidence로 대체하지 않는다.

핵심 demo 장면과 deck이 잡히고 위 필수 입력이 갖춰지면 행사 전에도 pitch 초안을 작성할 수 있다. 필수 입력이 없으면 멈추고 이를 만드는 작업부터 제안한다. 초안은 필수 입력·guide 산출물·실제 리허설 등 완료 계약의 예외가 아니다. 실제 미검증 결과는 evidence 대기 자리 또는 한계로 구분하고 말할 성과나 수치를 만들어 넣지 않는다. local/mock 결과를 현장·실제 sponsor 결과로 말하지 않는다. 다음 작업으로 현장 evidence 갱신이나 실제 리허설의 가능한 시점과 필요한 조건을 선제 제안하되 자동 실행하지 않는다.

## 공통 사실과 증거 인계

[자료와 실행 기록 인계](../../references/delivery-handoffs.md)에 따라 /deck이 연결한 기존 사실표와 기준별 증거를 읽는다. 별도 사실 원본을 복제하지 않고 원문·실행 evidence와 현재 build를 대조한다. 없으면 기존 기록에서 필요한 사실을 연결하고 채택 경로를 남긴다. 각 발화·화면 cue·guide가 어떤 claim과 기준을 쓰는지 기록하며 언어별 수치·한계·local/mock 범위를 일치시킨다. 근거 충돌·미검증은 성과에서 제외하고 기존 자료와 불일치하면 영향받는 버전과 재검수 대기를 기록한다.

## 1. 발표 조건

[발표 레퍼런스 가이드](../../references/presentation-reference-guide.md)의 공통 시간 해석을 `/deck`과 동일하게 쓴다. 공식 `event.pitch_minutes`가 확인되면 초로 환산한 `presentation.effective_seconds`와 공식 source를 사용한다. 공식 미확인은 null을 유지한다. 출처 있는 사용자 확인 시간·범위와 준비 목표가 있으면 보존하고, 둘 다 없을 때만60초/user-default/provisional로 준비한다. 필드 누락은 같은 규칙으로 읽고 migration하지 않는다. deck과 유효시간·출처·Q&A 조건이 다르면 `/adapt` 기록과 재작업부터 안내한다. Q&A unknown을 별도로 가정하지 않는다. 포함 슬롯은 확인된 Q&A 배정까지 유효시간 안에 두며 배정 미확인은 RISK다.

먼저 확인한다.

- 총 발표 시간
- Q&A 포함 여부
- live demo 시간
- presenter 언어
- 청중 언어
- 반드시 보여줄 slide / 화면
- 가장 강한 evidence
- demo 실패 시 fallback

확인된 공식 심사 기준별로 deck의 evidence와 이를 보여줄 demo 장면·발화/cue를 연결한다. 근거가 없으면 대기 자리 또는 한계로 남기고, rubric이 unknown이면 미확인으로 표시하며 심사 기준을 발명하지 않는다.

## 2. 시간 예산

전체 시간을 구간별로 먼저 배분한다.

문제 설명이 길어져 제품과 evidence 시간이 사라지지 않게 한다. 준비 기본 60초의 제안은 문제 8초, 핵심 변화/데모 32초, 차별/기술 12초, 마무리 3초, 전환/여유 5초다. 공식 시간이 확인되면 그 시간으로 다시 배분한다. 동시 발화·demo는 중복 합산하지 않고 loading·전환·여유를 포함한 실제 총 경과시간을 계산한다. 시간 증가를 임의의 내용 채우기로 처리하지 않고, 감소 시 핵심 전후 결과를 보존하며 부차 정보를 삭제한다. 독립 expected와 evidence는 바꾸지 않는다.

각 구간마다 적는다.

- 시작/종료 시간
- slide 또는 화면
- 말할 문장
- click / tab / scroll cue
- 실패 시 fallback cue

## 3. 문장

발표문은 글이 아니라 말이다.

- 한 문장에 한 메시지
- 소리 내어 읽기 쉬운 길이
- 비개발자가 모르는 용어는 처음 한 번만 설명
- 기술 설명은 화면에서 실제 일어나는 순서와 맞춤
- 쓰는 sponsor가 있으면 이름을 역할과 함께 말함
- 수치와 결과는 demo contract의 PASS scenario와 동일하게 유지
- ORACLE INVALID, UNVERIFIED scenario와 제외한 sponsor나 기능은 결과로 말하지 않음
- slide에 이미 보이는 문장을 그대로 읽지 않음

## 4. Demo

live demo는 "클릭한다" 수준이 아니라 실제 순서를 적는다.

예:
- 어느 tab을 연다
- 어떤 preset을 선택한다
- 어느 버튼을 누른다
- 어떤 결과가 뜰 때 다음 문장으로 넘어간다
- loading이 길면 무엇을 말한다
- failure 시 어느 screenshot으로 전환한다

## 5. Q&A

공식 또는 사용자 확인으로 Q&A가 없으면 `qa_mode: none`, `qa_seconds: 0`으로 기록하고 출처를 official/user-confirmed로 구분한다. 이 경우 Q&A 대본·시간 배정은 필수가 아니며 없음의 근거만 남긴다. 그 외에는 심사 기준, 차별점, sponsor 사용, 확장성, 한계에서 질문을 뽑되 unknown을 Q&A 존재 확정으로 보지 않는다.

각 답변은 확인된 Q&A 예산에 맞춘다. 20~30초는 연습용 길이 예시이지 별도 Q&A 시간이 있다는 가정이 아니다. 구현되지 않은 roadmap을 현재 기능처럼 말하지 않는다. 제외한 항목을 물으면 한계로 답한다.

## 6. Rehearsal

대본을 만든 뒤 실제로 시간을 잰다.

- 제한 시간을 넘으면 문장을 줄인다.
- 빠르게 말해서 맞추지 않는다.
- demo loading 시간을 포함한다.
- slide 전환과 tab 이동도 시간에 넣는다.

최소 두 번 연속 제한 시간 안에 들어오도록 조정한다.

실제 발화와 화면 조작으로 수행한 리허설의 수행자·일시·자료 버전·측정 초수·fallback 결과를 남긴다. 계산상 시간표나 자동 타이머 테스트는 실제 리허설이 아니다. 미실시는 미실시로 표시하고 완료를 주장하지 않는다. 조건 변경 후 deck·대본·demo cue·fallback 재검수 전에는 `presentation.status: dirty`를 유지한다. 최종 ready는 `/preflight final`의 시간·렌더·설득/시각 QA·리허설 확인 뒤에만 기록한다.

## 7. 출력

`workspace/<event-slug>/output/pitch/`에 저장한다.

새 iteration을 만들 때는 해당 iteration의 `report.md` 상단에 흐름 breadcrumb와 `presentation.review.status` 및 이전 iteration 처리(superseded or kept)를 명시하고 `hackathon.yaml`의 `presentation.review`를 갱신한다. 발표 기준 iteration은 하나만 active이며 승인 전은 `active_version: null`·`status: in_review`로 유지한다. 기존 workspace에 review 필드가 비어 있다고 임의로 채우지 않는다. 이 kit 기록 변경은 종료 게시 절차의 상시 승인으로 commit·push해 추적을 유지한다.

`language.public_guide`에 설정된 각 언어의 public guide는 `workspace/<event-slug>/output/guide/<lang>.md`에 작성한다. 내용은 `.claude/rules/language.md`를 따르고 deck·demo의 검증된 사실과 숫자를 유지한다. 발표자와 청중 언어가 다르면 대본보다 guide를 우선 작성한다. 작성은 공개·발송이 아니다. `public_links.guide`는 실제 공개 후 비로그인 접근을 확인한 URL만 기록한다.

최종 파일에는 아래를 포함한다.

- timed script
- screen cues
- demo fallback
- Q&A 또는 `none` 확인 근거
- 발표 직전 체크리스트

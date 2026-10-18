---
description: 끝난 해커톤의 링크를 reference 파일에 정리한다
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

`AGENTS.md`의 현재 해커톤 workspace 선택과 소유 경계, 종료 후 규칙을 따른다. 시작에 `/archive · 시작 | 사용자 확인한 행사 slug(미확정이면 행사 미확정) | 이번 작업 범위`, 종료에 `/archive · 실제 상태 | 행사 slug | 갱신한 기록 또는 없음 | 미확인 링크/다음 단계`를 표시한다. 완료는 확인된 링크 정리의 완료이지 새 공개·제출·제품 구현 완료가 아니다. 일부만 마쳤으면 부분완료, 입력·승인 부족이면 대기, 작업 실패면 실패다. 질문으로 멈출 때도 종료를 표시하며 도구 호출마다 반복하지 않는다. 다음 command는 안내만 하고 승인 없이 자동 실행하지 않는다.

현재 행사 workspace의 `hackathon.yaml`에 제출 또는 실제 공개가 확인된 demo·slides·guide URL만 `public_links`에 기록한다. 미확인 URL을 만들어 넣지 않는다. `public_links`가 없는 과거 workspace는 산출물이나 제출 확인 기록에서 찾되 확인할 수 없으면 비워 둔다.

사용자가 대상 행사를 확인한 뒤 그 workspace를 읽고 직접 참가한 행사 링크를 `references/my-hackathons.md`에 추가하거나 갱신한다.

이미 같은 이름의 항목이 있으면 event 링크와 날짜로 같은 행사인지 확인한다. 다른 회차면 별도 항목으로 추가한다.

## my-hackathons.md에 남길 것

- 행사 링크
- 프로젝트 repository
- demo
- slides
- presentation guide
- submission page
- 대응하는 workspace 링크

상세 회고, 심사 기준, sponsor 설정, 임시 작업 상태는 workspace에 이미 있으므로 reference에 반복하지 않는다.

## 행사 후 내리기

[현장 상태와 종료 점검](../../references/field-status-and-closeout.md)을 함께 읽는다. 현재와 과거 상태, 사용자 보고와 직접 확인을 구분한다. 필요한 경우 읽기 전용 `tools/workflow_checks.py`로 명시한 workspace와 검사 범위의 진단을 확인하되 결과를 제품 PASS로 쓰거나 과거 기록을 자동 수정하지 않는다.

행사가 끝나고 데모를 유지하지 않기로 하면 사용자 확인 후 아래를 한다. 되돌릴 수 없는 삭제는 따로 승인을 받는다.

- 제품 README와 kit `references/`의 우리 데모 링크에 취소선을 긋고 만료 이유를 적는다. 다른 참가자의 링크는 건드리지 않는다.
- 저장소 About의 웹사이트 칸을 영상 링크로 바꾸거나, 가리킬 곳이 없으면 비운다.
- 호스팅 앱을 내리고 실제 주소로 접속해 확인한다. 플랫폼별 방법이 `references/`에 있으면 그것을 따른다.
- 서버 비밀값을 지우고, 채팅 등에 노출된 적이 있는 키는 재발급을 안내한다.
- 공개 저장소에 최종작 외 이력이 남았으면 이력 재작성 여부를 사용자에게 묻는다. 진행하면 먼저 번들로 백업하고 SHA 대응표를 workspace에 남긴다.

## 다른 reference

- 확인된 수상작 링크는 `references/winners.md`
- 전체 project gallery와 일반 출품작 링크는 `references/submissions.md`

workspace와 reference의 역할을 섞지 않는다.

archive가 끝나도 workspace를 삭제하거나 이동하지 않는다. 과거 규칙·선택·제작 시각·evidence·oracle 격리·실제 제출 이력을 보존하며 새 정책으로 역사 기록을 일괄 migration하지 않는다. 보호 경로와 기존 dirty는 승인 없이 수정하지 않는다.

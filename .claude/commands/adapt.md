---
description: 발표 조건 변경을 반영하고 해당하는 sponsor credential과 실제 환경을 연결한다
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

`AGENTS.md`의 현재 해커톤 workspace 선택, 제품 위치와 복구 경계, Sponsor 사용 조건을 따른다. 시작에 `/adapt · 시작 | 행사 slug(미확정이면 행사 미확정) | 이번 작업 범위`, 종료에 `/adapt · 실제 상태 | 행사 slug | 연결 evidence/산출물 또는 없음 | 남은 승인/다음 단계`를 표시한다. 실제 연결·smoke test·E2E까지 확인해야 완료이며 문서 작성은 연결 완료가 아니다. 실제로 불필요하면 검토완료와 N/A 이유를 표시한다. 일부만 마쳤으면 부분완료, 입력·승인 부족이면 대기, 작업 실패면 실패다. 질문으로 멈출 때도 종료를 표시하며 도구 호출마다 반복하지 않는다. 다음 command는 안내만 하고 승인 없이 자동 실행하지 않는다.

현재 행사 workspace의 `hackathon.yaml`과 제품 연결 모드에서는 `preparation.md`를 읽는다. 아래 환경설정 전용 예외에서는 preparation.md가 없어도 가능하다.

이 단계는 제품 구현 단계가 아니다. 발표 조건을 확인·갱신하고, 연결 대상이 있으면 `/prepare`에서 만들어 둔 integration을 실제 sponsor 환경에 연결한다. 발표시간 확인은 sponsor 유무와 관계없이 수행하며 공식 안내가 행사 전에 나오면 현장까지 기다리지 않는다.

`AGENTS.md`의 Sponsor 사용 조건에 따라 `sponsors[].used: true`로 채택이 확인된 sponsor를 연결한다. null·누락·기존 의미 충돌은 미정이지 제외나 N/A가 아니다. 미정은 확인 항목으로 남긴다. 채택 대상이 없고 공식 요건상 연결이 실제로 불필요한 경우에만 연결 항목을 N/A로 기록한다. 발표 조건 확인까지 생략하거나 전체 adaptation을 자동 N/A 처리하지 않는다. required 미사용은 FAIL, judged 제외는 점수 영향을 기록한다.

## 전체 재계획이 필요한 변경

새 규칙이 사전 제작 허용, 기존 제품 출품 자격, 필수 기술·배포·제출물 또는 제품 방향·여러 단계의 완료 판정을 바꾸면 [`/replan`](replan.md)을 먼저 제안한다. `/adapt`의 연결·조건 수정만으로 전체 준비를 유효하다고 유지하지 않는다. 현재 확인한 금지와 안전상 보류는 기록하되 `/replan`이나 신규 구현을 사용자 승인 없이 자동 실행하지 않는다. 단순 발표시간·endpoint·계정 조건 갱신은 아래 `/adapt` 범위를 유지한다.

## 발표 조건 확인과 변경

[발표 레퍼런스 가이드](../../references/presentation-reference-guide.md)의 공통 해석 규칙을 적용한다. 공식 event.pitch_minutes 우선이며 미확인은 null이다. 출처 있는 사용자 확인 시간·범위와 목표를 보존하고 둘 다 없을 때만60초/user-default/provisional을 쓴다. 공식 source와 Q&A 합산/별도·배정 초수를 확인한다. 미확인을 별도로 가정하지 않는다.

1. 이전 유효시간·출처·Q&A 조건과 새 공식시간·출처·확인일·Q&A 조건을 `adaptation.md`에 기록한다. 공식 또는 사용자 확인으로 Q&A가 없으면 `qa_mode: none`, `qa_seconds: 0`을 쓰고 Q&A 출처를 official/user-confirmed로 구분한다. 사용자 확인을 공식 시간·규칙 확인으로 승격하지 않는다.
2. `hackathon.yaml`의 공식 시간과 `presentation` 유효시간·출처·timing_status·Q&A를 갱신한다. 시간/출처/Q&A 조건 변경 시 `presentation.status: dirty`로 두고 deck·pitch·demo cue·fallback의 영향과 재검수 대기를 적는다. 60초 기본값→공식 120초도 자료는 자동 완료가 아니다.
3. 승인 범위 안에서 `/deck` → `/pitch` 재작업 경로를 안내한다. 승인 없는 전체 재생성은 하지 않는다. 시간 증가 시 임의 내용을 채우지 않고, 감소 시 핵심 전후 결과를 보존하며 부차 정보를 삭제한다. 독립 expected와 실행 evidence는 변경하지 않는다.
4. deck·대본·cue·fallback의 시간 일치, 전체 렌더와 설득/시각 QA, 실제 리허설을 다시 확인하도록 `/preflight final`을 안내한다. 조건 기록 완료, adaptation 완료, 발표 준비 완료를 구분한다. 연결이 해당하면 기존 smoke/E2E 완료 기준도 그대로 필요하다.

`preparation.md` 없는 조건부 예외: 발표 조건 기록 또는 구현 전 최초 계정 연결이 필요한 경우, 공식 규칙과 사용자 승인 범위 안에서 환경설정 점검만 수행한다. 입력은 hackathon.yaml·공식 계정/endpoint 문서·확인된 소유 권한이다. adaptation.md에 `환경설정 전용`, 목적·허용 출처·시각·설정 범위·실제 점검 결과·제품 미구현·E2E 미실시·prepare 재개 조건을 남긴다. 제품 코드·앱 수정이나 제품 smoke/E2E 완료 주장은 포함하지 않는다. 계정 생성·유료 호출·외부 전송은 별도 승인 경계를 유지한다. 제품 연결 모드에 preparation.md가 없으면 입력 대기다. 조건 기록 완료와 환경설정 점검 완료, 제품 연결 완료, presentation 완료를 구분하며 일괄 migration하지 않는다.

## 시작 전

아래 제품 보존·복구 확인은 제품 변경이 있을 때 적용한다. 발표 조건 기록만 하는 작업에 sponsor 연결을 강제하지 않으며 필수 입력 확인은 별도로 유지한다.

- `AGENTS.md`의 제품 위치와 복구 경계를 따른다. Git 제품은 branch·HEAD·working tree와 `preparation.md`의 준비 변경 범위를 비교한다.
- 준비 작업이 dirty였다면 HEAD만으로 복구하지 못한다. 이번 작업의 검증된 변경은 상시 승인 commit 등으로 보존하되 범위 밖 변경을 함께 commit하지 않는다. 미추적 파일까지 준비 상태 전체를 보존하고 복구 가능성을 확인하기 전에는 현장 수정을 시작하지 않는다. branch 분리만으로 준비 작업이 격리되지 않는다.
- Git 현장 수정은 보존이 확인된 준비 상태를 기준으로 사용자 승인 아래 분리된 branch에서 한다. 이번 command의 검증된 변경에 대한 일반 commit·push는 종료 게시 절차의 상시 승인을 적용한다. tag, reset, force push, branch 생성·삭제, 공개 전환과 앱 복원은 별도 승인 없이 하지 않는다.
- hosted app은 실제 앱 위치·소유 계정·권한과 준비 상태의 보존·복구 방법을 확인한 뒤 수정한다. 확인되지 않은 플랫폼 버전/복원 기능이나 Git commit을 기준점으로 적지 않는다. 복구 방법이 없거나 미확인이면 사용자와 방안을 정하고 보존을 확인할 때까지 수정을 보류한다.

## 연결

1. 행사에서 제공한 credential 또는 account를 확인한다.
2. 공식 endpoint와 region, credits/quota를 확인한다.
3. key, endpoint, model, account 같은 실제 값은 환경 변수나 secret store에 넣는다.
4. 준비해 둔 adapter를 실제 provider로 전환한다.
5. 가장 작은 smoke test를 실행한다.
6. 핵심 E2E를 한 번 실행한다.

필요한 코드 수정은 최소 범위로 제한한다.

## 실패했을 때

smoke test나 E2E가 실패하면 먼저 원인을 나눈다.

- credential, 권한, quota, region: 공식 문서나 sponsor 운영진으로 확인한다. 코드를 고치지 않는다.
- infra error(network, timeout, provider 장애): 재시도 횟수를 정하고 결과를 기록한다.
- adapter bug: 최소 범위로 고친다.
- product failure: `/prepare` 범위의 문제다. `/adapt` 안에서는 핵심 기능을 새로 만들지 않는다. 이는 adapt의 역할 제한이지 현장 신규 구현 금지가 아니다. 공식 제작 시간과 승인 범위 안의 현장 `/prepare`는 허용된다.

sponsor별 `sponsors[].requirement`(없으면 행사 기본값 `sponsor_requirement.level`)를 적용한다. feature freeze 전까지 복구하지 못하면:

- `optional` sponsor는 준비된 local 또는 대체 provider로 되돌리고, 그 sponsor를 demo, deck, pitch, submission 주장에서 뺀다.
- `required`나 `judged` sponsor는 자격 또는 점수 영향을 적고 계속할지 사용자가 정한다. 연결하지 못한 `required` sponsor는 final preflight에서 FAIL이다.
- 되돌려야 하면 보존된 준비 상태와의 변경을 보여주고 사용자 확인 뒤 복구한다. dirty 준비 작업이 빠진 HEAD로 되돌리지 않는다. hosted app 복원도 확인된 방법만 사용한다.

## 자료와 실행 안내 인계

[자료와 실행 기록 인계](../../references/delivery-handoffs.md)를 따른다. 기존 runbook의 채택 sponsor 최초 호출 안내를 읽고 실제 설정·호출 경로·결과·readback 근거 또는 미실행 이유를 adaptation.md에 연결한다. 안내·mock·실서비스·제품 E2E를 구분하며 계정 미지급과 환경설정 전용 예외를 성공으로 확대하지 않는다. 제품·설정·명칭·링크·시간 또는 검증 결과가 바뀌면 기존 사실표의 근거와 영향받는 deck/pitch/guide/submission 버전을 연결해 갱신·재검수 대기를 남긴다. 타 command 자동 실행·자료 전체 재생성·과거 제출 덮어쓰기는 하지 않는다.

## 기록

실제 연결 결과와 evidence, 실패 분류, fallback 여부, 남은 리스크는 `workspace/<event-slug>/adaptation.md`에 남기되 credential 자체는 적지 않는다. 제외 결정된 sponsor만 `hackathon.yaml`에 `used: false`와 이유를 적는다. 연결 실패만으로 채택 결정을 자동 변경하지 않는다. `used: true`도 실제 사용 성공의 증거가 아니다.

시간/Q&A/조건 변경으로 deck·pitch의 새 iteration이 생기면 해당 iteration `report.md` 상단과 `hackathon.yaml`의 `presentation.review`를 함께 갱신한다. 발표 기준은 하나만 active이며 승인 전은 `in_review`로 유지하고 superseded/kept를 명시한다.

`product.name` 변경이 발생하면 영향 범위(제품 저장소/화면/문서/덱/제출 폼/public_links 중 해당 항목)와 각 항목의 반영 상태를 `adaptation.md`와 종료 보고에 자동으로 남긴다. 저장소 이름 규칙은 `AGENTS.md`를 따르고 과거 행사의 일괄 rename은 하지 않는다.

---
description: 프로젝트에 맞는 demo scenario와 ground truth를 고정한다
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

`AGENTS.md`의 현재 해커톤 workspace 선택과 Demo 계약을 따른다. 시작에 `/demo <모드> · 시작 | 행사 slug(미확정이면 행사 미확정) | 이번 작업 범위`, 종료에 `/demo <모드> · 실제 상태 | 행사 slug | contract/evidence 또는 없음 | 실제 verdict·남은 승인/다음 단계`를 표시한다. 모드는 criteria 또는 verify이며 pre-event/on-site는 각각의 호환별칭이다. 불명확하면 모드 미확정으로 표시하고 질문 뒤 대기로 종료한다. criteria 완료는 독립 expected와 contract 고정이지 제품 PASS가 아니다. verify는 검토완료와 실제 verdict를 별도로 쓰고 미실행·UNVERIFIED·실패를 숨기지 않는다. 초안만 있으면 초안 작성, 일부만 마쳤으면 부분완료, 입력·승인 부족이면 대기, 검토 자체 실패면 실패다. 질문으로 멈출 때도 종료를 표시하며 도구 호출마다 반복하지 않는다. 다음 command는 안내만 하고 승인 없이 자동 실행하지 않는다.

## 역할별 실행

기본 모드는 `criteria`(기준수립) / `verify`(실행검증)다. 호환별칭 `pre-event` → `criteria`, `on-site` → `verify`를 유지하되 시간 허가로 해석하지 않는다. build_policy의 criteria·data·prompt 등 해당 행위 허용을 확인한다. 사전 기준수립이 금지된 행사는 공식 제작 시작 이후 제품 제작 전에 criteria를 수행한다. 기존 제품은 재사용 자격과 독립 근거를 확인하며 이미 본 실제 출력으로 expected를 역산하지 않는다.

- **criteria (제품 제작 전, 설계 초안은 있으면 참고):** 제품·모델의 actual 출력이나 판정에서 expected를 역산하지 않는다. 명세·독립 계산 등으로 시나리오의 expected와 출처, 각 surface의 제품 유형별 검증 기준을 먼저 정하고 contract에 고정한다. 아직 실행하지 않았다면 actual·verdict는 미실행으로 남긴다. contract 경로를 `hackathon.yaml`의 `demo_contract`에 기록한다.
- **verify (구현과 필요한 실제 환경 연결 후):** 고정된 contract와 preparation.md, adaptation.md(있으면)를 읽고 동일한 scenario를 실제 환경에서 실행하여 actual·verdict·evidence를 덧붙인다. 실제 출력에 맞춰 expected를 바꾸지 않는다. expected 자체가 잘못됐거나 출처가 부족하면 ORACLE INVALID/UNVERIFIED로 격리한다. 독립 근거로 수정해도 해당 scenario는 이번 행사 deck·pitch·submission에서 PASS 결과로 되살리지 않고 한계로만 설명한다. 이전 버전과 변경 이유를 보존하고 새 기준은 향후 별도 검증한다.

demo schema는 프로젝트마다 다르다. 고정 YAML 필드를 강제하지 않는다. YAML, JSON, Markdown 중 제품에 가장 읽기 쉬운 형식을 선택하고 현재 행사 workspace에 둔다.

## 순서

1. criteria에서 scenario별 expected 값을 제품·모델 출력과 독립적인 명세나 손 계산 등으로 정하고 출처를 적는다. 제품 코드와 테스트는 동작 확인 자료로 쓰되 제품이 만든 expected의 독립 근거로 단독 사용하지 않는다.
2. demo에 보여줄 surface(web UI, CLI, CI comment, API 응답 등)를 모두 적는다.
3. 각 surface에 `AGENTS.md`의 제품 유형별 기준을 적용한다. 판정 제품은 positive control(문제 입력 → 문제 판정)과 safe negative control(정상 입력 → 정상 판정), 편집·계산 제품은 동작 결과와 보존 상태(invariant), 복원·생성 제품은 사전 평가 기준·독립 참조 자료·허용 오차를 고정한다. 혼합 제품은 주장별로 나눈다. 조작 성공은 복원 품질의 증거가 아니며 객관적으로 검증하지 못한 품질 주장은 UNVERIFIED다.
4. `/prepare`의 local/mock 실행과 현장 실제 실행에서 같은 입력을 재현하고 actual·로그를 기록한다.
5. 고정한 expected와 actual을 비교해서 surface별 verdict를 낸다.

제품이 내부에서 모델로 expected를 만들어 판정하는 구조라면, 그 expected도 1의 독립 근거와 대조한다. 대조하지 못한 제품 판정은 UNVERIFIED다.

## Verdict

- PASS: 제품 결과가 사전에 고정한 독립 expected·평가 기준·허용 오차와 invariant를 충족한다.
- PRODUCT FAIL: expected가 유효하고 infra와 모델이 정상인데 제품 결과가 다르다.
- MODEL ERROR: 모델 출력이 잘못돼 제품 판단이 성립하지 않는다.
- INFRA ERROR: sandbox, network, quota, CI runner 같은 실행 환경이 실패했다.
- ORACLE INVALID / UNVERIFIED: expected가 틀렸거나 독립 근거가 없다.

ORACLE INVALID나 UNVERIFIED를 제품의 문제 발견(예: collision)이나 PRODUCT FAIL로 적지 않는다. 같은 모델이나 여러 모델이 같은 답을 반복해도 expected의 근거가 되지 않는다.

## 필수 조건별 관측과 집계

case별 필수 조건의 실제 관측과 부분 판정, 전체 판정 이유를 함께 기록한다. 숫자 일치만으로 UI·provenance·상태 전이를 포함한 case 전체를 PASS로 올리지 않는다. DOM 텍스트 존재와 실제 표시를 구분해 display:none·잘림·접힌 상태를 확인하고, 실패 뒤 재시도는 새 요청·동일 입력 식별자·최종 결과를 대조한다. CLI/API 제품은 해당 입출력과 보존 상태로 검사하며 없는 웹 UI를 요구하지 않는다.

숫자 PASS+필수 UI FAIL이면 전체 PASS가 아니며, 클릭 성공+다른 입력 결과는 실패다. 원래 고정 expected가 없는 실시간 숫자는 UNVERIFIED이고 모의응답·격리 handler 실행은 실제 배포 백엔드 성공과 분리한다. 수정 후 영향받은 case와 코드·설정·배포 버전을 재대조하기 전에는 PASS로 승격하지 않는다. 관련 파일 바이트가 같은 문서 전용 커밋을 제품 재검증으로 오해하지 않는다.

기존 contract의 expected·input·허용 오차를 사후 분해·수정해 실패를 PASS로 되살리지 않는다. 선택적으로 `tools/workflow_checks.py`의 aggregate_checks를 집계 보조로 사용할 수 있지만 제품 실행·독립 근거·브라우저 관측을 대신하지 못한다. 새 필드나 contract schema는 강제하지 않는다.

## 반드시 표현할 내용

형식은 자유지만 아래 의미는 확인할 수 있어야 한다.

- 이름 있는 demo scenario 또는 ground truth
- expected 값의 출처
- 시작 조건이나 필요한 setup
- 사용자가 하는 행동 또는 입력
- 기대 결과
- surface별 제품 유형에 맞는 control·동작 결과·invariant·평가 기준·허용 오차
- 실제 결과와 verdict
- 실제로 보여줄 evidence
- 다시 실행하는 방법
- 발표에서 제외할 scenario, sponsor, 기능과 이유
- 필요하면 fallback

예시(형식은 자유): 주문 금액 계산은 고정된 가격표와 손 계산으로 할인 적용·미적용 결과 및 원본 가격표 보존을 검증한다. 방 편집은 한 가구 이동 시 다른 가구·방 유지, 초기화 시 보정 완료 상태 복귀를 독립 명세로 정한다. 복원 품질은 별도의 참조 자료·평가 기준·허용 오차로 검증한다. 제품·모델 출력에 맞춰 기준을 바꾸거나 안전·충돌 판정 기능을 추가하지 않는다.

## 규칙

- 모델 생성값은 한 번이든 여러 번이든 정답의 근거로 쓰지 않는다.
- 같은 scenario를 반복해서 재현할 수 있어야 한다.
- demo에 필요 없는 기능을 추가하지 않는다.
- deck, pitch, submission은 PASS scenario와 실제 evidence만 결과로 쓴다.

생성한 demo contract 경로를 현재 행사 workspace의 `hackathon.yaml`의 `demo_contract`에 workspace 기준 상대 경로로 남긴다. 필드가 없으면 추가한다.

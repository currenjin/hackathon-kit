---
description: 제품 준비, 제출, 발표 직전 상태를 실제 실행과 렌더 결과로 점검한다
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

`AGENTS.md`의 현재 해커톤 workspace 선택과 행사 전 완료 기준, Demo 계약을 따른다. 시작에 `/preflight <모드> · 시작 | 행사 slug(미확정이면 행사 미확정) | 이번 작업 범위`, 종료에 `/preflight <모드> · 실제 상태 | 행사 slug | 보고서 또는 없음 | PASS / FAIL / RISK / N/A 결과·남은 승인/다음 단계`를 표시한다. 모드는 pre-event 또는 final이며 불명확하면 모드 미확정으로 표시하고 질문 뒤 대기로 종료한다. 검토완료는 검사 종료이지 모든 항목 PASS나 제품 구현 완료가 아니다. 일부만 검사했으면 부분완료, 입력·승인 부족이면 대기, 검사 자체 실패면 실패다. 질문으로 멈출 때도 종료를 표시하며 도구 호출마다 반복하지 않는다. 다음 command는 안내만 하고 승인 없이 자동 실행하지 않는다.

현재 행사 workspace와 실제 제품을 기준으로 확인한다. 문서만 읽고 PASS 처리하지 않는다.

두 번 실행한다.

- pre-event: preparation readiness 점검. 사전 제작 허용·실제 구현된 범위만 product readiness도 별도로 검사한다. `/prepare`는 허용된 제품 검사에만 필요하며 금지 행사 사전 점검의 필수 입력이 아니다. 결과는 `workspace/<event-slug>/preflight-pre-event.md`
- final: `/submit` draft 뒤, 실제 제출 전. 제출·발표 중 이번 검사 범위를 명시한다. 조건부 최종 발표는 선정 대기로 분리하고 실제 폼에 필요한 제품·자료·접근 검수는 유지한다. 선정 후 발표 범위만 재개하며 제출 확인을 되돌리지 않는다. 결과는 `workspace/<event-slug>/preflight-final.md`

다시 실행하면 파일을 덮어쓰지 않는다. 실행 시각을 heading으로 한 새 section을 맨 위에 추가하고 이전 결과는 history로 남긴다. 기존 workspace의 `preflight.md`는 그대로 둔다.

## Pre-event

먼저 build_policy와 공식 출처·제작 시간·행위별 허용 상태를 확인한다. on-site-build-only의 사전 점검에는 허용된 제품 명세·화면·상태 설계·사용자 검토·현장 실행 계획과 규칙·지참 기기·허용준비를 포함하되 제품 실행·구현을 요구하지 않는다. restricted-preparation도 확인된 준비만 점검하고 unknown은 RISK다. 아래 제품 실행 항목은 사전 제작이 허용되어 실제 구현한 범위에만 적용한다. N/A는 제품 PASS가 아니다.

### 사전 준비 완료 gate

[사전 준비 완료 기준](../../references/pre-event-readiness.md)을 읽고 다음을 근거 경로·버전·PASS / FAIL / RISK / N/A와 함께 따로 보고한다.

- 제품 계획 준비: 제품 명세, 화면·상태 설계, 실제 전달한 시안의 사용자 검토/승인, walkthrough 빈칸 해소, 현장 실행 계획.
- 실행환경 준비: 범용 스타터·도구·지참 기기의 실제 검증 범위와 사전 확인 가능한 남은 작업.
- 현장 확인 대기: 사전 확인 불가 이유, 최초 확인 경로와 독립 성공/실패 기준, 실패 대응·자격 영향·중단/축소 조건을 갖춘 계정·모델·권한·배포 확인.
- 실제 제품 검증: 미구현/미실행 또는 독립 기준과 실제 제품 경로의 검증 결과. 허용된 사전 구현 행사는 기존 제품 E2E·UI·복구 gate도 충족해야 한다.

입력 → 행동 → 화면·상태 변화 → 결과 → 예외를 따라가며 `무엇을 보여주나`, `누르면 어떻게 되나`, `AI와 고정 코드 중 누가 맡나` 같은 핵심 결정이 남았는지 검사한다. 미해결이면 FAIL 또는 RISK의 이유를 적고 전체 결론은 **사전 준비 미완료**로 쓴다. 스타터 build·checksum·테스트 수로 이 결과를 PASS로 바꾸지 않는다.

지급 전 계정 등만 미확인이고 필수 산출물·검토와 사전 검증, 대응 계획이 충족됐으면 `사전 준비 완료 · 제품 미구현/현장 확인 대기`처럼 범위를 붙인다. 제품 PASS·발표 ready·실제 제출 완료로 승격하지 않는다. 공식 금지·허용 미확인으로 필요한 산출물을 준비할 수 없으면 `공식 제한으로 준비 범위만 점검`이며 N/A로 지워 전체 준비 완료로 만들지 않는다. 새 YAML schema나 사전 제품 코드를 요구하지 않는다.

- 구현 전 criteria에서 고정한 demo contract의 expected마다 제품·모델 결과와 독립된 출처가 있고, 각 발표 surface에서 제품 유형별 검증을 local/mock으로 재현했다. 판정은 positive/safe negative control, 편집·계산은 동작 결과와 invariant, 복원·생성은 사전 평가 기준·참조 자료·허용 오차를 적용한다. 아직 못 했다면 PASS가 아니다
- 제품 핵심 E2E가 동작한다
- demo 핵심 UI 디자인이 구현되어 있다
- `sponsor_requirement`가 공식 출처와 함께 적혀 있다
- 쓰기로 한 sponsor adapter가 공식 문서 기준으로 가능한 데까지 구현되어 있다
- credential 없이 검증 가능한 test/typecheck가 통과한다
- 현장에서 남은 sponsor 작업이 key/endpoint 연결 수준으로 정리되어 있다
- Git 제품은 branch·HEAD·working tree 상태와 미커밋 준비 변경 범위가 `preparation.md`에 있다. dirty HEAD만으로 복구 가능한 준비 기준점이라 하지 않으며 `/adapt` 전 준비 상태 보존·복구 확인 조건이 있다
- hosted app은 실제 앱 위치·소유 계정·권한과 확인된 복구 방법·근거를 기록했다. 복구 미확인/부재는 RISK이며 `/adapt` 수정 전에 보존을 확인한다. 플랫폼 버전·복원 기능이나 Git commit을 가정하지 않는다
- deploy/run/reset 방법이 있다
- submission 마감과 timezone이 공식 출처와 함께 적혀 있다
- 이번 검수에서 확인한 최근 응답·보고·`preparation.md`/`adaptation.md`/`report.md`/최근 작성 문서 상단에 흐름 breadcrumb(`> ` 인용문, 완료만 bold, 현재 상태 괄호 표기)가 실제로 들어 있다. 생략·형식 위반은 FAIL이며 미이행 상태를 완료로 승격하지 않는다
- `product.name`이 확정됐거나 임시 코드명과 재명명 영향범위가 기록돼 있다. 미확정이면 `/design` 완료가 아니라 초안 단계로 표기한다

공식 규칙상 현장 제작만 허용되는 경우 사전 구현 완료 항목은 허용 범위에 맞춰 적용하고 미구현 사실을 명시한다. N/A로 표시해도 제품 구현 완료를 뜻하지 않는다. 규칙 미확인은 N/A가 아니라 RISK로 남긴다.

## Product readiness (허용된 제작·실행 후)

- 제품 URL이 열린다
- 쓰는 sponsor API 인증이 된다
- credits/quota가 demo 반복 실행에 충분하다
- 각 sponsor의 `requirement`(없으면 `sponsor_requirement.level`)가 `required`인 경우 사용 여부와 실제 제품 경로 동작을 확인한다. 미사용·연결 실패는 FAIL이다
- 최신 build가 배포되어 있다
- secrets가 화면이나 저장소에 노출되지 않는다

## Demo

- demo contract의 expected 값마다 독립 출처가 있다
- 실제 결과가 demo contract의 독립 expected·평가 기준·허용 오차와 invariant를 충족한다
- 보여주는 surface마다 제품 유형별 검증을 실제로 실행했다. 판정 제품의 positive/safe negative control은 유지하고 편집 조작 성공을 복원·생성 품질 검증으로 대신하지 않는다
- 핵심 scenario를 reset 후 두 번 연속 재현한다
- product failure, model error, infra error, oracle invalid가 구분된다
- live demo 클릭 경로가 확정됐다
- fallback screenshot 또는 recording이 있다

## Deck

- [발표 레퍼런스 가이드](../../references/presentation-reference-guide.md)의 기술 QA와 설득/시각 QA를 분리했다. 테스트 수·잘림 없음만으로 발표 품질을 PASS 처리하지 않는다
- 메시지·실제 핵심 데모·가독성 검토에 필요한 장면으로 선정한 대표 렌더의 사용자 검토·승인 기록이 있다. 개수 규정은 없으며 렌더 불가이면 완료가 아니다

- 전체 slide를 render해서 검사했다
- clipping / overflow가 없다
- screenshot이 늘어나거나 찌그러지지 않았다
- 저해상도 이미지가 없다
- demo와 숫자가 같다
- ORACLE INVALID, UNVERIFIED, 제외한 sponsor나 기능이 결과로 들어가 있지 않다
- 최신 UI screenshot이다
- sponsor 역할이 실제 architecture와 같다
- 발표에 쓰지 않는 불필요한 slide가 없다

## Pitch

- 공식 `event.pitch_minutes`, `presentation.effective_seconds`·source·timing_status·Q&A 조건이 deck·대본·demo cue·fallback의 현재 버전과 일치한다. 공식 시간은 60초로 덮지 않으며 provisional은 공식 확정이 아니다
- 슬라이드별 발화·demo·loading·전환·여유의 총 경과시간을 계산했다. 동시 진행은 중복 합산하지 않고 Q&A 포함 슬롯은 확인된 Q&A 예산도 총합에 넣었다. Q&A unknown/배정 미확인은 별도나 0초로 가정하지 않고 RISK로 남긴다
- 시간 변경 후 dirty 상태의 자료가 모두 재검수됐다. 변경 기록만으로 발표 준비 완료가 되지 않는다
- `presentation.review.active_version`이 명시돼 있고 `status: approved`이며 현재 발표 기준 iteration이 하나다. active 미지정, `pending`/`in_review`, 다중 active, superseded 미정리는 발표 준비 완료가 아니다. 다중 iteration이 있으면 superseded_versions와 kept 분류가 각 `report.md` 상단과 일치한다

- 실제 화면을 넘기며 rehearsal했다
- loading 시간과 tab 이동을 포함해 제한 시간 안에 들어온다
- 두 번 연속 제한 시간을 지켰다
- 실제 리허설 수행자·일시·자료 버전·측정 초수와 fallback 결과가 있다. 미실시는 명시하고 계산상 예산·자동 테스트로 대체하지 않는다
- `qa_mode: none`이면 공식 또는 사용자 확인 근거와 `qa_seconds: 0`을 대조하고 Q&A 답변 검수는 해당 근거로 N/A 처리한다. 출처는 official/user-confirmed로 구분한다. 그 외에는 Q&A 답변이 실제 구현 범위를 넘지 않는다

## Submission

- draft가 실제 제출 폼 필드를 모두 채웠다
- character limit을 넘지 않는다
- demo contract와 숫자가 같고 제외 항목이 없다
- repository/demo/slides/guide 링크를 직접 열어봤다
- public이어야 하는 링크가 로그인 없이 열린다
- 마감까지 남은 시간을 행사 timezone으로 확인했다

## 자료 인계 검수

[자료와 실행 기록 인계](../../references/delivery-handoffs.md)를 적용한다. pre-event에는 허용된 실행표의 담당·확인 시점·완료 증거·미달 시 축소 조건과 최초 호출의 승인·비용·실행/미실행 범위를 본다. 금지된 사전 명령·criteria·자료나 아직 없는 최종 사실표를 요구하지 않는다.

final에는 기존 사실표·공식 기준별 증거와 실제 deck/pitch/guide/submission을 원문·독립 contract·실행 evidence까지 대조한다. 현재 build·claim·언어·검수한 자료 버전·불일치와 해결 여부를 보고서에 남긴다. 파일 존재·반복된 문구·정적 테스트만으로 PASS/ready가 되지 않는다. 미해결 주장은 제외 또는 한계로 남기고 기존 presentation pending/dirty 계약을 유지한다. 공식 기준 미확인은 RISK이며 임의 심사 점수를 만들거나 기존 제품 실행 판정을 바꾸지 않는다.

## Multilingual

- 설정된 언어 artifact가 모두 있다. `/pitch`가 작성하는 `output/guide/<lang>.md`도 `language.public_guide`의 각 언어별로 확인한다. 파일 생성과 공개 URL 확인은 별개다
- 번역 때문에 layout이 깨지지 않았다
- 숫자, 제품명, sponsor 이름이 언어별로 일치한다

## Report

[현장 상태와 종료 점검](../../references/field-status-and-closeout.md)을 함께 읽는다. 현재와 과거 상태, 사용자 보고와 직접 확인을 구분한다. 필요한 경우 읽기 전용 `tools/workflow_checks.py`로 명시한 workspace와 검사 범위의 진단을 확인하되 결과를 제품 PASS로 쓰거나 과거 기록을 자동 수정하지 않는다.

각 항목을 PASS / FAIL / RISK / N/A로 적는다.

N/A는 실제로 해당하지 않을 때만 쓰고 이유를 적는다. `AGENTS.md`의 Sponsor 사용 조건에 따라 `used`는 채택 결정으로 읽고 실제 사용은 실행 evidence로 확인한다. null·누락·기존 의미 충돌은 채택 미정이다. 채택 미정 또는 unknown 요건은 RISK이지 제외나 N/A가 아니다. `required` sponsor 미사용이나 연결 실패처럼 필수 조건을 못 채우면 FAIL이다. judged 제외는 점수 영향을 기록한다.

FAIL을 문장으로 완화해 PASS로 바꾸지 않는다. 남은 RISK에는 발표 시 우회 방법을 함께 적는다.

final 결과에 FAIL이 있으면 실제 제출 전에 사용자에게 알리고, 해당 주장을 submission draft에서 뺀다.

제출 범위 완료는 presentation ready가 아니다. 발표 범위를 검사할 때는 발표 관련 시간·Q&A·대표 렌더 승인·전체 렌더·설득/시각 QA·실제 리허설이 모두 확인된 경우에만 `presentation.status: ready`로 기록한다. 공식 시간이나 Q&A가 미확인이면 준비용 검수 결과와 최종 준비 상태를 구분하고 pending/dirty를 유지한다. 검사 종료는 presentation 완료와 다르다.

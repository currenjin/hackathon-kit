---
description: 심사 기준, 실제 제품, demo evidence를 하나의 발표 서사로 묶어 최종 deck을 만든다
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

`AGENTS.md`의 현재 해커톤 workspace 선택과 Command 입출력, Demo 계약을 따른다. 시작에 `/deck · 시작 | 행사 slug(미확정이면 행사 미확정) | 이번 작업 범위`, 종료에 `/deck · 실제 상태 | 행사 slug | 산출물 또는 없음 | 남은 검증/승인/다음 단계`를 표시한다. 전체 렌더와 내용 QA까지 마쳐야 완료다. 문구·slide map만 작성했으면 초안 작성, 일부만 마쳤으면 부분완료, 입력·승인 부족이면 대기, 작업 실패면 실패다. 문서 작성은 제품 구현 완료가 아니다. 질문으로 멈출 때도 종료를 표시하며 도구 호출마다 반복하지 않는다. 다음 command는 안내만 하고 승인 없이 자동 실행하지 않는다.

현재 행사 workspace와 실제 제품 위치(Git 저장소 또는 소유 계정의 hosted app)를 읽고 발표용 deck을 만든다. build_policy의 deck 사전 작성 허용을 개별 확인한다. 금지·unknown이면 사전 작성하지 않는다. 최신 신규 출품물의 자격이 확인된 실제 evidence만 결과로 쓰며 과거/연습용 evidence로 대체하지 않는다.

이 커맨드의 목표는 슬라이드 문구를 채우는 것이 아니다. 심사위원이 제한된 시간 안에 문제, 제품, 실제 동작, sponsor 역할, 차별점을 이해하고 기억할 수 있는 deck을 완성하는 것이다.

## 1. 먼저 읽을 것

최소한 아래를 확인한다.

- 현재 행사 `hackathon.yaml`
- `ideation.md`가 있으면 함께
- `design.md`
- `preparation.md`
- `adaptation.md`가 있으면 함께
- `/demo`가 만든 demo contract. 위치는 `AGENTS.md`의 Command 입출력을 따른다
- 실제 제품 위치와 최신 UI
- 실제 실행 결과, 로그, report, CI 결과
- `references/winners.md`와 `references/submissions.md` 중 현재 행사와 관련 있는 링크
- `.claude/rules/design.md`
- [발표 레퍼런스 가이드](../../references/presentation-reference-guide.md): 출처별 적용 한계, 공통 시간 해석, 대표 렌더 승인 흐름
- `.claude/rules/writing/common.md`
- 출력 언어에 맞는 writing rule

파일에 적힌 내용보다 실제 제품과 실제 실행 결과가 우선한다. 서로 다르면 먼저 차이를 해결한다.

핵심 demo 장면이 잡히고 위 필수 입력이 갖춰지면 행사 전에도 deck 초안을 작성할 수 있다. 입력이 없으면 멈추고 입력을 만드는 작업부터 제안하며, 초안을 이유로 필수 입력·완료 계약을 생략하지 않는다. 실제 미검증 결과는 evidence 대기 자리 또는 한계로 구분하고 성과·수치를 만들지 않는다. local/mock evidence는 그 경로로만 표시하며 on-site 완료로 승격하지 않는다. 초안 뒤에는 `/pitch`의 필수 입력 충족 여부와 작성 가능한 시점·다음 작업을 선제 제안하되 자동 실행하지 않는다.

## 공통 사실과 증거 인계

[자료와 실행 기록 인계](../../references/delivery-handoffs.md)를 따른다. 기존 사실표를 찾아 재사용하고 없으면 [공통 사실 양식](../../templates/project-facts.md)의 필요한 절을 현재 workspace에 작성해 notes 또는 기존 인계 문서에 경로를 남긴다. 원문·독립 contract·실행 evidence를 읽어 claim별 현재 build·검증 경로·사용 범위와 한계를 확인하며 사실표 자체를 증거로 보지 않는다. 미해결 충돌은 성과에서 제외한다.

[심사 기준별 증거 양식](../../templates/judging-evidence.md)은 기존 slide map에 통합할 수 있다. 공식 기준→보여줄 장면→실행 evidence를 연결하고, 미확인 기준·상속한 코드·행사 중 제작 부분·local/mock 한계를 분리한다. /pitch와 /submit이 같은 경로를 참조하도록 인계하며 다른 command를 자동 실행하지 않는다.

## 2. 발표 조건을 고정한다

deck을 만들기 전에 아래를 한 줄씩 적는다.

- 공식 발표시간과 출처, `presentation.effective_seconds`·`timing_status`·`qa_mode`·`qa_seconds`
- live demo 유무
- presenter 언어
- deck 언어
- 청중 언어
- 제출용 deck인지 발표용 deck인지
- 보여줘야 하는 sponsor. `AGENTS.md`의 Sponsor 사용 조건에 따라 채택 결정(`used: true`)과 실제 사용 evidence가 모두 확인된 대상에서 고른다. null·누락·기존 의미 충돌 또는 unknown 요건은 미정이며 N/A가 아니다. 미검증 사용은 성과에서 빼고 required 실패·judged 영향은 한계로 기록한다
- 심사 기준
- 가장 강한 evidence 1~3개
- 제외할 scenario, sponsor, 기능

발표 시간이 짧으면 slide 수를 줄인다. slide 수를 채우기 위해 메시지를 만들지 않는다.

가이드의 공통 시간 해석을 `/pitch`와 동일하게 적용한다. 공식 `event.pitch_minutes`가 확인되면 그 값을 초로 환산하며, 공식 미확인은 null 그대로 두되 출처 있는 사용자 확인 시간·범위와 준비 목표가 있으면 보존한다. 둘 다 없을 때만 준비용60초/provisional/user-default를 쓴다. 필드 누락은 읽기 시 같은 규칙으로 해석하고 migration하지 않는다. 공식값·유효시간 불일치나 출처 미확인은 먼저 해결한다. Q&A 미확인은 별도로 가정하지 않고 RISK로 남긴다. 공식 또는 사용자 확인으로 Q&A가 없으면 `qa_mode: none`, `qa_seconds: 0`을 쓰고 출처를 official/user-confirmed로 구분한다. Q&A 포함 슬롯이면 배정된 Q&A까지 총합에 넣는다. 시간·출처·Q&A 조건을 slide map에 남기고 이후 조건 변경은 `/adapt`로 기록한다.

## 3. 서사를 먼저 만든다

PPT부터 만들지 않는다. 먼저 짧은 발화 초안을 쓰고 slide map을 작성한다. 이는 서사 초안이지 필수 입력을 우회한 `/pitch` 완료가 아니다.

각 slide마다 아래를 정한다.

| 항목 | 내용 |
| --- | --- |
| Message | 이 slide에서 기억해야 할 한 문장 |
| Evidence | 그 말을 증명하는 실제 근거 |
| Visual | screenshot, diagram, number, text 중 무엇으로 보여줄지 |
| Source | demo contract의 scenario 이름, 파일, 실행 결과 중 어디서 왔는지 |
| Pitch role | 발표에서 이 slide가 맡는 역할 |
| Timing | 같은 유효시간 안의 발화·demo·전환·여유 구간, 동시 진행은 중복 합산하지 않음 |

다음은 필요한 메시지를 고르는 재료이지 각각 한 장씩 만드는 필수 목차가 아니다.

1. 제품 이름 + one-liner
2. 문제를 이해하기 위한 최소 배경
3. 실제 문제와 왜 기존 방식으로 놓치는지
4. 제품이 어떻게 해결하는지
5. 실제 제품 화면
6. 실제 실행 evidence
7. sponsor가 제품 경로에서 맡는 역할. 쓰는 sponsor가 없으면 뺀다
8. 기존 대안과의 차이
9. closing

공식값이나 사용자 확인 시간이 없는 경우의 준비 기본60초는 유지하되 장수 기본값은 두지 않는다. 시간 안에 필요한 메시지·실제 핵심 데모·가독성과 공식 조건으로 장수를 정한다. 가이드의 문제 8초 + 핵심 변화/데모 32초 + 차별/기술 12초 + 마무리 3초 + 전환/여유 5초는 사용자 정책 기반 제안이며 출처의 공식 정답이 아니다. 투자 피치의 시장·팀·전체 프레임을 강제하지 않는다. 공식 시간이 있으면 그 시간을 우선한다. 언어별 deck의 파일 구성은 제출 조건에 따른다.

신규 deck은 메시지·실제 핵심 데모·가독성 검토에 필요한 장면을 representative renders로 선정해 먼저 사용자에게 보여주고 승인받은 뒤 전체 제작한다. 대표 렌더 개수 규정은 없으며 외부 live demo 화면과 전환도 함께 확인한다. 기존 deck 자동 재생성은 하지 않는다. 대표 렌더나 승인이 없으면 전체 제작 대기다.

## 4. Evidence 중심으로 구성한다

심사 기준을 문장으로 주장하지 않는다.

확인된 공식 심사 기준별로 이를 보여줄 slide/demo 장면과 실제 evidence 출처를 slide map에 연결한다. 근거가 없으면 대기 자리 또는 한계로 남긴다. rubric이 unknown이면 미확인으로 표시하며 임의의 심사 기준을 만들지 않는다.

나쁜 예:
- "Highly innovative"
- "Built with Daytona"
- "Production ready"

좋은 방향:
- 실제 제품 screenshot
- 실제 PASS / FAIL
- Expected / Actual
- latency, count, test result처럼 검증된 수치
- 실제 GitHub Action / PR comment
- sponsor가 호출되는 architecture path

숫자와 결과는 demo contract의 PASS scenario나 실제 실행 결과에서만 가져온다. 숫자의 출처를 찾을 수 없으면 slide에서 뺀다. ORACLE INVALID, UNVERIFIED scenario와 제외한 sponsor나 기능은 결과로 넣지 않는다.

## 5. Screenshot을 제대로 만든다

실제 제품 screenshot을 mockup보다 우선한다.

screenshot마다 확인한다.

- 최신 build인가
- demo에서 실제 보여줄 상태와 같은가
- demo contract에서 검증된 결과를 보여주는가
- secret이나 개인 정보가 없는가
- 원본 비율을 유지하는가
- slide에서 읽을 핵심 영역이 충분히 큰가
- 필요하면 crop했는가. stretch하지 않는다
- 브라우저 chrome, 불필요한 빈 공간을 줄였는가
- 핵심 evidence가 fold 아래에 숨어 있지 않은가

UI가 너무 작으면 screenshot 전체를 억지로 키우지 않는다. 핵심 부분을 crop하거나 별도 detail slide를 쓴다.

## 6. Diagram을 쓸 때

diagram은 실제 architecture나 실행 순서를 설명할 때만 쓴다.

- 제품 코드의 실제 흐름과 일치해야 한다.
- sponsor logo를 나열하는 그림을 만들지 않는다.
- component 수를 발표에 필요한 만큼만 줄인다.
- 화살표 방향이 실제 data/control flow와 맞아야 한다.
- screenshot이 더 잘 설명하면 diagram을 만들지 않는다.

## 7. Visual system

`design.md`와 제품의 기존 시각 언어를 우선한다.

최소한 아래를 통일한다.

- canvas ratio
- background / surface
- typography hierarchy
- accent roles
- spacing
- border / radius
- code / number treatment
- screenshot frame
- diagram style

한 slide에는 메시지 하나를 둔다. 장식이 evidence보다 먼저 보이면 줄인다.

## 8. 다국어 deck

여러 언어가 필요하면 한 언어 deck을 완성한 뒤 다른 언어를 만든다.

직역하지 않는다.

- 사실, 숫자, slide 순서는 유지한다.
- 문장은 각 언어에서 자연스럽게 다시 쓴다.
- 번역 때문에 font size가 달라져 layout이 무너지면 layout을 다시 맞춘다.
- 제품명, API, 표준 기술 용어는 임의로 번역하지 않는다.

## 9. 산출물

결과는 `workspace/<event-slug>/output/deck/`에 저장한다.

새 iteration(review-v2 등)을 만들 때는 해당 iteration 디렉터리의 `report.md` 상단에 흐름 breadcrumb와 `presentation.review.status`(현재 상태) 및 이전 iteration 처리(superseded or kept)를 명시한다. 동시에 `hackathon.yaml`의 `presentation.review`를 갱신한다: 승인 전까지 `active_version: null`과 `status: in_review`, 사용자 승인 시 `active_version`을 해당 iteration 상대 경로로 설정하고 `status: approved`, `reviewed_at` 기록. superseded 처리한 이전 iteration은 `superseded_versions`에 추가하고 kept는 포함하지 않는다. 발표 기준 iteration은 하나만 active이며 명시 전에는 결정하지 않는다. 기존 workspace에 review 필드가 비어 있다고 임의로 채우지 않는다. 이 kit 기록 변경은 종료 게시 절차의 상시 승인으로 commit·push해 추적을 유지한다.

가능한 환경에서는 아래를 만든다.

- editable source
- PPTX
- PDF
- 필요하면 slide별 preview image

제출용 파일명은 행사명과 제품명을 알아볼 수 있게 정한다.

## 10. Render QA

파일 생성으로 끝내지 않는다. 전체 slide를 실제로 render해서 눈으로 검사한다.

각 slide에서 확인한다.

- 텍스트 overflow / clipping 없음
- font가 너무 작지 않음
- screenshot 비율 왜곡 없음
- 저해상도 이미지 없음
- alignment와 spacing 일관
- dark/light 대비 충분
- footer나 page number가 본문을 침범하지 않음
- 여러 언어가 섞여 깨지지 않음
- 마지막 slide까지 style drift 없음

문제가 있으면 수정 후 다시 render한다.

렌더할 수 없으면 완료가 아니라 시각 검수 대기다. 기술 QA(파일·overflow·실행 evidence)와 설득/시각 QA(문제→핵심 변화 이해, 한 장 한 메시지, 핵심 가독성·시선·발화 일치)를 별도로 기록한다. 테스트 수나 screenshot 잘림 없음만으로 발표 품질 완료를 주장하지 않는다. 대표 렌더 사용자 승인과 전체 렌더 검수 결과를 함께 남긴다.

## 11. Content QA

최종 deck과 source of truth를 다시 대조한다.

- 제품 이름
- sponsor 이름
- 숫자
- demo result
- architecture
- repository / slide / guide 링크
- 실제 구현 여부
- 제외 항목이 남아 있지 않음

deck에만 존재하는 기능이나 수치가 있으면 안 된다.

## 12. Pitch와 연결

마지막으로 각 slide가 `/pitch`에서 어떤 구간에 대응하는지 확인한다.

live demo가 핵심이면 deck이 demo를 대신 설명하지 않는다. deck은 문제와 맥락을 세우고, demo가 동작을 증명하도록 역할을 나눈다.

발표 시간 안에 쓰이지 않는 slide는 제출용 부록이 아니라면 제거한다.

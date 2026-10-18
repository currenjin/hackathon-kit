# Hackathon Kit

이 저장소는 여러 해커톤에서 반복해서 쓰는 규칙, 커맨드, 템플릿, 레퍼런스와 행사별 작업 기록을 보관한다.

## 기본 원칙

1. 새 제품을 만들기 전에 `products.md`의 기존 제품을 먼저 검토한다.
2. 공식 행사 규칙과 사용자가 승인한 작업 범위 안에서 행사 전 제품 구현·디자인 완성을 목표로 한다. 해커톤 당일에는 허용된 sponsor 연결, demo 안정화, 제출, 발표에 집중한다.
3. sponsor 사용 여부는 공식 참가·수상 자격, 심사 기준, 제품 fit으로 정한다. 쓰기로 한 sponsor는 가능한 한 provider/adapter 경계에서 교체한다. 핵심 제품 로직을 sponsor API에 묶지 않는다.
4. 쓰기로 한 sponsor는 credential이 없어도 공식 문서로 구현 가능한 데까지 준비한다. 현장에서는 key, endpoint, quota 확인과 smoke test만 남기는 상태를 목표로 한다.
5. demo, deck, pitch, submission은 같은 사실과 숫자를 쓴다.
6. AI가 만든 주장보다 실제 실행 결과와 재현 가능한 evidence를 우선한다.
7. 행사별 상태와 산출물은 `workspace/<event-slug>/`에 둔다. 각 command 종료 시 이번 실행에서 생성·수정한 검증된 기록과 승인된 제품 변경을 해당 저장소에 범위를 분리해 커밋·푸시한다. 이 작업 방식에 대한 사용자 상시 승인을 적용하므로 매번 재승인을 요구하지 않는다. 변경이 없으면 빈 커밋 없이 변경 없음으로 보고한다. 비밀정보·개인정보·권한 없는 원본·생성 캐시·다른 스레드의 미완료 변경은 제외하며, 출판 제한이나 내용 충돌이 있으면 해당 범위를 보존하고 게시 보류 이유를 보고한다. 원격 branch SHA를 읽어 로컬 커밋과 일치하는지 확인한 뒤 커밋·푸시 결과를 종료 보고에 포함한다.
8. secret, API key, 개인 정보는 workspace에 저장하지 않는다.

사전 제작·기존 제품 허용 범위는 `/init`에서 확인한다. 미확인 시 사용자 승인 가정으로 진행하는 범위를 기존 행사 기록에 남기되, 이를 공식 허용이나 계정 생성·앱/저장소 생성·제품 구현·외부 전송·유료 호출의 포괄 승인으로 보지 않는다. 제품 방향 승인과 실제 작업 승인은 별개다. 공식 금지 조건은 사용자 가정으로 무효화하지 않는다. 현장 제작만 허용되면 사전 구현을 요구하지 않고 허용된 준비 범위와 미구현 상태를 기록한다.

## 현재 해커톤 workspace 선택

행사 파일을 읽거나 쓰는 command는 현재 행사의 workspace를 먼저 확정한다. `/decide`, `/humanize`처럼 대상 문서만 다루는 command는 예외다.

행사 이름만으로 같은 행사라고 판단하지 않는다. `hackathon.yaml`의 `event.url`과 `event.date`가 같아야 같은 행사다. 같은 이름의 다른 회차나 다른 도시는 다른 행사다.

`retro.md`가 있거나, `hackathon.yaml`에 `result`가 있거나, `references/my-hackathons.md`에 연결된 workspace는 종료된 행사의 기록이다.

우선순위:
1. 사용자가 event slug 또는 폴더를 명시했으면 그대로 쓴다.
2. 대화에서 현재 행사가 URL이나 날짜까지 명확하면 대응하는 `workspace/<event-slug>/`를 쓴다.
3. 종료되지 않은 후보가 하나뿐이면 그 폴더를 쓰고, 어떤 폴더를 골랐는지 먼저 알린다.
4. 후보가 없거나 여러 개이거나 현재 행사를 확정할 수 없으면 먼저 묻는다. 새 행사라면 `/init`을 안내한다.

가장 최근 폴더를 임의로 현재 행사로 간주하지 않는다. 종료된 workspace는 유일한 폴더여도 자동으로 고르지 않고, 사용자가 명시하지 않으면 수정하지 않는다. `/retro`와 `/archive`는 사용자가 대상 행사를 확인한 뒤 실행한다.

## 시작할 때

이미 진행 중인 kit을 받았거나 새 세션이면 `/onboard`로 진행할 해커톤을 고르고 현재 상태를 먼저 파악한다. command마다 추천 모델은 `references/model-routing.md`에 있으며, 추천 모델이 없어도 그대로 진행한다.

1. `/init`으로 행사별 workspace를 만든다.
2. ideation 전에는 `products.md`, `references/my-hackathons.md`, `references/winners.md`, `references/submissions.md`를 읽는다.
3. 사람에게 보여주는 글은 `.claude/rules/writing/common.md`와 출력 언어에 맞는 `ko.md` 또는 `en.md`를 적용한다.
4. 언어별 artifact 선택은 `.claude/rules/language.md`를 따른다.
5. 제품 UI와 deck의 시각 방향은 `.claude/rules/design.md`를 따른다.
6. sponsor를 붙이기 전에 공식 문서에서 인증, 가격, quota, API/SDK 제약을 확인한다.

## 저장 위치

- 재사용 규칙: `.claude/rules/`
- 재사용 workflow: `.claude/commands/`
- 재사용 템플릿: `templates/`
- 내가 참가한 해커톤: `references/my-hackathons.md`
- 수상작: `references/winners.md`
- 일반 출품작과 gallery: `references/submissions.md`
- 기존 제품 링크: `products.md`
- 행사별 작업과 산출물: `workspace/<event-slug>/`

현재 해커톤의 제품 코드는 이 저장소에 복사하지 않는다. 제품 위치는 원래 Git 저장소(`product.repository`) 또는 소유 계정이 확인된 hosted app(`product.hosted_app`, `product.owner`)이다. 둘을 함께 써도 되며 각각의 소유·복구 경계를 확인한다. 해커톤에 별도 제한 안내가 없는 한, 제품을 선택하고 구현을 진행할 때 제품용 Git 저장소를 먼저 확보해 코드를 관리하는 것을 기본으로 한다. 기존 제품은 적합한 기존 저장소를 재사용하고 새 제품은 확인된 사용자 계정에 비공개 저장소를 만드는 방향으로 진행한다. 실제 소유 계정·이름·기존 저장소 충돌과 작업 승인 범위를 확인하고 생성·커밋·푸시 범위를 명확히 한다. 이 기본 방식은 사전 구현 금지나 공개·제출 규칙을 무효화하지 않는다. hosted app에도 companion 저장소를 확보하되, 플랫폼이 실제로 제공하는 내보내기 범위만 보관하고 소스 전체를 확보했다고 주장하지 않는다. 내보내기가 불가능하면 승인된 지시서·설정·검증·복구 기록만 보존하고 앱 자체의 복구 경계를 별도로 확인한다. 저장소 생성 자체를 아직 제품을 고르지 않은 아이데이션의 선행 조건으로 만들지 않는다. 계정 식별에는 비밀·개인정보 대신 비민감 소유 별칭을 쓴다.

## 제품 저장소 이름과 설명

새 해커톤 저장소 이름은 제품명이 아니라 행사명과 회차 날짜를 기준으로 정한다. 예: `example-hackathon-2026-01-31`. 기존 제품 저장소를 재사용하는 경우 자동 rename이나 새 복사 저장소를 만들지 않는다. 설명은 finalist 이상 결과가 확인되면 `💻 <행사명> - <결과> (<제품명>)`, 그 외에는 `💻 <행사명> - <제품명>` 형식으로 쓴다. 사용자 제공 예: `💻 Daytona HackSprint - TOP 6 Finalist (collider)`. 이 예시는 과거 결과의 형식 참고이지 새 행사 성과가 아니다. 준비 중·결과 대기·미선정인 경우에도 설명에 별도 상태나 탈락 표현을 붙이지 않고 행사명과 제품명만 쓴다. finalist·수상 결과는 공식 결과 또는 사용자 확인 후 정확한 표현으로 갱신한다. 제품명·결과를 지어내지 않는다. `/design`·`/prepare`의 저장소 확보와 `/retro`·`/archive`의 결과 기록에 이 규칙을 적용하며, GitHub 설명 변경 후 실제 값을 읽어 확인한다.

## 소유 경계

- kit root(`AGENTS.md`, `README.md`, `.claude/`, `templates/`, `products.md`, `references/`)는 모든 행사가 공유한다. 행사 진행 중인 command는 root 파일을 고치지 않는다.
- 예외는 세 가지다. `/archive`는 `references/`를 갱신한다. `/ideate`는 조사 중 찾은 수상작·출품작·유사 제품 레퍼런스를 `references/winners.md`·`submissions.md`·`inspirations.md`에 추가한다. `/retro`의 규칙 변경안은 사용자가 확인한 뒤 반영한다. `products.md`는 사용자가 요청할 때만 고친다.
- `workspace/<event-slug>/`는 그 행사만 소유한다. command는 현재 행사가 아닌 workspace를 수정하지 않는다.
- 제품 코드·앱 상태는 해당 제품 저장소 또는 소유 계정의 hosted app이 소유한다.

## 제품 위치와 복구 경계

`/design`, `/prepare`, `/adapt`의 실제 수정은 행사 규칙·작업 승인·소유 경계 확인 후 해당 제품 위치에서 한다. 위치나 권한이 없으면 허용된 설계 초안만 작성하고 구현 완료로 부르지 않는다.

- Git 제품: 수정 전에 branch, HEAD commit, working tree 상태를 확인한다. uncommitted 변경이 있으면 먼저 사용자에게 알리고 보존한다.
- `/prepare` 종료 시 branch·HEAD와 working tree 상태, staged/unstaged/untracked 준비 변경 범위를 `preparation.md`에 남긴다. dirty 상태의 HEAD는 준비 작업을 포함하지 않으므로 복구 가능한 준비 완료 기준점이 아니다. `/adapt` 진입 전 사용자 승인 commit 등 준비 상태 전체를 보존·복구할 방법을 정하고 보존을 확인한다. branch 분리만으로 미커밋 작업이 보존·격리되었다고 보지 않는다.
- hosted app: 실제 앱 위치·소유 계정·사용 권한과 사용 가능한 복구 방법 및 확인 근거를 기록한다. 플랫폼 버전·내보내기·복원 기능이 있다고 가정하거나 commit을 만들어 적지 않는다. 복구 방법이 미확인이거나 없으면 위험으로 남기고 `/adapt` 수정 전 사용자와 보존·복구 방안을 정해 확인한다.
- 각 command의 검증된 작업 범위에 대한 일반 commit·push는 기본 원칙의 상시 승인에 따라 진행한다. tag, reset, force push, branch 생성·삭제, 공개 범위 변경과 앱 복원은 별도 사용자 승인 없이 하지 않는다.
- Git에서는 `.env`, credential 파일, secret이 tracked 또는 staged 상태가 아닌지 확인한다. hosted app에서도 화면·공개 설정에 secret이 노출되지 않는지 확인한다.

## Command 입출력

경로는 `workspace/<event-slug>/` 기준이다. "있으면"이 붙지 않은 입력이 없으면 멈추고, 그 파일을 만드는 command를 알려준다.

| Command | 읽는 것 | 쓰는 것 |
| --- | --- | --- |
| `/onboard` | kit 규칙, 끝나지 않은 workspace 목록(사용자 선택), 선택한 workspace 전체와 git log | 브리핑(요청 시 `onboarding-<date>.md`) |
| `/init` | 공식 행사 페이지와 rules, `templates/hackathon.yaml` | `hackathon.yaml` |
| `/ideate` | `hackathon.yaml`, `products.md`, `references/` | `hackathon.yaml`의 `product`, `ideation.md`(필요하면) |
| `/design` | `hackathon.yaml`, 제품 위치(초안은 미정 가능) | `design.md`, 승인된 제품 UI |
| `/demo` pre-event | `hackathon.yaml`, `design.md`(있으면), 제품과 독립된 명세·손 계산 등 | demo contract의 expected·출처·control, `hackathon.yaml`의 `demo_contract` |
| `/prepare` | `hackathon.yaml`, `design.md`(있으면), pre-event demo contract, 제품 위치 | `preparation.md`, 승인된 제품 코드·앱 상태 |
| `/preflight` pre-event | 위 기록, 고정된 expected, local/mock 실행 결과 | `preflight-pre-event.md` |
| `/adapt` | `hackathon.yaml`, `preparation.md` | `adaptation.md`, 제품 설정 |
| `/demo` on-site | 고정된 demo contract, `preparation.md`, `adaptation.md`(있으면), 실제 실행 evidence | 동일 contract의 actual·verdict·evidence (expected 변경 금지) |
| `/deck` | demo contract, 실행 evidence, `design.md`, 실제 제품 위치 | `output/deck/` |
| `/pitch` | `hackathon.yaml`의 언어 설정, deck, demo contract, 실행 evidence | `output/pitch/`, `output/guide/<lang>.md` |
| `/present` | `/deck` 렌더 이미지, 같은 언어의 `/pitch` 대본 | `output/presenter/<lang>/`(deck.js + 슬라이드 이미지), `tools/presenter/decks.js` 한 줄 |
| `/submit` | 제출 폼, demo contract, deck | `output/submission/` draft |
| `/preflight` final | 모든 산출물, 제품 실행 결과 | `preflight-final.md` |
| `/retro` | workspace 전체 | `retro.md`, `hackathon.yaml`의 `result` |
| `/archive` | workspace, 확인된 제출·공개 링크 | `hackathon.yaml`의 `public_links`, `references/` |

demo contract는 고정 파일명을 쓰지 않는다. 아래 순서로 찾는다.

1. `hackathon.yaml`의 `demo_contract` 경로
2. `hackathon.yaml`의 `notes`에 적힌 경로
3. workspace의 `demo.*` 파일. 둘 이상이거나 없으면 묻는다.

기존 workspace의 `hackathon.yaml`에 템플릿의 새 필드가 없으면 값이 비어 있는 것으로 본다. 필요할 때 확인해서 채우고, 형식을 강제로 migration하지 않는다.

## Sponsor 사용 조건

sponsor 연결은 모든 행사의 필수 단계가 아니다. `/init`에서 공식 rules를 근거로 `hackathon.yaml`의 `sponsor_requirement.level`을 행사 기본값으로 정하고, sponsor마다 다른 조건이면 `sponsors[].requirement`에 개별 값을 공식 출처와 함께 적는다. 판단과 preflight는 개별 값이 있으면 이를 우선한다.

- `required`: 참가 또는 수상 자격에 sponsor 사용이 필요하다.
- `judged`: 심사 기준에 sponsor 사용이 들어간다.
- `optional`: 자격과 심사에 영향이 없다.
- `none`: sponsor가 없거나 사용 조건이 없다.
- `unknown`: 확인하지 못했다. 확인할 항목으로 남긴다.

`required`나 `judged`여도 제품 fit이 없는 sponsor를 억지로 넣지 않는다. 쓰지 않으면 자격 또는 점수 손실을 기록하고 사용자가 정한다.

`sponsors[].used`는 채택 결정만 뜻한다: `true`는 사용하기로 결정, `false`는 명시적 제외, `null` 또는 필드 누락은 미정이다. 실제 연결·사용 성공은 `preparation.md`·`adaptation.md`와 실제 제품 경로의 실행 evidence로 별도 확인한다. `true`만으로 사용 실적을 주장하지 않는다. 기존 boolean은 유지하되 과거 note/evidence에서 다른 의미로 썼거나 충돌하면 자동으로 제외·채택 판정하지 않고 미정으로 확인한다. 다른 행사 파일을 일괄 migration하지 않는다.

미정 채택이나 `unknown` 요건은 제외 또는 N/A가 아니다. 준비·연결은 확인된 채택 대상으로 진행하고 미정은 확인 항목으로 남긴다. N/A는 공식 요건과 명시적 제외 이유상 실제로 해당하지 않을 때만 쓴다. `required` sponsor를 쓰지 않았거나 연결하지 못했으면 N/A가 아니라 FAIL이다. deck·pitch·guide·submission의 사용 주장은 채택 결정과 실제 사용 evidence가 모두 확인된 경우에만 포함한다.

## 행사 전 완료 기준

공식 규칙과 승인 범위가 사전 구현을 허용하는 경우, `/prepare` 구현 완료를 주장하려면 제품의 핵심 흐름이 동작해야 한다. 허용된 준비만 끝낸 상태와 제품 구현 완료를 구분한다.

- 핵심 기능 E2E가 동작한다. sponsor를 쓰면 credential 없이도 대체 provider나 local mode로 동작한다.
- 쓰기로 한 sponsor마다 integration seam이 있다.
- 공개 문서로 구현할 수 있는 sponsor adapter는 구현되어 있다.
- credential이 없는 sponsor는 key/endpoint 주입과 실제 smoke test만 남아 있다.
- demo에 보여줄 핵심 화면의 디자인이 끝나 있다.
- 실행, 배포, reset 방법을 알고 있다.

sponsor 항목의 N/A는 위 Sponsor 사용 조건을 따른다. 채택 미정이나 요건 미확인을 미사용으로 간주하지 않는다.

사전 구현이 허용돼도 해커톤 당일에 제품 핵심 기능을 새로 만드는 상태는 제품 준비 완료가 아니다. 현장 제작만 허용되는 행사에는 이 사전 구현 완료 기준을 강제하지 않는다.

## Demo 계약

demo 파일의 schema는 프로젝트마다 다르다. 공통 필드를 강제하지 않는다.

`/demo`의 pre-event 실행은 `/design` 뒤, 제품 출력으로 시나리오를 판정하기 전에 contract에 독립적인 expected·출처·제품 유형별 검증 기준을 고정한다. `/prepare`에서 local/mock으로 재현하고 pre-event `/preflight`에서 검사한다. 현장 `/demo`에서는 같은 contract에 실제 결과와 evidence를 붙인다. 현장 결과에 맞춰 expected를 바꾸지 않는다. 근거 오류가 드러나면 ORACLE INVALID/UNVERIFIED로 격리한다. 독립 근거를 재검증해 수정하더라도 이번 행사에서 해당 scenario를 PASS 근거로 다시 사용하지 않고 한계로만 보고한다. 이전 버전과 변경 이유는 보존하고 새 기준은 향후 별도로 검증한다.

### Ground truth와 verdict

- expected 값은 제품이나 모델 출력을 보기 전에 독립된 명세·손 계산·외부 테스트 벡터 등으로 정하고 출처를 적는다. 제품이 생성한 expected, 그 값을 그대로 복제한 테스트, 모델의 다수결은 독립 근거가 아니다.
- verdict는 고정된 expected와 실제 결과를 비교해서 낸다.
- expected가 틀렸거나 독립 근거가 없으면 그 scenario는 ORACLE INVALID 또는 UNVERIFIED다. 제품의 문제 발견(예: collision)이나 제품 failure로 보고하지 않는다.
- 같은 모델이나 여러 모델이 같은 답을 반복해도 expected의 근거가 되지 않는다.
- demo에서 보여주는 surface(web UI, CLI, CI comment, API 응답 등)마다 해당 동작·주장에 맞는 검증 기준을 둔다. 판정 제품은 positive control(문제 입력 → 문제 판정)과 safe negative control(정상 입력 → 정상 판정)을 유지한다.
- 편집·계산 제품은 동작 결과와 보존되어야 할 상태(invariant)를 독립 명세로 고정한다. 예: 한 가구 이동 시 다른 가구와 방 유지, 초기화 시 보정 완료 상태 복귀. 검증을 위해 범위 밖 안전·충돌 판정을 추가하지 않는다.
- 복원·생성 제품은 출력 확인 전에 정한 평가 기준·독립 참조 자료·허용 오차로 검증한다. 객관적으로 확인하지 못한 품질 주장은 UNVERIFIED로 남긴다. 편집 조작 성공과 복원 품질은 별도 주장으로 나누며 서로의 검증을 대신하지 않는다. 혼합 제품에는 해당 기준을 함께 적용한다.
- 실패는 product failure, model error, infra error, oracle invalid로 나눠 기록한다.

### 발표 주장

deck, pitch, public guide, submission의 수치와 결과는 위 검증을 통과한 scenario와 실제 실행 evidence에서만 가져온다. ORACLE INVALID, UNVERIFIED scenario와 제외한 sponsor나 기능은 모든 산출물에서 빼거나 한계로만 적는다.

## 발표시간 계약

공식 발표시간이 확인되면 그 시간을 우선한다. 공식값이 없으면 출처 있는 사용자 확인 시간·범위 안에서 준비 목표를 정하고 공식 확인과 구분한다. 둘 다 없을 때만 발표·데모·화면 전환을 합친 준비용 기본 예산을 60초로 둔다. 60초는 공식 행사 규칙이 아니라 사용자 승인 준비 기본값이며, 공식 시간은 미확인으로 유지한다. Q&A가 별도인지 합산인지 확인하고 미확인은 임의로 분리하지 않는다. `/deck`과 `/pitch`는 같은 유효 시간과 출처를 사용해 장수·정보량·발화·데모·전환·여유 시간을 설계하고 실제 리허설과 시각 품질을 별도로 검수한다. 실제 발표시간이 나중에 확인되면 `/adapt`에서 기존 기본값/출처와 새 공식 시간/출처, Q&A 조건, 영향받는 자료를 기록한다. sponsor 변경이 없더라도 발표 조건 갱신은 adaptation의 유효한 작업이다. 실제 자료 수정은 해당 `/deck`·`/pitch` 범위의 승인 아래 진행하고, 기존 실행 증거와 독립 expected는 그대로 보존한다. 공식 안내가 행사 전에 도착하면 즉시 같은 갱신 절차를 적용하며 현장까지 기다리지 않는다. 시간 변경 후 deck·대본·demo cue·fallback을 함께 재검수하기 전에는 새 시간 기준 준비 완료라고 주장하지 않는다.

## 종료 후

`/retro`는 현재 행사 workspace에 상세 회고를 남긴다.

`/archive`는 직접 참가한 행사 링크를 `references/my-hackathons.md`에 추가한다. 수상작은 `references/winners.md`, 일반 출품작과 gallery는 `references/submissions.md`에 둔다. workspace는 삭제하지 않는다.

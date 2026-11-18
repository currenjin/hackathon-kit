# 규칙 기반 workflow 계약

공식 규칙과 사용자 작업 승인은 둘 다 필요하다. 사용자 승인은 공식 금지를 해제하지 않는다. 미확인은 허용이 아니다. 새 source는 원문을 실제 확인한 경우에만 기록하며 검색 snippet이나 과거 요약을 공식 확인으로 승격하지 않는다.

## 게시 권한

템플릿 사용은 게시 승인이 아니다. kit 작성자의 개인 승인이나 다른 사용자의 관행을 현재 사용자에게 이전하지 않는다. 작업 중 처음 게시가 필요할 때 로컬 수정 / stage·commit / push 범위와 대상 저장소·branch·경로를 확인하고, 현재 대화 또는 기존 작업 승인 기록에 남긴다. 새 YAML 필드나 별도 승인 파일을 필수로 만들지 않는다.

이미 확인한 승인 안의 반복 작업은 매 command마다 재승인을 요구하지 않는다. 범위가 바뀌거나 불명확하면 그 부분만 확인하며, 현재 사용자의 명시적 금지와 보호 경로가 우선한다. 게시 승인 미확인 시 허용된 로컬 작업은 계속하고 stage·commit·push만 보류한다. 기록 작성·제품 구현·외부 제출·팀 채널 게시·공개 전환의 승인은 서로 대체하지 않는다.

승인된 게시만 명시 경로·hunk로 분리해 staged diff를 검수하고 커밋·푸시한다. 기존 index·다른 작업자 변경·secret·개인정보·권한 없는 원본·생성 캐시는 제외한다. 빈 커밋은 만들지 않으며 실패하면 작업을 보존하고 미게시 범위를 보고한다. 게시 후 정확한 remote branch SHA를 로컬 commit과 대조한다. tag·reset·force push·branch 생성/삭제·공개 전환·앱 복원은 별도 승인 경계를 유지한다.

## 참가 방식과 역할

모든 command는 [참가 방식과 본인 역할](team-participation.md)을 먼저 적용한다. 새 세션의 본인 선택과 매 command의 정본 재확인을 통해 주 역할을 우선순위로 유지하되 전체 목표·공유 명세·통합과 다른 역할 기여를 계속 고려한다. 개인 참가와 unknown·종료된 행사의 읽기 전용 범위, `/onboard`의 신규 본인 등록 예외도 이 계약을 따른다.

## 정책과 기록

[템플릿](../templates/hackathon.yaml)의 `build_policy`를 사용한다. 기존 workspace는 migration하지 않고 누락 필드를 unknown으로 읽는다. 필요한 현재 행사 필드만 확인 후 기록한다.

- `prebuild-permitted`: 공식 사전 제작 허용. 허용된 행위와 시점, 별도 사용자 작업 승인 안에서만 제작한다.
- `on-site-build-only`: 사전 제작 금지. 공식 제작 시작 이후 종료 전, 행위별 규칙과 사용자 승인 아래 새로 제작한다.
- `restricted-preparation`: 허용 범위 미확인. 출품용 제작은 보류하고 규칙 조사와 확인된 저위험 준비만 한다.

`source`는 모드 판정 원문 위치, `checked_at`은 실제 확인 시각이다. `starts_at`/`ends_at`은 timezone offset이 있는 공식 제작 시간이며 행사 입장·등록·제출 시간과 구분한다. 모르면 null이다. `pre_event`의 planning/design/prompt/data/criteria/code/deck/pitch/submission은 각각 allowed/forbidden/unknown이며 기본 unknown이다. 코드 허용에서 다른 행위 허용을 추론하지 않는다. 각 행위의 출처·인용·범위는 `notes`에 남긴다. 코드 재사용은 아이디어 적합성과 별개로 `code_reuse`에 같은 세 상태로 기록한다. 제작 가능 시점이 미확인이면 제작하지 않는다.

## 전체 흐름과 breadcrumb

아래 화살표는 위치 안내이지 자동 다음 단계 실행 승인이 아니다. 시작·중간·종료 첫 줄에는 해당 분기의 연속 구간과 현재 실제 상태를 표시한다. Markdown 인용문을 쓰고 실제 완료 근거가 있는 단계만 굵게 쓴다. 보조 command는 현재 구간 옆에 대상과 상태를 붙인다. N/A는 제품 PASS가 아니며 unknown은 RISK다.

### prebuild-permitted

/init → /ideate(사용자 선택) → /demo criteria → /design(시각 승인·구현) → /prepare → /preflight pre-event → /adapt(필요한 실제 연결) → /demo verify → /deck → /pitch → /submit draft → /preflight final → 사용자 실제 제출 → 발표 → /retro → /archive

criteria는 제품 제작 전에 수립한다. 설계 초안은 행위 허용 범위 안에서 criteria보다 먼저 검토할 수 있으나 실제 UI 구현은 criteria 이후다. deck/pitch/submission의 사전 작성도 각각 허용을 확인한다. verify는 실제 실행 환경이 갖춰지면 행사 전에도 가능하며 local/mock과 실제 provider evidence를 구분한다.

### on-site-build-only

행사 전: /init → 허용된 /ideate 재평가·제품 명세 → /design(허용된 사전설계 검토) → 허용된 현장 실행 계획 → /preflight pre-event(preparation readiness)

사전설계 검토는 planning/design 허용·사용자 승인 범위에서만 수행하며 `/design`의 제품 UI 구현 완료가 아니다. 제품 명세·화면·상태 설계·검토·현장 실행 계획을 기준으로 준비를 점검하고, 금지된 코드·prompt·fixture나 사전 실계정 호출을 필수 산출물로 요구하지 않는다. 행위가 금지·미확인이면 그 부분을 보류하고 가능한 점검만 한다.

공식 제작 시작 후: /ideate(필요 시 사용자 재선택) → /adapt(최초 계정 설정이 선행할 때만) → /demo criteria → /design(시각 승인·구현) → /prepare(현장 신규 구현) → /adapt(실제 연결 필요 시) → /demo verify → /deck → /pitch → /submit draft → /preflight final → 사용자 실제 제출 → 발표 → /retro → /archive

사전 planning/design/prompt/data/criteria/deck/pitch/submission을 일괄 허용하지 않는다. 현장 시작만으로 모든 행위가 허용되는 것도 아니다. 기존 코드 재사용 자격은 별도로 확인한다.

### restricted-preparation

/init(부분완료·출처 확인 대기) → 허용된 비차단 검토 /ideate → /preflight pre-event(unknown은 RISK) → 규칙 확인 → 해당 분기 재개. 출품용 구현·금지/미확인 자료 작성은 보류한다. 과거 기록 검토와 규칙 차이 분석은 진행하되 금지된 새 아이디어·설계 작성으로 확장하지 않는다.

어느 분기든 조건 변경 → /replan[/init 재확인 실제 수행 → /ideate 전체 재평가 실제 수행 → recommendation·사용자 결정 대기] → 허용된 단계 재개다. 자동실행금지의 유일한 이 예외는 승인된 replan 내부 init+ideate의 조사·기록·추천 범위다. 구현·제품선택·명칭·sponsor 채택·다른 command 실행까지 확대하지 않는다.

## 제출 후 선정되는 발표

제출 뒤 대표·결선 발표를 선정하는 행사는 [현장 상태 계약](field-status-and-closeout.md#제출과-조건부-발표)을 적용한다. `/submit draft → /preflight final(제출 범위) → 사용자 실제 제출 → 선정 대기 → 선정 후 /adapt → 필요한 /deck·/pitch → /preflight final(발표 범위) → 발표`로 범위를 나눈다. 제출물에 필수인 영상·발표 자료 검수와 제품 검증은 생략하지 않는다. 선정 대기는 발표 ready가 아니며 이 분기는 다음 command 자동 실행 승인이 아니다.

## 사후 기준과 인계

이미 구현된 제품을 인계받았거나 criteria를 구현 뒤 작성했다면 그 시점과 기준 작성자가 본 코드·화면·actual 범위를 기존 contract나 검증 보고에 기록한다. 새로운 필드나 별도 파일은 필수가 아니다. 사후 기능 점검을 수행할 수 있지만 사전 독립 acceptance 완료로 표시하지 않는다.

선행 명세의 고정 버전·작성 시점·출처로 확인되는 조건은 그 조건에 한정한 명세 적합 관찰로 보고한다. 선행 출처 없이 구현 뒤 정한 조건은 사후 기능 점검으로 표시하고, 정답·품질의 독립 근거가 없으면 UNVERIFIED다. 다른 모델의 재검토만으로 기준의 사전성이 복구되지는 않는다. 발표 자료의 기능 설명과 관찰에는 이 범위를 밝히고 사전 독립 검증 성과나 `/demo` acceptance PASS로 포장하지 않는다.

기존 expected·input·허용 오차와 과거 결과는 보존한다. ORACLE INVALID 또는 UNVERIFIED로 격리한 scenario의 기준을 고쳐 이번 행사 PASS로 되살리지 않는다. 유효한 실제 관측도 삭제하지 않고 사전 독립 acceptance, 선행 명세 적합 관찰, 사후 기능 점검을 구분한다. 이 경로는 oracle 격리나 기존 자료의 성과 주장 제한을 해제하지 않는다.

## 완료와 역사

종료 후 `/retro`·`/archive`에는 `AGENTS.md`의 사실 기반 작업 회고 규칙과 [기록 완료와 운영 종료](field-status-and-closeout.md#기록-완료와-운영-종료)를 적용한다. 기존 workspace·evidence·결과·발표 사용자 보고로 사실 기록을 완료하며 소감·감상·필수 인터뷰를 gate로 두지 않는다. 소감 부재·거절만으로 빈 감상 섹션이나 `reflection_pending`을 만들거나 대기·부분완료로 낮추지 않는다. 사실 누락은 미확인, 실제 해당하지 않는 경우만 근거와 함께 비해당으로 남긴다. 기록 완료와 제품 검증·실제 제출·운영 종료는 별도이며 기존 승인·소유·역사 보존 계약을 유지한다.

preparation readiness는 허용된 준비의 점검 결과이고 product readiness는 실제 제품 구현·독립 기준 검증 결과다. 전자를 후자의 PASS로 표시하지 않는다. 현재 신규 출품물의 결과 주장은 자격이 확인된 최신 build의 실제 evidence만 쓴다. 과거 evidence와 제출 사실, oracle 오류 이력은 지우지 않는다. 이름·repo·commit 시각 변경으로 기존 제작을 신규 제작으로 위장하지 않는다.

사전 준비 완료 판정에는 [사전 준비 완료 기준](pre-event-readiness.md)을 적용한다. 제품 명세, 화면·상태 설계와 사용자 검토·walkthrough, 현장 실행 계획을 확인하며 스타터 준비만으로 대체하지 않는다. 핵심 결정이나 검토가 남으면 사전 준비 미완료다.

제품 계획 준비·실행환경 준비·현장 확인 대기·실제 제품 검증을 분리한다. 지급 전 계정·실모델·실배포는 사전 확인 불가 이유·독립 판정·최초 확인·실패 대응·축소 조건을 갖추면 현장 확인 대기로 남겨도 된다. 준비 가능한 핵심 설계를 계정 부재로 미루거나 불가능한 사전 실호출을 강제하지 않는다.

공식 금지·허용 미확인 때문에 필수 산출물을 만들 수 없으면 공식 제한으로 준비 범위만 점검한 것이며 전체 준비 완료가 아니다. 이 기준은 kit 운영 기준이고 공식 행사 규칙이 아니다. command 수정 자체는 행사 설계 승인·구현·후속 command 실행이나 과거 완료 상태 변경을 뜻하지 않는다.

## AGENTS.md의 적용 한계

AGENTS.md와 본 계약을 함께 읽는다. 기본 원칙 2, 사전 제작 경계와 행사 전 완료 기준은 공식 규칙과 승인 범위에 종속되므로 on-site-build-only에서 사전 구현을 요구하지 않는다. 기존 제품을 먼저 읽는 것은 조사 순서이지 새 규칙 재평가의 우선 채택권이 아니다. 독립 expected·control·oracle 격리, 소유·복구와 저장소 이름·설명 규칙은 유지한다.

Demo 입출력은 criteria/verify 역할로 읽고 pre-event/on-site는 호환별칭으로만 사용한다. `/adapt`의 preparation 필수 입력은 해당 command에 적힌 제한된 환경설정 예외를 함께 읽는다. 이 예외나 다른 권한의 적용을 확정할 수 없으면 해당 실행만 충돌로 보류하고 가능한 조사·기록은 계속한다.

종료 게시에는 위 게시 권한을 적용한다. 공통 파일 유지보수 요청은 행사 command 실행이나 workspace·제품 변경 승인이 아니며 현재 사용자의 명시적 stage/commit/push 금지와 보호 경로가 우선한다.

## 정적 검증

`python -B -m unittest discover -s tests -v`는 문서 문자열·frontmatter·상대 링크 및 정책 fixture의 정적 계약 검사다. 모델이 지시를 실제 이행하는 실행 test가 아니다. YAML 검사는 PyYAML이 있는 환경에서 수행한다. fixture는 합성 테스트 데이터이며 실제 행사 규칙 확인 근거가 아니다.

회원 저장 CLI 검사는 임시 합성 행사에서 실제 파일 생성·선택·수정·거부를 실행한다. 참가 방식·질문 분기·모든 command로의 전파는 정적 계약 검사이며 native 질문 화면이나 모델의 실제 이행을 검증하지 않는다.

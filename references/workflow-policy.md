# 규칙 기반 workflow 계약

공식 규칙과 사용자 작업 승인은 둘 다 필요하다. 사용자 승인은 공식 금지를 해제하지 않는다. 미확인은 허용이 아니다. 새 source는 원문을 실제 확인한 경우에만 기록하며 검색 snippet이나 과거 요약을 공식 확인으로 승격하지 않는다.

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

## 완료와 역사

preparation readiness는 허용된 준비의 점검 결과이고 product readiness는 실제 제품 구현·독립 기준 검증 결과다. 전자를 후자의 PASS로 표시하지 않는다. 현재 신규 출품물의 결과 주장은 자격이 확인된 최신 build의 실제 evidence만 쓴다. 과거 evidence와 제출 사실, oracle 오류 이력은 지우지 않는다. 이름·repo·commit 시각 변경으로 기존 제작을 신규 제작으로 위장하지 않는다.

사전 준비 완료 판정에는 [사전 준비 완료 기준](pre-event-readiness.md)을 적용한다. 제품 명세, 화면·상태 설계와 사용자 검토·walkthrough, 현장 실행 계획을 확인하며 스타터 준비만으로 대체하지 않는다. 핵심 결정이나 검토가 남으면 사전 준비 미완료다.

제품 계획 준비·실행환경 준비·현장 확인 대기·실제 제품 검증을 분리한다. 지급 전 계정·실모델·실배포는 사전 확인 불가 이유·독립 판정·최초 확인·실패 대응·축소 조건을 갖추면 현장 확인 대기로 남겨도 된다. 준비 가능한 핵심 설계를 계정 부재로 미루거나 불가능한 사전 실호출을 강제하지 않는다.

공식 금지·허용 미확인 때문에 필수 산출물을 만들 수 없으면 공식 제한으로 준비 범위만 점검한 것이며 전체 준비 완료가 아니다. 이 기준은 kit 운영 기준이고 공식 행사 규칙이 아니다. command 수정 자체는 행사 설계 승인·구현·후속 command 실행이나 과거 완료 상태 변경을 뜻하지 않는다.

## AGENTS.md의 적용 한계

AGENTS.md는 보호된 파일이며 이 변경에서 수정하지 않았다. 기본 원칙 2, 사전 제작 경계, 행사 전 완료 기준은 공식 규칙과 승인 범위에 종속되어 있으므로 on-site-build-only에서는 사전 구현 요구가 적용되지 않는다. 기존 제품을 먼저 읽는 것은 조사 순서이지 새 규칙 재평가의 우선 채택권이 아니다. 독립 expected·control·oracle 격리, 소유·복구, 저장소 이름·설명 규칙은 유지한다.

다만 AGENTS의 Command 입출력 표와 Demo 계약에는 pre-event/on-site라는 옛 시간 명칭 및 adapt의 preparation 필수 입력이 남아 있다. 이들은 본 계약의 criteria/verify 역할과 adapt의 제한된 환경설정 예외로 명시적으로 정정한 command를 함께 읽어야 한다. 이 문서가 AGENTS를 수정했다거나 충돌이 사라졌다고 주장하지 않는다. 권한 체계상 예외 적용을 확정할 수 없으면 해당 실행만 충돌로 보류하고 가능한 조사·기록은 계속한다.

종료 게시의 상시 승인보다 현재 사용자의 명시적 stage/commit/push 금지와 보호 경로가 우선한다. 공통 파일 유지보수 요청은 행사 command 실행이나 workspace·제품 변경 승인이 아니다.

## 정적 검증

`python -B -m unittest discover -s tests -v`는 문서 문자열·frontmatter·상대 링크 및 정책 fixture의 정적 계약 검사다. 모델이 지시를 실제 이행하는 실행 test가 아니다. YAML 검사는 PyYAML이 있는 환경에서 수행한다. fixture는 합성 테스트 데이터이며 실제 행사 규칙 확인 근거가 아니다.

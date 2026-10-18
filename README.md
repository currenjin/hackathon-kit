# hackathon-kit

[English](README.en.md) · 한국어

해커톤에서 반복해서 쓰는 규칙, 커맨드, 템플릿, 레퍼런스를 모아 둔 저장소다.

제품 자체는 각 Git 저장소 또는 소유 계정이 확인된 hosted app에서 개발한다. `hackathon-kit`은 행사 선택, sponsor 준비, demo, deck, pitch, submission, 회고를 돕는다.

## Workspace

행사별 작업은 `workspace/<event-slug>/`에 저장한다.

```
workspace/
└─ <event-slug>/
   ├─ hackathon.yaml
   ├─ ideation.md
   ├─ design.md
   ├─ preparation.md
   ├─ preflight-pre-event.md
   ├─ adaptation.md
   ├─ <demo contract>               # 경로는 hackathon.yaml의 demo_contract
   ├─ preflight-final.md
   ├─ retro.md
   └─ output/
```

workspace는 Git에 커밋할 수 있는 상태로 유지하고, 커밋과 푸시는 필요할 때 직접 한다. 다음 해커톤을 시작해도 이전 행사 폴더는 그대로 남긴다. 이전 행사 폴더를 새 구조로 옮기지 않는다.

API key, secret, 개인 정보는 workspace에 넣지 않는다. 환경 변수나 로컬 secret store를 사용한다.

## References

레퍼런스는 `references/` 아래에서 관리한다.

- `references/my-hackathons.md`: 내가 참가한 해커톤
- `references/winners.md`: 수상작
- `references/submissions.md`: 전체 출품작 gallery와 일반 출품작 링크
- [발표 레퍼런스 가이드](references/presentation-reference-guide.md): 출처별 적용 한계, 1분 준비 기본값, 대표 렌더 검토와 시간 변경 흐름
- [사전 준비 완료 기준](references/pre-event-readiness.md): 제품 명세, 화면·상태 설계와 검토, 현장 실행 계획의 완료 gate. 스타터 준비와 제품 검증을 분리한다
- [현장 상태와 종료 점검](references/field-status-and-closeout.md): 조건부 발표, 사용자 확인 상태, 공개 범위와 운영 종료, 읽기 전용 일관성 검사
- [자료와 실행 기록 인계](references/delivery-handoffs.md): 기존 사실표·runbook·slide map을 재사용해 여러 자료의 사실과 실행 증거를 연결한다
- [Command별 추천 모델](references/model-routing.md): 주도·검토 모델과 사람이 정할 것. 추천 모델이 없어도 알리고 이어서 진행한다
- [발표자 도구](tools/presenter/README.md): 청중 창과 발표자 창(현재·다음 슬라이드, 할 말, 타이머). `/present`가 행사별 덱 폴더를 만든다
- [조건부 스타터 레퍼런스](references/starter-references.md): 제품에 필요한 경우만 가이드와 코드 스타터를 검토한다. 기본 스택이나 설치를 강제하지 않는다
- [합성 작성 예시](examples/synthetic-handoff.md): 제품 명세·현장 실행표·공통 사실표·심사 기준별 증거의 작성 방법. 실제 행사 evidence가 아니다

공통 양식은 [사실표](templates/project-facts.md), [현장 실행표](templates/execution-plan.md), [심사 기준별 증거](templates/judging-evidence.md)에 있다. 기존 행사 문서에 필요한 절만 사용하며 파일 수를 완료 조건으로 만들거나 과거 workspace를 migration하지 않는다.

## Flow

진행 중인 kit을 이어받았거나 새 세션이면 먼저 [`/onboard`](.claude/commands/onboard.md)로 끝나지 않은 행사 중 하나를 고르고, 지금까지의 기록과 남은 일·다음 command를 파악한다.

[workflow 계약](references/workflow-policy.md)을 모든 command에 적용한다. `build_policy`는 공식 제작 허용 모드·제작 시간·출처와 행위별 사전 허용을 기록한다. planning/design/prompt/data/criteria/code/deck/pitch/submission은 각각 확인하며 unknown은 허용이 아니다. 기존 workspace는 migration하지 않는다. 화살표와 breadcrumb는 위치 안내이지 자동 실행 승인이 아니다.

### Rules or assumptions changed

[`/replan`](.claude/commands/replan.md)은 현재 workspace에서 `/init` 재확인과 `/ideate` 전체 재평가를 실제 수행하는 orchestration이다. 실행 승인은 두 하위 단계의 조사·기록·recommendation까지 포함한다. 하위 command 자동실행금지의 예외는 이 범위뿐이며 init/ideate를 안내만 하고 종료하지 않는다.

```text
/replan → /init 재확인 실제 수행 → /ideate 전체 재평가 실제 수행
        → 산출물·완료 상태 재편 → recommendation → 사용자 결정 대기
```

/init 재확인은 동일 URL·날짜의 workspace를 유지한다. 일반 초기화의 빈칸만 채우기와 달리 변경값·이전값·출처·확인 시각 이력을 보존해 갱신한다. 새 공식 트랙·필수 기술·심사 기준으로 기존 아이디어 유지/수정/새 후보를 비교하며 코드 재사용 자격은 별도로 평가한다. 기존 선택은 보존하되 재평가 대기로 표시한다.

제품 선택·명칭·sponsor 채택은 사용자 결정이다. 구현·다른 command·계정 생성·배포·제출은 자동 실행하지 않는다. 규칙/출처 미확인이면 가능한 비차단 검토는 수행하고 막힌 하위항목은 부분완료로 남긴다. 허용을 추론하거나 과거 evidence를 신규 출품 결과로 재사용하지 않는다.

### prebuild-permitted: 공식 사전 제작 허용

```text
/init → /ideate(사용자 선택) → /demo criteria(독립 expected·control)
→ /design(시각 승인·실제 UI) → /prepare → /preflight pre-event
→ /adapt(필요한 실제 연결) → /demo verify → /deck → /pitch
→ /submit draft → /preflight final → 사용자 실제 제출 → 발표
→ /retro → /archive
```

각 행위의 공식 허용과 작업 승인을 확인한다. criteria는 제품 제작 전에 수립하며 허용된 설계 초안은 먼저 검토할 수 있다. 사전 deck·pitch·submission은 각각 허용 확인 후 작성한다. verify는 실행 환경이 준비되면 행사 전에도 가능하고 실제 provider와 local/mock을 구분한다.

### on-site-build-only: 공식 사전 제작 금지

```text
행사 전: /init → 허용된 /ideate·제품 명세 → /design(허용된 사전설계 검토)
         → 허용된 현장 실행 계획 → /preflight pre-event
         (기획·설계·사용자 검토·실행계획과 환경 점검, 제품 PASS 아님)
공식 제작 시작 후:
/ideate(필요 시 사용자 재선택) → /adapt(최초 계정 설정이 선행할 때만)
→ /demo criteria → /design(시각 승인·실제 UI) → /prepare(현장 신규 구현)
→ /adapt(필요한 실제 연결) → /demo verify → /deck → /pitch
→ /submit draft → /preflight final → 사용자 실제 제출 → 발표
→ /retro → /archive
```

금지 행사에서는 criteria도 공식 시작 후 수립할 수 있다. `/adapt`의 신규 구현 금지는 그 command의 역할 제한이며 현장 `/prepare`까지 막지 않는다. preparation.md 없는 최초 환경설정 예외는 제품 수정·E2E가 아닌 설정 점검과 adaptation 기록만 포함한다. 제품 변경 시 기존 소유·승인·보존·복구 계약을 유지한다.

### restricted-preparation: 미확인

/init 부분완료 → 가능한 비차단 /ideate 검토 → /preflight pre-event(unknown은 RISK) → 공식 확인 후 해당 분기 재개. 출품용 제작과 미확인 사전 행위는 보류한다. preparation readiness와 product readiness를 분리하며 N/A는 제품 PASS가 아니다.

`/demo pre-event`는 `criteria`, `/demo on-site`는 `verify`의 호환별칭이다. 별칭은 시점 허가가 아니다. 실제 출력으로 expected를 역산하지 않으며 oracle 오류·control의 엄격한 기존 규칙을 유지한다.

공식 발표시간 미확인 시 공식값은 null로 유지하고 출처 있는 사용자 확인 시간·범위를 따른다. 둘 다 없을 때만 준비 예산60초를 쓴다. 공식 시간이 확인되면 우선하고 Q&A none은 확인 근거와 0초를 기록한다. 대표 시안 승인·전체 렌더·실제 리허설을 유지하며 장수는 강제하지 않는다. 기존 deck·workspace 자동 재생성은 하지 않는다.

제출 뒤 대표·결선 발표를 선정하는 행사는 [조건부 발표 분기](references/field-status-and-closeout.md#제출과-조건부-발표)를 적용한다. 제출 범위 final 검수와 선정 후 발표 범위 검수를 구분하며, 제출 완료를 발표 ready로 올리지 않는다.

### After the hackathon

```
/retro
  ↓
/archive
```

상세 작업 기록은 `workspace/<event-slug>/`에 보존하고, 다음에 다시 볼 링크만 `references/`에 남긴다.

운영 규칙과 command 입출력은 `AGENTS.md`를 본다.

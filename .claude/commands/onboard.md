---
description: kit을 처음 받거나 새 세션에서 진행 중인 해커톤의 현재 상태·남은 일·다음 할 일을 파악한다
---

## 실행 표시

다른 command와 같은 breadcrumb 규칙([workflow 계약](../../references/workflow-policy.md))을 따른다. 흐름 첫 줄은 Markdown 인용문(`> `)으로 표시한다. 시작에 `/onboard · 시작 | 행사 slug 또는 행사 미확정`, 종료에 `/onboard · 완료 | 행사 slug | 브리핑 | 다음 command와 추천 모델`을 표시한다. 다음 command는 안내만 하고 자동 실행하지 않는다.

## 하는 일

읽기만 한다. 제품 코드·행사 기록·kit 파일을 고치지 않는다. 결과는 사용자에게 브리핑으로 보고하고, 사용자가 원하면 `workspace/<event-slug>/onboarding-<YYYY-MM-DD>.md`로 남긴다.

## 1. kit 규칙 익히기

1. `AGENTS.md`, `CLAUDE.md`를 읽는다.
2. `references/workflow-policy.md`, `references/model-routing.md`를 읽는다.
3. `.claude/rules/`의 글쓰기·언어·디자인 규칙 목록을 확인한다(본문은 필요할 때 읽는다).
4. `.claude/commands/`의 command 이름과 description만 훑는다.

## 2. 진행할 해커톤 고르기

사용자가 slug를 이미 말했으면 그 workspace를 쓴다. 아니면 **사용자가 고르게 한다.** 후보가 하나여도 확인을 받는다.

1. `workspace/` 아래에서 **끝나지 않은 행사**만 모은다. 끝난 행사는 `retro.md`가 있거나, `hackathon.yaml`에 `result`가 있거나, `references/my-hackathons.md`에 연결된 workspace다.
2. 후보마다 한 줄로 보여 준다: slug · 행사 이름 · `event.date` · 현재 단계(`hackathon.yaml` notes 최신 줄 기준) · 마지막 커밋 날짜.
3. 사용자가 고를 때까지 기다린다. 후보가 없으면 `/init`으로 새 행사를 만들자고 안내하고 멈춘다.
4. 끝난 행사를 보고 싶다고 하면 읽기 전용으로만 연다.

## 3. 지금까지의 작업 파악

현재 행사 workspace에서 아래를 읽고 사실만 모은다.

- `hackathon.yaml`: 일정·마감·제출 URL·발표 시간·언어·`build_policy`·`product`·`public_links`·`notes`(최신이 위). 해커톤 종료 후 할 일 같은 예약 작업도 notes에 있다.
- 최근 기록: `git log --oneline -30 -- workspace/<event-slug>/`와 최근 수정 파일. 커밋 SHA가 재작성된 적이 있으면 `sha-rewrite-*.md`로 옛 SHA를 새 SHA로 바꿔 읽는다.
- 단계별 산출물: `ideation*`, `selection*`, `product-spec-current.md`, `demo-criteria-*`·`demo-*.json`, `design*`, `preparation*`, `demo-reference/`(다른 모델의 검토·판정 원문), `output/`(submission·deck·pitch·presenter).
- 제품 위치: `product.repository`의 branch·HEAD·remote 일치, 배포 URL이 있으면 응답 여부. 비밀값은 열지 않는다.

## 4. 남은 일 정리

[현장 상태와 종료 점검](../../references/field-status-and-closeout.md)을 함께 읽는다. 현재와 과거 상태, 사용자 보고와 직접 확인을 구분한다. 필요한 경우 읽기 전용 `tools/workflow_checks.py`로 명시한 workspace와 검사 범위의 진단을 확인하되 결과를 제품 PASS로 쓰거나 과거 기록을 자동 수정하지 않는다.

- 각 command의 실제 상태를 breadcrumb 규칙으로 판정한다. 파일이 있다는 이유로 완료로 올리지 않는다.
- 아직 미확인·대기·FAIL·UNVERIFIED로 남은 항목, 다른 모델의 검토가 지적했지만 반영 안 된 항목, 사용자 결정 대기를 모은다.
- 마감과 일정(제작 종료·제출·발표·결과)을 현재 시각과 비교해 남은 시간을 적는다.

## 5. 브리핑

아래 순서로 짧게 보고한다.

1. 행사와 지금 단계(breadcrumb 한 줄)
2. 제품 한 줄과 위치(저장소, 배포, 영상)
3. 확정된 것 3–5개(근거 파일)
4. 남은 일과 막힌 것(우선순위순, 근거 파일)
5. 사용자 결정이 필요한 것
6. 다음 command와 [추천 모델](../../references/model-routing.md). 추천 모델이 지금 세션이 아니어도 "이어서 진행할 수 있다"고 안내한다.

추측으로 빈칸을 채우지 않는다. 기록에서 확인하지 못한 것은 미확인으로 적는다.

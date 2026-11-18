---
description: kit을 처음 받거나 새 세션에서 진행 중인 해커톤의 현재 상태·남은 일·다음 할 일을 파악한다
---

## 실행 표시

다른 command와 같은 breadcrumb 규칙([workflow 계약](../../references/workflow-policy.md))을 따른다. 흐름 첫 줄은 Markdown 인용문(`> `)으로 표시한다. 시작에 `/onboard · 시작 | 행사 slug 또는 행사 미확정`, 종료에 `/onboard · 완료 | 행사 slug | 브리핑 | 다음 command와 추천 모델`을 표시한다. 다음 command는 안내만 하고 자동 실행하지 않는다.

## 하는 일

읽기 전용을 기본으로 하며 제품 코드·공유 행사 설정·evidence·kit 파일을 고치지 않는다. 좁은 예외는 아래 응답 절차를 거친 신규 본인 등록이며, 기존 기록 선택은 회원 파일도 다시 쓰지 않는다. 결과는 사용자에게 브리핑으로 보고하고, 사용자가 원하면 `workspace/<event-slug>/onboarding-<YYYY-MM-DD>.md`로 남긴다.

## 1. kit 규칙 익히기

1. `AGENTS.md`, `CLAUDE.md`를 읽는다.
2. `references/workflow-policy.md`, `references/model-routing.md`를 읽는다. 게시 권한은 현재 사용자의 기존 승인 기록에서 확인하되 템플릿의 과거 문구로 승인을 추정하지 않는다. 읽기 전용 브리핑을 위해 새 게시 승인이나 공유 설정 변경을 요구하지 않는다.
3. `.claude/rules/`의 글쓰기·언어·디자인 규칙 목록을 확인한다(본문은 필요할 때 읽는다).
4. `.claude/commands/`의 command 이름과 description만 훑는다.

## 2. 진행할 해커톤 고르기

사용자가 slug를 이미 말했으면 그 workspace를 쓴다. 아니면 **사용자가 고르게 한다.** 후보가 하나여도 확인을 받는다.

1. `workspace/` 아래에서 **끝나지 않은 행사**만 모은다. 끝난 행사는 `retro.md`가 있거나, `hackathon.yaml`에 `result`가 있거나, `references/my-hackathons.md`에 연결된 workspace다.
2. 후보마다 한 줄로 보여 준다: slug · 행사 이름 · `event.date` · 현재 단계(`hackathon.yaml` notes 최신 줄 기준) · 마지막 커밋 날짜.
3. 사용자가 고를 때까지 기다린다. 후보가 없으면 `/init`으로 새 행사를 만들자고 안내하고 멈춘다.
4. 끝난 행사를 보고 싶다고 하면 읽기 전용으로만 연다.

## 2-1. 본인 역할 확인

행사를 고른 뒤 [참가 방식과 본인 역할](../../references/team-participation.md)의 native 질문·CLI·세션 연결 규칙을 적용한다. 종료된 행사 열람은 이 등록 절차와 세션 연결 변경을 건너뛴다. `participation.mode: individual`이면 모든 역할 질문을 건너뛰며, 누락·unknown이면 개인/팀을 추정하지 않고 읽기 전용 브리핑을 계속할 수 있다.

확인된 `team`이면 먼저 실행 환경을 확인한다. Windows에서는 WSL의 Linux 환경을 안내하며 native Windows Python으로 저장 CLI를 실행하지 않는다. 지원 환경에서 CLI `list`로 실제 회원 기록을 읽는다. 기록이 없으면 등록 여부 질문 없이 바로 신규 등록 역할 질문으로 간다. 기록이 있으면 다음 질문을 각각 응답 뒤 분기한다.

1. **이번 팀에 본인의 주 역할을 이미 등록했나요?** 선택지: `예, 등록했어요` / `아니요, 처음 등록해요`.
2. 예이면 **본인에 해당하는 팀원 기록을 선택하세요.** 선택지는 실제 `<member-id> (<main-role>)` 목록과 `내 기록이 없어요`다. host 한도에 맞춘 페이지 탐색은 공통 계약을 따르며 회원을 지어내지 않는다.
3. 아니요 또는 내 기록이 없어요이면 공통 계약의 **이번 팀에서 주로 맡을 역할은 무엇인가요?**를 묻고 본인 ID 확인 후 CLI `register`로 신규 본인 등록을 수행한다. ID가 이미 있으면 덮어쓰지 않고 기존 선택으로 돌아간다.
4. 기존 기록 선택은 의도적인 본인 확인으로 처리하고 CLI `read`로 정본을 읽는다. 선택한 행사·본인 연결만 세션 안에서 갱신하며 `hackathon.yaml`·기존 회원·evidence는 변경하지 않는다.

취소·빈 응답이면 등록·선택을 완료로 간주하지 않는다. 역할 미확인 상태를 밝히고 가능한 읽기 전용 브리핑만 이어가며 다음 command는 자동 실행하지 않는다.

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

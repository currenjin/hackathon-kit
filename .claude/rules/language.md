# Language

언어는 현재 행사 설정인 `workspace/<event-slug>/hackathon.yaml`의 `language`를 따른다. 번역·public guide 작성도 [workflow 계약](../../references/workflow-policy.md)의 행위별 허용과 제작 시간을 적용하며 언어 요구가 사전 제작 허가를 뜻하지 않는다.

## Artifact 선택

- pitch는 기본적으로 `presenter` 언어로 만든다.
- deck, submission, public guide는 각각 설정된 언어로 만든다.
- public guide는 기존 `/pitch`가 `workspace/<event-slug>/output/guide/<lang>.md`에 작성한다. 파일 생성만으로 공개했다고 기록하지 않는다.
- 발표 언어와 청중 언어가 다르면 `public_guide`를 우선 준비한다.
- 여러 언어를 한 화면에 섞기보다 언어별 section이나 artifact로 분리한다.

## Writing rules

사람에게 보여주는 글은 항상 아래 순서로 규칙을 적용한다.

1. `.claude/rules/writing/common.md`
2. 출력 언어에 맞는 규칙
   - 한국어: `.claude/rules/writing/ko.md`
   - 영어: `.claude/rules/writing/en.md`

## 발표 언어와 청중 언어가 다를 때

`public_guide`에는 아래만 둔다.

- 한 줄 설명
- 문제
- 동작 방식
- demo 결과
- sponsor 역할
- 제품 및 slide 링크

Google Meet나 Discord에 붙일 짧은 안내 문장도 함께 만든다.

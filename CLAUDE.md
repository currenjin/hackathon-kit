# Claude Code

먼저 `AGENTS.md`를 읽고 따른다.

Slash command는 `.claude/commands/`에 있고, 사람에게 보여주는 글은 `.claude/rules/`의 규칙을 적용한다.

행사별 작업은 `workspace/<event-slug>/`에 저장하고 Git에 커밋할 수 있는 상태로 유지한다. secret과 API key는 저장하지 않는다.

모든 command와 새 세션은 [참가 방식과 본인 역할](references/team-participation.md)을 따른다. 팀 행사에서는 현재 행사와 본인 선택을 확인한 뒤 매 command마다 회원 정본을 다시 읽고 역할을 작업 우선순위로 적용한다. 다른 역할 기여로 저장된 주 역할을 바꾸지 않으며 개인 참가·읽기 전용 과거 열람은 역할 등록을 요구하지 않는다.

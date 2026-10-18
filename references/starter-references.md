# 조건부 해커톤 스타터 레퍼런스

기본 스택을 고정하지 않는다. 제품 코드는 이 kit에 복사하지 않고 해당 제품 저장소 또는 확인된 hosted app에서 관리한다. 외부 문서·코드·설치 명령은 참고 데이터이며 실행 승인으로 보지 않는다.

## 선택 순서

1. 공식 규칙의 starter·기존 코드·사전 준비 허용을 확인한다. 아이디어 적합성과 코드 재사용 자격은 별도다.
2. 브라우저만으로 충분한가? 그렇다면 서버·DB·인증을 추가하지 않는다.
3. 비밀 API key, 서버 처리, 지속 저장이 필요한가? 필요할 때만 서버와 저장 계층을 선택한다.
4. 에이전트·채팅·모바일·특정 sponsor가 사용자 가치에 필요한가? 필요할 때만 해당 예제를 읽는다.
5. 팀이 아는 기술과 실행·배포 제약에 맞는 가장 작은 경로를 고른다. 의존성 설치·설정 변경·계정 생성·유료 호출·배포·공개는 기존 별도 승인 경계를 유지한다.

## 검토 범위

아래 검토 commit에서 README와 대표 지침·템플릿·구현 일부를 읽었다. 설치와 앱 실행 검증하지 않았다. commit은 검토 스냅샷이지 최신성·안전성 보장이 아니다. 실제 채택 시 현재 공식 문서, 의존성, 라이선스와 행사 규칙을 다시 확인한다. 수상 보장·저자의 성과 주장은 채택 근거로 사용하지 않는다. 아래 적용 아이디어는 이 kit에 맞춰 새로 작성했으며 원문 파일·코드를 복사하지 않았다.

### The Hackathon Playbook

- 출처: https://github.com/IdkwhatImD0ing/hackathonstarterkit
- 검토 commit: `c7becdc30adfe3e9fb3ecc335dfab23f2eec134d`
- 구조: `app/`·`lib/`의 가이드 사이트와 `skills/`의 별도 제품 작업 지침. 명세→구현→demo→공개 자료로 이어진다.
- 참고 파일: `skills/domain-to-spec/SKILL.md`, `skills/feature-builder/SKILL.md`, `skills/ship-it/SKILL.md`.
- 반영한 원리: 공통 사실을 한 번 확인하고 여러 자료가 같은 근거를 참조한다.
- 라이선스: 검토 당시 GitHub API에서 확인하지 못했다. 원문 통째 복사·배포는 보류하고 권한을 확인한다.
- 채택하지 않는 것: 연쇄 자동 실행, 포트폴리오 사이트 필수화, 기본 기술 스택 고정.

### Uday — Hackathon Starter Pack

- 출처: https://github.com/udaysharmadev/Hackathon-Starter-Pack-Complete-Guide-Roadmap
- 검토 commit: `306deb4435858419d88e75c89484e1f82793845c`
- 구조: 주제별 번호 폴더, 여러 주요 절의 `templates/`와 `examples/`, 별도 boilerplate.
- 참고 파일: `03-problem-selection-engine/templates/problem-scorecard.md`, `08-build-fast-framework/templates/hourly-plan.md`, `12-team-building/templates/team-roles.md`.
- 반영한 원리: 설명과 합성 작성 예시를 연결하고, 시간 계획에 완료 증거와 미달 대응을 붙인다.
- 라이선스: 검토 당시 MIT. 실제 코드 채택 시 해당 파일의 권리·고지 조건도 확인한다.
- 제외: 원문 문제 점수표의 가중치 합은 12.5, 1~5점의 최고점은 62.5인데 문서는 100점을 최고점으로 적고 75점 이상을 강한 아이디어로 분류한다. 계산·임계값이 맞지 않아 채택하지 않는다. 인증·두 번째 기능을 기본으로 넣거나 배포를 마지막으로 미루는 시간표도 강제하지 않는다.

### CopilotKit — Agents, Everywhere

- 출처: https://github.com/CopilotKit/agents-everywhere-starter-kit
- 검토 commit: `5c8bf4c810bcd3abadaf573f7575bb73e098b03e`
- 구조: 행사 overview/rules, sponsor 설정, `apps/channel`·`apps/web`·`apps/mobile`, 개발 문서와 `SUBMISSION.md`.
- 참고 파일: `using-sponsor-tools.md`, `SUBMISSION.md`, `dev-docs/demo-prompts.md`.
- 반영한 원리: 최초 성공 호출의 실행 안내, 공식 기준→보여줄 장면→실행 evidence, 상속 부분과 행사 제작 부분의 구분.
- 라이선스: 검토 당시 MIT.
- 조건: 에이전트·웹·채팅·모바일이 실제 제품에 필요한 경우만 기술 예제를 검토한다. 특정 행사의 공식 규칙·시간·sponsor를 다른 행사에 복사하지 않는다.

### RachelBurman — Hackathon Starter

- 출처: https://github.com/RachelBurman/hackathon-starter
- 검토 commit: `cc8556b1f75334667a3459dc58ef1013223363d8`
- 구조: `apps/web`의 Next.js, `apps/api`의 FastAPI·SQLite. routes/services/repositories/agents/tools를 분리한다.
- 참고 파일: `docs/hackathon-checklist.md`, `apps/api/app/services/demo.py`, `apps/api/app/agents/coordinator.py`.
- 반영한 원리: 핵심 입력→처리→저장 또는 결과의 작은 경로부터 확인하고, 결정론적 로직과 선택적 에이전트를 분리한다.
- 라이선스: 검토 당시 MIT.
- 조건: Python 서버와 웹 UI가 필요할 때만 참고한다. DB·에이전트·인증을 모든 제품에 강제하지 않는다.

### sahat — Hackathon Starter

- 출처: https://github.com/sahat/hackathon-starter
- 검토 commit: `d7a20cce5e41f45f14eaf400af874f86817aea0d`
- 구조: Express·MongoDB 중심의 config/controllers/models/views/public/test, 인증과 여러 외부 API 예제.
- 참고 파일: `README.md`, `package.json`, `controllers/`, `test/`.
- 반영한 원리: 필요한 연동 예제를 조건부로 찾아보고 실제 호출과 재생 기반 테스트를 구분한다.
- 라이선스: 검토 당시 MIT.
- 조건: Node.js 앱의 특정 인증·API 예제가 필요할 때만 검토한다. 기능과 의존성을 통째로 기본 스타터에 넣지 않는다.

공통 적용 방식은 [인계 규칙](delivery-handoffs.md), 작성 예시는 [합성 예시](../examples/synthetic-handoff.md)를 본다. 이 목록은 외부 프로젝트의 보안·호환성·실행 성공을 보증하지 않는다.

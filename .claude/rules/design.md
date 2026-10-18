# Design

제품 UI, demo 화면, deck에 공통으로 적용한다.

## Product

- [workflow 계약](../../references/workflow-policy.md)의 build_policy에 따라 허용된 시점에 demo 핵심 화면을 준비한다. design/prompt/data의 사전 허용을 각각 확인하며 코드 금지만으로 사전설계를 허용하지 않는다. 초안·시각 승인·실제 UI 구현 완료는 별개다.
- 기존 제품에 시각 체계가 있으면 유지한다. 해커톤마다 제품 전체를 다시 디자인하지 않는다.
- 색상, typography, spacing, radius, 상태 표현을 일관되게 쓴다.
- 제품에 필요한 loading, success, failure, empty, infrastructure error 상태를 구분한다.
- 제품이 사용자에게 검증되지 않은 판정을 제공하는 경우 unverified를 success/failure 및 infra/model error와 구분한다. 해당 판정을 제공하는 CI comment 같은 비 UI surface에도 적용한다. 내부 demo 검증 상태를 모든 UI에 강제하거나 범위 밖 판정 기능을 추가하지 않는다.
- demo 중 한눈에 읽어야 하는 결과는 로그보다 먼저 보여준다.
- screenshot과 projector에서 읽히는 크기와 대비를 확인한다.
- secret, 개인 정보, 행사 Wi-Fi 같은 민감한 값이 demo 화면에 드러나지 않게 한다.
- 사용자 화면에는 내부 식별자(`S0`·`S1` 같은 시나리오 번호), 모델·계산 용어(`입자`), 뜻이 갈리는 축약(`~12:30`)을 쓰지 않는다. 사용자가 하는 행동과 상황으로 이름을 짓는다(예: "신고 시각", "15분 늦게 빠졌다면", "표류 경로 경우의 수"). 결과 JSON·코드 식별자는 그대로 둔다.
- 화면 설명 문장은 결과를 읽는 데 꼭 필요한 것만 남긴다. 카드 제목·부제·요약 문장이 같은 뜻을 반복하면 하나만 둔다.

## Demo

- 심사위원이 봐야 하는 핵심 상태를 클릭 수가 적은 경로에 둔다.
- 입력 → 실행 → 결과의 흐름이 화면에서 이어져야 한다.
- evidence는 실제 실행 결과와 연결한다.
- raw model reasoning이나 내부 debug 정보는 기본 화면에 노출하지 않는다.
- loading이 길어도 현재 무엇을 하는지 알 수 있게 한다.

## Deck

- 제품의 기존 시각 언어를 deck에 가져올 수 있으면 가져온다.
- 한 slide에 메시지 하나를 둔다.
- 실제 제품 screenshot을 mockup보다 우선한다.
- screenshot은 원본 비율을 유지한다.
- screenshot을 stretch하지 않는다. 필요하면 crop한다.
- 작은 UI를 억지로 한 화면에 모두 넣지 않는다.
- detail이 중요하면 별도 crop이나 detail slide를 쓴다.
- diagram은 실제 실행 경로를 설명할 때만 사용한다.
- sponsor logo 나열보다 sponsor가 실제로 들어가는 위치를 보여준다.
- 장식보다 문제, 결과, sponsor 역할, evidence가 먼저 읽혀야 한다.
- deck 전체에서 typography, spacing, image treatment가 drift하지 않게 한다.

## Rendering

artifact는 편집 화면만 보고 끝내지 않는다.

- 실제 PDF/PPTX 또는 slide preview로 render한다.
- clipping, overflow, low resolution을 눈으로 검사한다.
- projector나 일반 laptop 화면에서도 핵심 text가 읽히는지 본다.
- 여러 언어 버전은 각각 render한다.

## Reference

디자인 레퍼런스가 제공되면 색만 복사하지 않는다. typography, density, spacing, composition, image treatment 중 어떤 요소를 가져올지 먼저 정한다.

# CodingTest-Log

프로그래머스 알고리즘 & SQL 풀이 및 문법 정리

## 목표

- 매일 1문제 이상 풀고 기록하기
- 틀린 문제는 `mistakes.md`에 정리하고 다시 풀기

## 진행 현황

| 구분 | 푼 문제 수 |
|---|---|
| Lv.1 | 10 |
| Lv.2 | 11 |
| Lv.3 | 0 |
| SQL | 20 |

## 다시 풀 문제

AI/풀이를 참고한 문제. 안 보고 다시 풀면 체크하기.

- [ ] [Lv2] 최댓값과 최솟값
- [ ] [Lv2] 피보나치 수
- [ ] [Lv2] 전화번호 목록 (해시 풀이까지)
- [ ] [Lv2] 의상
- [ ] [Lv2] 짝지어 제거하기 (스택, `stack[-1]`)
- [ ] [Lv2] 게임 맵 최단거리 (BFS 템플릿 안 보고)
- [ ] [Lv1] 완주하지 못한 선수 (딕셔너리 풀이)

## 폴더 구조

```
├── programmers/        # 알고리즘 풀이 (레벨별)
│   ├── _template/      # 새 문제 추가 시 복사해서 사용
│   ├── lv1/
│   ├── lv2/
│   └── lv3/
├── sql/                # SQL 풀이 (고득점 Kit 카테고리별)
│   ├── select/
│   ├── sum-max-min/
│   ├── group-by/
│   ├── join/
│   ├── string-date/
│   └── is-null/
└── notes/              # 문법 및 참고 정리
    ├── python-syntax.md
    ├── sql-syntax.md
    ├── algorithm-patterns.md
    └── mistakes.md
```

## 커밋 규칙

| 태그 | 용도 | 예시 |
|---|---|---|
| `SOLVE:` | 새 문제 풀이 | `SOLVE: [Lv2] 타겟 넘버 (DFS)` |
| `RETRY:` | 재풀이 | `RETRY: [Lv2] 게임 맵 최단거리 - BFS로 재풀이` |
| `DOCS:` | 문법/노트 정리 | `DOCS: sql-syntax.md 날짜 함수 추가` |

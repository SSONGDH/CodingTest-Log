# CodingTest-Log

프로그래머스 알고리즘 & SQL 풀이 및 문법 정리

## 목표

- 매일 1문제 이상 풀고 기록하기
- 틀린 문제는 `mistakes.md`에 정리하고 다시 풀기

## 진행 현황

| 구분 | 푼 문제 수 |
|---|---|
| Lv.0 | 0 |
| Lv.1 | 10 |
| Lv.2 | 0 |
| Lv.3 | 0 |
| SQL | 10 |

## 폴더 구조

```
├── programmers/        # 알고리즘 풀이 (레벨별)
│   ├── _template/      # 새 문제 추가 시 복사해서 사용
│   ├── lv0/
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

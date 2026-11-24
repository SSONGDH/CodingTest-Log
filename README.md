# CodingTest-Log

프로그래머스 · 백준 알고리즘 & SQL 풀이 및 문법 정리

## 목표

- 매일 1문제 이상 풀고 기록하기
- 틀린 문제는 `mistakes.md`에 정리하고 다시 풀기

## 진행 현황

| 구분 | 푼 문제 수 |
|---|---|
| Lv.1 | 10 |
| Lv.2 | 11 |
| Lv.3 | 1 |
| 백준 Bronze | 4 |
| SQL | 22 |

## 다시 풀 문제

AI/풀이를 참고한 문제. 안 보고 다시 풀면 체크하기.

- [ ] [Lv2] 최댓값과 최솟값
- [ ] [Lv2] 피보나치 수
- [ ] [Lv2] 전화번호 목록 (해시 풀이까지)
- [ ] [Lv2] 의상
- [ ] [Lv2] 짝지어 제거하기 (스택, `stack[-1]`)
- [ ] [Lv2] 게임 맵 최단거리 (BFS 템플릿 안 보고)
- [ ] [Lv3] 네트워크 (README의 "빈 화면에서 짜는 순서"대로)
- [ ] [Lv1] 완주하지 못한 선수 (딕셔너리 풀이)

## 검토할 문제

정석과 다른 방식으로 푼 문제. 정석 풀이를 읽고 이해했으면 체크하기.

- [ ] [BOJ 14215] 세 막대: 1씩 줄이는 while 반복 → 정렬 후 `c = a + b - 1` 공식 (정석)

## 폴더 구조

```
├── programmers/        # 알고리즘 풀이 (레벨별)
│   ├── _template/      # 새 문제 추가 시 복사해서 사용
│   ├── lv1/
│   ├── lv2/
│   └── lv3/
├── baekjoon/           # 백준 풀이 (티어별, 폴더명: 번호-문제-이름)
│   └── bronze/
├── sql/                # SQL 풀이 (고득점 Kit 카테고리별)
│   ├── select/
│   ├── sum-max-min/
│   ├── group-by/
│   ├── join/
│   ├── string-date/
│   └── is-null/
└── notes/              # 문법 및 참고 정리
    ├── exam-checklist.md   # 시험 직전에 훑어볼 체크리스트
    ├── python-syntax.md
    ├── sql-syntax.md
    ├── algorithm-patterns.md
    └── mistakes.md
```

## 커밋 규칙

| 태그 | 용도 | 예시 |
|---|---|---|
| `SOLVE:` | 새 문제 풀이 | `SOLVE: [Lv2] 타겟 넘버 (DFS)`, `SOLVE: [BOJ 1085] 직사각형에서 탈출 (수학)` |
| `RETRY:` | 재풀이 | `RETRY: [Lv2] 게임 맵 최단거리 - BFS로 재풀이` |
| `DOCS:` | 문법/노트 정리 | `DOCS: sql-syntax.md 날짜 함수 추가` |

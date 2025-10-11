t = int(input())
for _ in range(t):
    a, b = map(int, input().split(" "))
    xk, yk = map(int, input().split(" "))
    xq, yq = map(int, input().split(" "))

    king_moves = set()
    for dx, dy in [(a, b), (a, -b), (-a, b), (-a, -b),
                   (b, a), (b, -a), (-b, a), (-b, -a)]:
        king_moves.add((xk + dx, yk + dy))

    queen_moves = set()
    for dx, dy in [(a, b), (a, -b), (-a, b), (-a, -b),
                   (b, a), (b, -a), (-b, a), (-b, -a)]:
        queen_moves.add((xq + dx, yq + dy))

    ans = len(king_moves & queen_moves)
    print(ans)
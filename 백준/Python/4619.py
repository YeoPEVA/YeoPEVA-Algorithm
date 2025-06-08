while True:
    B, N = map(int, input().split())

    # 종료 조건
    if B == 0 and N == 0:
        break

    # A^N이 B에 가장 가까운 정수 A를 찾기 위한 초기값
    A = 0

    # A^N이 B보다 크거나 같아질 떄까지 A 증가
    while A ** N < B:
        A += 1

    # 두 후보 중 더 가까운 값을 선택
    lower = (A - 1) ** N
    upper = A ** N

    # B에 더 가까운 쪽의 A를 출력
    if abs(upper - B) < abs(B - lower):
        print(A)
    else:
        print(A - 1)

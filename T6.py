def find_order(n):
    from collections import defaultdict, deque

    adj = defaultdict(list)
    in_deg = defaultdict(int)
    queue = deque()
    words = []
    unique_char = set()

    for i in range(n):
        cur_w = input()
        words.append(cur_w)

    idx = 0
    while idx < n - 1:
        w1 = words[idx]
        w2 = words[idx + 1]

        if len(w1) > len(w2) and w1[:len(w2)] == w2:
            print(-1)
            return

        min_len = min(len(w1), len(w2))
        for j in range(min_len):
            if w1[j] != w2[j]:
                adj[w1[j]].append(w2[j])
                in_deg[w1[j]] += 0
                in_deg[w2[j]] += 1
                break
        idx += 1

    for word in words:
        for char in word:
            unique_char.add(char)
            in_deg[char] += 0

    for char in in_deg:
        if in_deg[char] == 0:
            queue.append(char)

    final_order = []
    while queue:
        queue = deque(sorted(queue))
        node = queue.popleft()
        final_order.append(node)

        for neighbor in adj[node]:
            in_deg[neighbor] -= 1
            if in_deg[neighbor] == 0:
                queue.append(neighbor)

    if len(final_order) != len(unique_char):
        print(-1)
    else:
        print("".join(final_order))

n = int(input())
find_order(n)
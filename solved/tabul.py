def tabulate_pis(N):
    if N <= 1:
      raise ValueError(N)
    v = int(N ** 0.5)
    smalls = [i - 1 for i in range(v + 1)]
    larges = [0 if i == 0 else N // i - 1 for i in range(v + 1)]

    for p in range(2, v + 1):
      if smalls[p - 1] == smalls[p]:
        continue

      p_cnt = smalls[p - 1]
      q = p * p
      end = min(v, N // q)
      for i in range(1, end + 1):
        d = i * p
        if d <= v:
          larges[i] -= larges[d] - p_cnt
        else:
          larges[i] -= smalls[N // d] - p_cnt
      for i in range(v, q - 1, -1):
        smalls[i] -= smalls[i // p] - p_cnt
    return smalls, larges
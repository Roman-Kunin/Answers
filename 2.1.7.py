def how_many_times(n: str) -> int:
    return min([n.lower().count(i) for i in 'python'])

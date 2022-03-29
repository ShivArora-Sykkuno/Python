from collections import defaultdict
import itertools


def canFinish(numCourses, prerequisites):
    immediate_prereq = defaultdict(list)
    for p in prerequisites:
        immediate_prereq[p[0]] += (p[1],)
    for i in range(numCourses):
        if i in immediate_prereq:
            stack, visited = [(i, False)], set()
            while stack:
                j, clear_visited_on_pop = stack.pop()
                if clear_visited_on_pop:
                    visited.remove(j)
                elif j >= i:
                    if j in visited:
                        return False
                    if j in immediate_prereq:
                        visited.add(j)
                        stack.append((j, True))
                        stack.extend(zip(immediate_prereq[j], itertools.cycle([False])))
    return True

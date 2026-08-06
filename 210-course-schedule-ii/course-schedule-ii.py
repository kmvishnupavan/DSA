from collections import deque

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        order = []

        while q:
            course = q.popleft()
            order.append(course)

            for nei in graph[course]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)

        if len(order) == numCourses:
            return order

        return []
import heapq

class Manager:
    def __init__(self, userId, taskId, priority):
        self.userId = userId
        self.taskId = taskId
        self.priority = priority

    def __lt__(self, other):

        if self.priority == other.priority:
            return self.taskId >= other.taskId  # higher taskId wins
        return self.priority >= other.priority  # higher priority wins



class TaskManager:
    def __init__(self, tasks):
        self.heap = []
        self.record = {}  # taskId -> Manager
        for userId, taskId, priority in tasks:
            m = Manager(userId, taskId, priority)
            heapq.heappush(self.heap, m)
            self.record[taskId] = m

    def add(self, userId, taskId, priority):
        m = Manager(userId, taskId, priority)
        heapq.heappush(self.heap, m)
        self.record[taskId] = m

    def edit(self, taskId, newPriority):
        if taskId not in self.record:
            return
        old = self.record[taskId]
        self.add(old.userId, taskId, newPriority)
        

    def rmv(self, taskId):
        if taskId in self.record:
            del self.record[taskId]  # lazy delete

    def execTop(self):
        while self.heap:
            top = heapq.heappop(self.heap)
            latest = self.record.get(top.taskId)
            if latest is None:
                continue  # removed
            if latest.priority != top.priority:
                continue  # outdated
            del self.record[top.taskId]
            return top.userId
        return -1
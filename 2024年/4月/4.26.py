# source: https://leetcode.cn/problems/snapshot-array/description/
## 法一：超出内存限制
class SnapshotArray:
    def __init__(self, length: int):
        self.current_array = [0] * length  # 当前的数组状态
        self.snapshots = []  # 存储每次快照的数组状态

    def set(self, index: int, val: int) -> None:
        self.current_array[index] = val  # 更新当前数组中的值

    def snap(self) -> int:
        # 存储当前数组的一个副本作为快照
        self.snapshots.append(self.current_array[:])
        return len(self.snapshots) - 1  # 返回这次快照的索引，即 snap_id

    def get(self, index: int, snap_id: int) -> int:
        # 返回指定快照中的值
        return self.snapshots[snap_id][index]

## 法二：二分法快速检索
class SnapshotArray1:
    def __init__(self, length: int):
        # 使用字典来存储每个索引的修改历史
        # 每个索引的历史是一个列表，包含 (snap_id, value) 元组
        self.history = {i: [] for i in range(length)}
        self.snap_id = 0  # 初始化快照 ID

    def set(self, index: int, val: int) -> None:
        # 如果当前修改的 snap_id 和最后一次修改的 snap_id 相同，则更新值
        # 否则添加新的修改记录
        if self.history[index] and self.history[index][-1][0] == self.snap_id:
            self.history[index][-1] = (self.snap_id, val)
        else:
            self.history[index].append((self.snap_id, val))

    def snap(self) -> int:
        # 仅递增 snap_id 并返回上一个 ID
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        # 获取索引的历史修改记录
        # 使用二分查找找到最接近但不超过 snap_id 的修改记录
        history = self.history[index]
        if not history:
            return 0  # 如果没有修改记录，默认值为 0
        l, r = 0, len(history) - 1
        while l <= r:
            mid = (l + r) // 2
            if history[mid][0] <= snap_id:
                l = mid + 1
            else:
                r = mid - 1
        # 如果找到了合适的记录，返回该值
        if r >= 0:
            return history[r][1]
        return 0
class PQ:
    def __init__(self) -> None:
        self.queue = []
        self.cost_map = {}
    def is_mt(self) -> bool:
        return not len(self.queue)
    def is_in(self, name: str) -> bool:
        return name in self.queue
    def push(self, name: str, cost: float) -> None:
        if name in self.queue:
            print("Already in queue. Push operation aborted.")
            return
        self.queue.append(name)
        self.cost_map[name] = cost
    def pop(self) -> tuple[str, float]:
        if self.is_mt():
            return None
        min_name, min_cost = min(self.cost_map.items(), key=lambda x: x[1])
        del self.cost_map[min_name]
        self.queue.remove(min_name)
        return min_name, min_cost
    def get_cost(self, name: str) -> float:
        if not name in self.queue:
            print(self.cost_map)
            print("Item not in queue. Get operation aborted.")
            return None
        return self.cost_map[name]
    def set_cost(self, name: str, cost: float) -> None:
        if not name in self.queue:
            print("Item not in queue. Set operation aborted.")
            return
        self.cost_map[name] = cost
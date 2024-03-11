import sukta.tree_util as stu


class AvgMeter:
    def __init__(self, value):
        self.value = value
        self.count = 1

    def update(self, value):
        self.value += value
        self.count += 1

    def compute(self):
        return self.value / self.count


class MetricAccumulator:
    def __init__(self):
        self.metrics = {}

    def update(self, metrics):
        for k, v in stu.iter_path(metrics, delim="/"):
            if stu.dict_has_path(self.metrics, k):
                x = stu.dict_get_path(self.metrics, k)
                x.update(v)
            else:
                stu.dict_set_path(self.metrics, k, AvgMeter(v))

    def compute(self):
        return stu.apply_vfunc(lambda x: x.compute(), self.metrics)

    def empty(self):
        self.metrics = {}

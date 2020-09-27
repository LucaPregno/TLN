class Father:
    def __init__(self, height, label="S"):
        self.height = height
        self.label = label

    def set(self, height, label):
        self.height = height
        self.label = label

    def print(self):
        print("Label:", self.label, "height:", self.height)

class Biryani:
    def __init__(self,smell,taste,texture, meatContent,color):
        self.smell = smell
        self.taste = taste
        self.texture = texture
        self.meatContent = meatContent
        self.color = color

hb = Biryani("onion smell", "spicy", "smooth",True, "multicolor")
ab = Biryani("turmeric/onion","moderate spicy", "sticky", True, "Yellow")
db = Biryani("pudina","spicy","rough", True,"Green")

print(hb.meatContent)
print(ab.color)
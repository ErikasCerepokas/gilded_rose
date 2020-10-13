import item


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def item_loop(self):
        for item in self.items:
            self.update_quality(item)

    def update_quality(self,item):
        self.sellin()
        if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
            if item.name != "Sulfuras, Hand of Ragnaros":
                self.quality_decrease()
        else:
            if item.quality < 50:
                item.quality += 1
                if item.name == "Backstage passes to a TAFKAL80ETC concert":
                    if item.sell_in < 11:
                        self.quality_increase()
                    if item.sell_in < 6:
                        self.quality_increase()
        if item.sell_in < 0:
            if item.name != "Aged Brie":
                if item.name != "Backstage passes to a TAFKAL80ETC concert":
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        self.quality_decrease()
                else:
                    item.quality -= item.quality
            else:
                self.quality_increase()

    def quality_increase(self):
        if item.quality < 50:
            item.quality += 1

    def quality_decrease(self):
        if item.quality > 0:
            item.quality -= 1

    def sellin(self):
        if item.name != "Sulfuras, Hand of Ragnaros":
            item.sell_in -= 1
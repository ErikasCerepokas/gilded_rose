import item


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality -= 1
            else:
                if item.quality < 50:
                    item.quality += 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            self.quality_increase()
                        if item.sell_in < 6:
                            self.quality_increase()
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in -= 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality -= 1
                    else:
                        item.quality -= item.quality
                else:
                    self.quality_increase()

    def quality_increase(self):
        if item.quality < 50:
            item.quality += 1
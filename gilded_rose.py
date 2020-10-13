
class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue
            if item.name == "Aged Brie":
                    if item.quality < 50:
                        item.quality += 1
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                    if item.quality < 50:
                        item.quality += 1
                        if item.name == "Backstage passes to a TAFKAL80ETC concert":
                            if item.sell_in < 11:
                                if item.quality < 50:
                                    item.quality += 1
                            if item.sell_in < 6:
                                if item.quality < 50:
                                    item.quality += 1
            else:
                if item.quality > 0:
                    item.quality -= 1
            if item.sell_in < 1:
                if item.name == "Aged Brie":
                    if item.quality < 50:
                        item.quality += 1
                elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                    item.quality = item.quality - item.quality
                else:
                    if item.quality > 0:
                        item.quality -= 1
            item.sell_in -= 1


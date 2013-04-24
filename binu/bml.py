class BML(object):
    def get_bml(self):
        raise NotImplementedError
    
class ActionMenuItem(BML):
    text = None
    href = None
    def __init__(self, text, href):
        self.text = text
        self.href = href
        
    def get_bml(self, pos):
        xml_ret = u"""<action key="{}" text="{}">{}</action>\n""".format(pos, self.text, self.href)
        return xml_ret

class ActionMenu(BML):
    _items = []
    align = "Left"
    def add(self, item):
        self._items.append(item)

    def get_bml(self):
        children_ret = ""
        for pos, item in enumerate(self._items):
            children_ret += item.get_bml(pos+1)
        return u'<menu align="{}" name="action_menu">\n{}</menu>'.format(self.align, children_ret)

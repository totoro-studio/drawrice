__author__ = 'Tony'

class LotteryQueue():
    __lq = {'ltype'   :   '',
            'number'  :   0}

    lqs = []

    def lqueueadd(self, lq):
        tail = len(self.lqs) -1
        if tail >=0 and self.lqs[tail]['ltype'] == lq['ltype']:
            self.lqs[tail]['number'] += lq['number']
        else:
            self.lqs.append(lq)

    def lqueuepop(self):
        self.lqs.pop()

    def lqueueclear(self):
        self.lqs.clear()

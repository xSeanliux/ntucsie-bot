import random, pickle

class quote:
    allquotes = []
    def __init__(self):
        with open ('zckquotes', 'rb') as fp:
            self.allquotes = pickle.load(fp)
            print("Loaded", len(self.allquotes), "quotes")

    ## Randomly chooses a quote from ./zck_quotes/zckquotes and displays it
    def getMsg(self, idx): #Gets the #idx -th quote, formats it, and returns it as a string
        if idx >= len(self.allquotes) or idx < 0:
            return "ZCK#%03d not found." % (idx)
        txt = self.allquotes[idx].splitlines()
        mxlen = 0
        fulltxt = ''
        for x in txt:
            if(x == ''):
                continue
            fulltxt = fulltxt + '> 　' + x.strip() + '\n'
            mxlen = max(mxlen, len(x))
        msg = '> 「\n%s> %s 」——ZCK#%03d' % (fulltxt, '　'*(mxlen + 1), idx)
        return msg

    def query(self, arr):
        if len(arr) > 5:
            arr = arr[:5]
        ret = []
        if len(arr) == 0:
            ret.append(self.getMsg(random.randint(0, len(self.allquotes) - 1)))
        else:
            ret = [self.getMsg(num) for num in arr]
        return ret
        
zck = quote()

if __name__ == "__main__":
    zck = quote()
    print(zck.query([1, 2, 3, 4, 5]))
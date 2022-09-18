import rpa as r


r.init()
r.url('https://groww.in/stocks/user/investments')
r.wait(6)
r.snap('page', 'results.png')
r.close()

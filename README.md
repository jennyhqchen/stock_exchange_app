# stock_exchange_app

A Simple Stock Exchange App based on Vue and Django.

### Functionality
This app provides below functionalities.

- Browse public market data
- Search stock by stock code and stock name
- Login and Register
- Sell and buy stock
- Shareholding Checking

Basically the app use the menu on the top for navigation
![屏幕快照 2021-03-24 下午9.15.45.png](https://cdn.nlark.com/yuque/0/2021/png/2556936/1616591756951-a4db0a52-ae5f-420f-b1da-eb60ba981209.png#align=left&display=inline&height=526&margin=%5Bobject%20Object%5D&name=%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202021-03-24%20%E4%B8%8B%E5%8D%889.15.45.png&originHeight=526&originWidth=2728&size=89844&status=done&style=none&width=2728)
#### Browse public market data
You can browse the public market data even if you don't login.
I use baostock to generate the historical market data and insert the data into MySQL.
Please check stock_exchange_app/stock_exchange/get_stock_basic.py and get_stock_history_k.py)
![屏幕快照 2021-03-24 下午8.54.45.png](https://cdn.nlark.com/yuque/0/2021/png/2556936/1616590503978-bd4782a9-4383-450b-a8db-e489fd9df4b3.png#align=left&display=inline&height=1294&margin=%5Bobject%20Object%5D&name=%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202021-03-24%20%E4%B8%8B%E5%8D%888.54.45.png&originHeight=1294&originWidth=2758&size=272054&status=done&style=none&width=2758)
#### Search Stock
You can search stock by stock name.
![屏幕快照 2021-03-24 下午8.57.25.png](https://cdn.nlark.com/yuque/0/2021/png/2556936/1616590672450-2c64ff04-e8c2-4dd6-b031-5a34cfd9b2f1.png#align=left&display=inline&height=728&margin=%5Bobject%20Object%5D&name=%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202021-03-24%20%E4%B8%8B%E5%8D%888.57.25.png&originHeight=728&originWidth=2768&size=94933&status=done&style=none&width=2768)
You can also search stock by stock code.
![屏幕快照 2021-03-24 下午8.58.44.png](https://cdn.nlark.com/yuque/0/2021/png/2556936/1616590750679-ebf08ff6-bcd5-4058-8494-c34dc85181ef.png#align=left&display=inline&height=496&margin=%5Bobject%20Object%5D&name=%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202021-03-24%20%E4%B8%8B%E5%8D%888.58.44.png&originHeight=496&originWidth=2772&size=81070&status=done&style=none&width=2772)
#### Login and Register
![屏幕快照 2021-03-24 下午8.59.30.png](https://cdn.nlark.com/yuque/0/2021/png/2556936/1616590791997-74d2666a-7501-4e60-a5bc-1632bb7fa1ab.png#align=left&display=inline&height=656&margin=%5Bobject%20Object%5D&name=%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202021-03-24%20%E4%B8%8B%E5%8D%888.59.30.png&originHeight=656&originWidth=2758&size=64855&status=done&style=none&width=2758)
#### Sell and Buy Stock
If you didn't login the app, when you click sell or buy, it will navigate to Login page first.
You can choose from the existing stocks and buy it with a proper price
![屏幕快照 2021-03-24 下午9.00.44.png](https://cdn.nlark.com/yuque/0/2021/png/2556936/1616590874000-cc14704f-4365-4c62-99e4-edccf96f0597.png#align=left&display=inline&height=998&margin=%5Bobject%20Object%5D&name=%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202021-03-24%20%E4%B8%8B%E5%8D%889.00.44.png&originHeight=998&originWidth=2760&size=165855&status=done&style=none&width=2760)
![屏幕快照 2021-03-24 下午9.01.29.png](https://cdn.nlark.com/yuque/0/2021/png/2556936/1616590900699-70260b8f-0482-4c7b-9cc1-3128cc4f8920.png#align=left&display=inline&height=730&margin=%5Bobject%20Object%5D&name=%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202021-03-24%20%E4%B8%8B%E5%8D%889.01.29.png&originHeight=730&originWidth=2752&size=80095&status=done&style=none&width=2752)
You can also check the stock you owned and sell them.
![屏幕快照 2021-03-24 下午9.02.35.png](https://cdn.nlark.com/yuque/0/2021/png/2556936/1616590969521-1498fed3-665f-424d-9733-98c1797f78c8.png#align=left&display=inline&height=466&margin=%5Bobject%20Object%5D&name=%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202021-03-24%20%E4%B8%8B%E5%8D%889.02.35.png&originHeight=466&originWidth=2756&size=59956&status=done&style=none&width=2756)
![屏幕快照 2021-03-24 下午9.03.25.png](https://cdn.nlark.com/yuque/0/2021/png/2556936/1616591017171-5c754cab-dc34-4b49-901b-9a427be46556.png#align=left&display=inline&height=610&margin=%5Bobject%20Object%5D&name=%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202021-03-24%20%E4%B8%8B%E5%8D%889.03.25.png&originHeight=610&originWidth=1210&size=47480&status=done&style=none&width=1210)
#### Profit
You can check the profit you get from selling the stock
![屏幕快照 2021-03-24 下午9.13.09.png](https://cdn.nlark.com/yuque/0/2021/png/2556936/1616591601885-011918c0-2381-41c3-b539-dc88f76d9389.png#align=left&display=inline&height=572&margin=%5Bobject%20Object%5D&name=%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202021-03-24%20%E4%B8%8B%E5%8D%889.13.09.png&originHeight=572&originWidth=2744&size=76665&status=done&style=none&width=2744)
### Next step

- Use real time stock dataset instead of historical batch dataset
- Provide Candlestick Charts for each stock
- More complete sell and buy workflow including Trade Matching, Clearing


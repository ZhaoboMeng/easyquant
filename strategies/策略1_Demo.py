from easyquant import StrategyTemplate


class Strategy(StrategyTemplate):
    def strategy(self, event):
        print('\n\n策略1触发')
        print('行情数据: 万科价格: ', event.data['000002'])
        print('检查持仓')
        print(self.user.balance)
        print('\n')

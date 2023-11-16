strategy_map = {

}


class BankDetailFactory:

    @staticmethod
    def create(strategy, **kwargs):
        instance = strategy_map[strategy]
        if not instance:
            raise Exception("invalid strategy")
        return instance.handle(**kwargs)

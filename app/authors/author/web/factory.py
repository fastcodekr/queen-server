strategy_map = {

}


class AuthorFactory:

    @staticmethod
    def create(strategy, **kwargs):
        instance = strategy_map[strategy]
        if not instance:
            raise Exception("invalid strategy")
        return instance.handle(**kwargs)

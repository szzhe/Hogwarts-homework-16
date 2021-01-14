def blank_warpper(fun):
    def run(*args, **kwargs):
        basepage = args[0]
        try:
            return fun(*args, **kwargs)
        except Exception as e:
            for blank in basepage.blank_list:
                eles = basepage.finds(*blank)
                if len(eles) > 0:
                    eles[0].click()
                    return fun(*args, **kwargs)
            raise e
    return run
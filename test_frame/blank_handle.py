import logging
import allure

logging.basicConfig(level=logging.INFO)
# error > info > debug

def blank_warpper(fun):
    def run(*args, **kwargs):
        basepage = args[0]
        try:
            logging.info("start find : \nargs: " + str(args) + " kwargs: " + str(kwargs))
            return fun(*args, **kwargs)
        except Exception as e:
            basepage.screenshot("./screenshot/blank.png")
            with open("./screenshot/blank.png", "rb") as f:
                picture_data = f.read()
            allure.attach(picture_data, attachment_type=allure.attachment_type.PNG)
            for blank in basepage.blank_list:
                eles = basepage.finds(*blank)
                if len(eles) > 0:
                    eles[0].click()
                    return fun(*args, **kwargs)
            raise e
    return run
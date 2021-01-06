import logging
import yaml
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    _params = {}

    def __init__(self, driver: WebElement = None):
        self.driver = driver

    def find(self, by, locator: str = None):
        if locator is None:
            self.driver.find_element(*by)
        else:
            self.driver.find_element(by=by, value=locator)

    def steps(self, path):
        with open(path) as f:
            steps: list[dict] = yaml.safe_load(f)
            element: WebElement = None
            for step in steps:
                logging.info(step)
                if "by" in step.keys():
                    element = self.find(step["by"], step["locator"])
                if "action" in step.keys():
                    action = step["action"]
                    if action == "find":
                        pass
                    elif action == "click":
                        element.click()
                    elif action == "text":
                        return element.text
                    elif action == "attribute":
                        element.get_attribute(step["value"])
                    elif action in ["send", "input"]:
                        content: str = step["value"]
                        for key in self._params.keys():
                            content = content.replace("{s}" % key, self._params[key])

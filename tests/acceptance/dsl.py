
class SortingLine:
    def __init__(self, driver):
        self._driver = driver
    def look_for(self, item, on):
        return self._driver.look_for(item, on=on)



def assert_found(item: str, among: list[str]):
    __tracebackhide__ = True
    assert item in among, f"Expected {item} to be found. Found {among}"

def assert_not_found(item: str, among: list[str]):
    __tracebackhide__ = True
    assert item not in among, f"Expected {item} to not be found. Found {among}"


from dsl import assert_found, assert_not_found

def test_missing_item_not_found(sorting_line):
    found_items = sorting_line.look_for("bottle", on="mostly cardboard")
    assert_not_found("bottle", among=found_items)

def test_cardboard_found_when_present(sorting_line):
    found_items = sorting_line.look_for("cardboard", on="mostly cardboard")
    assert_found("cardboard", among=found_items)

def test_find_different_items_when_present(sorting_line):
    found_items = sorting_line.look_for(["cardboard", "magazine"], on="mixed paper")
    assert_found("cardboard", among=found_items)
    assert_found("magazine", among=found_items)


def test_find_only_present_items(sorting_line):
    found_items = sorting_line.look_for(["cardboard", "bottle", "magazine", "vegetable"], on="mixed paper")
    assert_found("cardboard", among=found_items)
    assert_found("magazine", among=found_items)
    assert_not_found("bottle", among=found_items)
    assert_not_found("vegetable", among=found_items)

def test_find_only_searched_items(sorting_line):
    found_items = sorting_line.look_for(["magazine"], on="mixed paper")
    assert_not_found("cardboard", among=found_items)
    assert_found("magazine", among=found_items)
    assert_not_found("bottle", among=found_items)

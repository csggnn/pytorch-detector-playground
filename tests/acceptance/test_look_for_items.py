from dsl import assert_found, assert_not_found

def test_missing_item_not_found(sorting_line):
    found_items = sorting_line.look_for("bottle", on="mostly cardboard")
    assert_not_found("bottle", among=found_items)

def test_cardboard_found_when_present(sorting_line):
    found_items = sorting_line.look_for("cardboard", on="mostly cardboard")
    assert_found("cardboard", among=found_items)
#pyright: reportUnusedExpression=false
import relationalai as rai
import pandas as pd
from pandas.testing import assert_frame_equal
from relationalai.clients import config as cfg

def test_simple_people(engine_config: cfg.Config):
    model = rai.Model("people", config=engine_config)
    Person = model.Type("Person")

    with model.rule():
        alex = Person.add(name="Alex", age=19)
        bob = Person.add(name="Bob", age=47)
        carol = Person.add(name="Carol", age=17)
        deb = Person.add(name="Deb", age=17)

        carol.set(friend=deb)
        alex.set(friend=bob)
        alex.set(friend=carol)

    with model.query() as select:
        alex = Person(name="Alex")
        person = alex.friend
        person.age >= 21
        response = select(person.name)

    expected = pd.DataFrame({"name": ["Bob"]})
    assert_frame_equal(response.results, expected)

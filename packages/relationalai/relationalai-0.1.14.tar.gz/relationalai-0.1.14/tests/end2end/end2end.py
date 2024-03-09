#pyright: reportUnusedExpression=false
import os
import relationalai as rai
import random
import pandas as pd
from pandas.testing import assert_frame_equal
from relationalai.clients import config as cfg

def do_test(client_id: str|None, client_secret: str|None, engine_name: str):

    if client_id is None or client_secret is None:
        raise ValueError("RAI_CLIENT_ID and RAI_CLIENT_SECRET must be set")

    # Running against prod
    config = cfg.Config({
        'platform': "azure",
        'host': "azure.relationalai.com",
        'port': "443",
        'region': "us-east",
        'scheme': "https",
        'client_credentials_url': "https://login.relationalai.com/oauth/token",
        'client_id': client_id,
        'client_secret': client_secret,
        'engine': engine_name,
    })
    
    # Create an engine
    print(f"Creating engine {engine_name}")
    provider = rai.Resources(config=config)
    provider.create_engine(engine_name, 'XS')

    # Do the actual test
    print("Running test...")
    try:
        run_pyrel(config)
    finally:
        print(f"Deleting engine {engine_name}")
        provider.delete_engine(engine_name)

def run_pyrel(config: cfg.Config):
    model = rai.Model("people", config=config)
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

def test_e2e():
    random_number = random.randint(1000000000, 9999999999)
    
    do_test(
        client_id=os.getenv('RAI_CLIENT_ID'),
        client_secret=os.getenv('RAI_CLIENT_SECRET'),
        engine_name=f"pyrel-test-{random_number}"
    )

if __name__ == "__main__":
    test_e2e()

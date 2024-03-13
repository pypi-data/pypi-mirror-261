import relationalai as rai
import pandas as pd
from relationalai.clients import config as cfg
from relationalai.std.graphs import Graph
from pandas.testing import assert_frame_equal

def test_pagerank(engine_config: cfg.Config):
    # Create a model named "socialNetwork" with a Person type.
    model = rai.Model("socialNetwork", config=engine_config)
    Person = model.Type("Person")

    # Add some people to the model and connect them with a `follows` property.
    with model.rule():
        alice = Person.add(name="Alice")
        bob = Person.add(name="Bob")
        carol = Person.add(name="Carol")
        alice.set(follows=carol)
        bob.set(follows=alice)
        carol.set(follows=alice).set(follows=bob)

    # Create a graph and add all Person objects to the set of nodes
    # and the Person.follows property to the set of edges.
    graph = Graph(model)
    graph.nodes.extend(Person)
    graph.edges.extend(Person.follows)

    # Compute the PageRank of each person in the graph.
    with model.query() as select:
        person = Person()
        centrality = graph.compute.pagerank(person)
        response = select(person.name, centrality)

    # Note: this does fuzzy equality by default.
    assert_frame_equal(response.results, pd.DataFrame({
        "name": ["Alice", "Bob", "Carol"],
        "v": [0.397402, 0.214806, 0.387792]
    }))

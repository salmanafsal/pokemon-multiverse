from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_add_pokemon_to_squad():
    # Step 1: Add a Pokémon to the squad
  

    # Step 4: Retrieve the squad and verify its contents
    response = client.get("/")
    assert response.status_code == 200
    
    squad = response.json()
    print(squad)
    #assert len(squad) == 2
    #assert any(pokemon["name"] == "Pikachu" for pokemon in squad)
    #assert any(pokemon["name"] == "Bulbasaur" for pokemon in squad)
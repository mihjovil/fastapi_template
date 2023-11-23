from unittest import TestCase
import random
import requests

if __name__ == "__main__":
    simples = [
        {
            "id": i,
            "score": random.random()
        }
        for i in range(10)
    ]
    best = random.choice(simples)
    n = {
        "id": 1,
        "simples": simples,
        "best": best
    }
    response = requests.post("http://localhost:8000/new_nested", json=n)
    print(response)

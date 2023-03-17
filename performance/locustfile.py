import json
import random
from locust import HttpUser, task, constant
from helper import generate_king_name, generate_kingdom_name, generate_random_polygon

STANDARD_WEIGHT = 8
WAIT_TIME = 3 # wait for ${WAIT_TIME} seconds for each request

class KingdomAPIUser(HttpUser):

    wait_time = constant(2)
    latest_kingdom_id = 1

    @task(STANDARD_WEIGHT // 4)
    def create_kingdom(self):
        """
            Create a new kngdom
        """
        kingdom_data = {
            "name": generate_kingdom_name(),
            "king": generate_king_name(),
            "territory": generate_random_polygon()
        }
        headers = {'Content-Type': 'application/json'}
        response = self.client.post("/kingdoms/", data=json.dumps(kingdom_data), headers=headers)
        self.latest_kingdom_id = response.json()["id"]

    @task(STANDARD_WEIGHT)
    def get_specific_kingdom(self):
        if self.latest_kingdom_id:
            kingdom_id = random.randint(1, self.latest_kingdom_id)
            self.client.get(f"/kingdoms/{kingdom_id}")

    @task(STANDARD_WEIGHT // 8)
    def update_kingdom_king(self):
        """
            Oopsy, there was a coup in the kingdom, so the other king took over
        """
        kingdom_data = {
            "king": generate_king_name()
        }
        if self.latest_kingdom_id:
            kingdom_id = random.randint(1, self.latest_kingdom_id)
            headers = {'Content-Type': 'application/json'}
            self.client.put(f"/kingdoms/{kingdom_id}", data=json.dumps(kingdom_data), headers=headers)

    @task(STANDARD_WEIGHT // 8)
    def update_kingdom_territory(self):
        """
            There was a war recently with neighbours, so kingdom territory has been changed
        """
        kingdom_data = {
            "territory": generate_random_polygon()
        }
        if self.latest_kingdom_id:
            kingdom_id = random.randint(1, self.latest_kingdom_id)
            headers = {'Content-Type': 'application/json'}
            self.client.put(f"/kingdoms/{kingdom_id}", data=json.dumps(kingdom_data), headers=headers)

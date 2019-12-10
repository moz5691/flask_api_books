from locust import HttpLocust, TaskSet, between, task


class UserBehavior(TaskSet):
    @task(1)
    def get_books(self):
        self.client.get("/books")

    @task(1)
    def get_authors(self):
        self.client.get("/authors")


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(5.0, 9.0)
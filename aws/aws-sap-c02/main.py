import time
import random
import urllib.request


if __name__ == "__main__":
    url_head = "https://free-braindumps.com/amazon/free-aws-solutions-architect-professional-braindumps.html?p="
    for i in range(65, 112):
        urllib.request.urlretrieve(f"{url_head}{i+1}", f"webpage\\page_{i}.html")
        time.sleep(random.randint(10, 20))

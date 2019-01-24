import json

if __name__ == "__main__":
    with open('examples/our_tree1.json') as json_data:
        data = json.load(json_data)
        #print(data[0]["transaction"])
        for p in data:
            print p["id"]

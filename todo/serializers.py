

def ToDoSerializer(item) -> dict:
    return {
        "id": str(item["_id"]),
        "title": item["title"],
        "description": item["description"]
        }


def ToDosSerializer(entity) -> list:
    return [ToDoSerializer(item) for item in entity]

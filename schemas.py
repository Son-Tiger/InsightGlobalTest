pet = {
    "type": "object",
    "required": ["name", "type"],
    "properties": {
        "id": {
            "type": "integer"
        },
        "name": {
            "type": "string"
        },
        "type": {
            "type": "string",
            "enum": ["cat", "dog", "fish"]
        },
        "status": {
            "type": "string",
            "enum": ["available", "sold", "pending"]
        },
    }
}
order = {
    "type": "object",
    "required": ["id", "petId", "status"],
    "properties": { 
        "id": {
            "type": "integer"
        },
        "petId": {
            "type": "integer"
        },
        "status": {
            "type": "string",
        }
    }
}
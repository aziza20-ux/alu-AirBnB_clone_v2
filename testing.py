from models.base_model import BaseModel
from models import storage

# Step 1: Create a new object
obj = BaseModel()
obj.name = "Aziza"
obj.number = 42

# Step 2: Save it to file.json
obj.save()

# Step 3: Confirm it's in memory
print(storage.all())  # Shows objects currently in memory

# Step 4: Simulate a new run: clear and reload
storage.reload()

# Step 5: Confirm it was reloaded from file.json
print(storage.all())
for k, v in storage.all().items():
    print(v)

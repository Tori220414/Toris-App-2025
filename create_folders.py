import os

base_path = r"c:\Users\Tori\Tori's coding application"

folders = [
    "backend/src/controllers",
    "backend/src/models",
    "backend/src/routes",
    "backend/src/services",
    "backend/src/middlewares",
    "backend/src/utils",
    "backend/config",
    "frontend/public",
    "frontend/src/components",
    "frontend/src/pages",
    "frontend/src/services",
    "frontend/src/styles",
    "frontend/src/utils",
    "mobile/android",
    "mobile/ios",
    "mobile/src/components",
    "mobile/src/screens",
    "mobile/src/services",
    "mobile/src/styles",
    "mobile/src/utils",
    "docs/api",
    "docs/user-guides",
    "tests/backend",
    "tests/frontend",
    "tests/mobile",
    "tests/e2e",
]

for folder in folders:
    path = os.path.join(base_path, folder)
    os.makedirs(path, exist_ok=True)

print("Folders created successfully!")
# Add this to your script to create .gitkeep in each folder
for folder in folders:
    path = os.path.join(base_path, folder)
    os.makedirs(path, exist_ok=True)
    gitkeep_path = os.path.join(path, ".gitkeep")
    with open(gitkeep_path, "w") as f:
        pass
print(".gitkeep files created successfully!")
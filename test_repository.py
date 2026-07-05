from database.repository import Repository

repo = Repository()

project_id = repo.create_project(
    "Synthetic Quant"
)

print(f"Created Project ID: {project_id}")

print()

print("Projects:")

for project in repo.get_projects():
    print(dict(project))
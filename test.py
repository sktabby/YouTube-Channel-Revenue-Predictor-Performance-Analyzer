#generating a requiremnets.txt file

# generate_requirements.py

packages = [
    "flask",
    "joblib",
    "numpy"
]

with open("requirements.txt", "w") as f:
    for package in packages:
        f.write(package + "\n")

print("requirements.txt file created!")

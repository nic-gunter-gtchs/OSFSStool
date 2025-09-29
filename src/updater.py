# CLI app that provides a frontend to add definitions and article links to the DB
from handler import *

print("OSFSSdb Updater\n")
subject = input("Enter the acronym you'd like to update the information for: ").upper().strip()
#TODO: call db read function and check for existing values. if so, expect output formatted as {"titles":[],"descs":[],"links":[]} where a blank list element is used if no value is provided in each category

if result != None:
  print(f"\nAcronym {subject} has existing data:")
  for title in range(result["titles"]):
    print(f"{result["titles"][title]}: {result["descs"][title]}\n{result["links"][title]}\n")
ntitle = input("Please enter the definition you'd like to update or create. ").capitalize().strip()
ndesc = input("Optionally enter a short description of the meaning. ").strip()
nlink = input("Optionally enter a link to a Wikipedia article on the subject. Strongly recommended. ").lower().strip()
#TODO: call db update function and define args
print("\nDone. Exiting...\n")

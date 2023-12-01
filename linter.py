import sys
from pylint import lint

TRESHOLD = 10
run = lint.Run(["main.py"] ,exit = False)
score = run.linter.stats.global_note

print(f"Score: {score}")

if score < TRESHOLD:
    print(f"Linter failed with score: {score}")
    sys.exit(1)
sys.exit(0)
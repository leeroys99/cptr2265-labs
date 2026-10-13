# Lab 7 Starter Files: SOLID Refactoring & Design Patterns

Language: **Python** · Requires: Python 3.10 or newer

Unzip this into the root of your `cptr2265-labs` repository so the files land in `lab07/`.

| File | Used for |
|---|---|
| `starter/order_system.py` | **Part A.** The campus bookstore order system. It runs, but it violates at least three SOLID principles. |
| `partB/number_collection.py` | **Part B (optional).** A small collection with a hard-coded sorting choice to refactor with the Strategy pattern. You may write your own data structure instead. |
| `code-review-template.md` | **Part C.** Copy to `lab07/code-review.md` and fill it in. |

## Running the starters
```
cd lab07/starter
python order_system.py

cd ../partB
python number_collection.py
```
The Part A demo prints two receipts and then reports a crash on the third order. That crash is caused by one of the design problems you are looking for.

## Suggested folder layout for your submission
```
lab07/
  starter/       <- leave as given
  original/      <- copy of the starter, annotated with  SOLID VIOLATION (...)  comments
  refactored/    <- your SOLID-compliant version (may be several files)
  partB/         <- your Strategy pattern implementation
  code-review.md
```
Commit the annotated original and the refactored version in **separate commits** so your history shows the progression.

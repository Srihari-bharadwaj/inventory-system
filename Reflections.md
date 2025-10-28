# Reflection – Static Code Analysis Lab

# 1. Which issues were the easiest to fix, and which were the hardest? Why?
The easiest ones to fix were style issues like missing blank lines, unused imports, and function naming. They were mostly formatting-based and quick to correct.
The hardest was dealing with the global variable warning since it required changing how the data was handled inside functions without breaking the program’s logic.

# 2. Did the static analysis tools report any false positives? If so, describe one example.
Yes, Pylint gave a warning about using the global statement even though it was actually needed to load the inventory data properly. The code works fine and it’s not a real issue in this small script.

# 3. How would you integrate static analysis tools into your actual software development workflow?
I’d integrate tools like Pylint, Bandit, and Flake8 in a CI pipeline using GitHub Actions. They could automatically run checks on every commit or pull request. I’d also run them locally before pushing code to catch simple mistakes early.

# 4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?
After applying the fixes, the code became cleaner, easier to read, and more secure. Using proper naming, safe file handling with with, and input validation made it more reliable and less error-prone. The final code feels more professional and maintainable.
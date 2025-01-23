# Instructions for injecting external content on build

Hugo is static, so i cannot fetch content on runtime from APIs like Readwise to display my latest reads.

Therefore before building the site, I have to run the scripts I wrote to inject this content into the markdown files.

## Add Readwise Reads

[python script](scripts/reads.py)


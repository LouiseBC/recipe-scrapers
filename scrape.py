from recipe_scrapers import scrape_me
import sys

# give the url as a string, it can be url from any site listed below
scraped = scrape_me(sys.argv[1])


print(scraped.servings())
print("\n".join(scraped.ingredients()))
sys.stdout.flush()
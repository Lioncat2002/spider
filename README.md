# Spider
A web crawler for crawling through a "free" games website
coupled with a svelte based front end for showing the games

## Parts:

### Python web crawler
- Uses BeautifulSoup4 for parsing the html 
- Uses requests to fetch the pages
- Lives in the `web scraping` directory

### Svelte front end
- Displays the json thus created by the web crawler
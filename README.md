# Maria Group Co. Ltd. website

The Arabic, English and Simplified Chinese editions are static HTML. Update the content and related-page slugs in `site/content.json`, then run `python3 site/build.py` and commit the generated pages. The styling is in `assets/corporate.css`. A seventh entry in a content row is a space-separated list of related page slugs. An optional eighth entry selects an existing emblem.

To review locally, open `index.html` in a browser or run `python3 -m http.server 8080` from the repository root.

The three existing PDFs are retained byte for byte. They contain Rodeena statements requiring approval, so the review edition directs document enquiries to email. The independent Rodeena concept is in `review/rodeena.md`. All review pages include a noindex directive. Official indexing and sitemap changes belong in the publication review.

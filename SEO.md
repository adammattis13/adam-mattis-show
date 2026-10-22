# Search and AI-search discoverability

Canonical public origin: https://www.theadammattisshow.com/. The Sites copy retains its existing owner-only access and is not crawlable by search engines. Deploy these same files to the public domain for indexing; a Sites publication does not change access or automatically deploy another host.

The homepage includes canonical and social metadata, a linked WebSite/WebPage/PodcastSeries/Person/Organization/PodcastEpisode graph, and a visible FAQ mirrored in FAQPage markup. Podcast and FAQ markup does not guarantee a Google rich result. No ratings, invented transcripts, or unverified guest information are included. Episode reading/listening time is approximate and uses timeRequired rather than claiming exact audio duration.

robots.txt allows crawlers and advertises sitemap.xml. The sitemap lists only the real homepage; fragment anchors are not separate pages. This permission cannot override host authentication or a provider's X-Robots-Tag. Submit the public-domain sitemap in a verified Google Search Console and Bing Webmaster Tools property, then inspect indexing after the public host serves the new files. No property verification credentials are stored in this repo.

Keep JSON-LD aligned with visible copy. After changing its exact text, recompute the SHA-256 CSP hash in both the HTML meta policy and _headers. Preserve existing access controls. Google AI search uses the same foundational crawlability, helpful content, and factual structured-data principles as conventional search; no special AI file or ranking promise is needed. See https://developers.google.com/search/docs/appearance/ai-features.

Run python3 scripts/build.py before packaging. Validate the structured data, sitemap, canonical, and deployed headers when changing the public origin.

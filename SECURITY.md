# Security and deployment

This project is a static HTML, CSS, JavaScript, and image site. It requires no PHP runtime, database, or server-side packages. Disable PHP handlers on any self-managed host serving this site; patch any separately installed runtime through the hosting provider.

The HTML enforces a restrictive Content Security Policy without inline scripts, inline styles, or eval. Google Analytics, Google Fonts, and the Spotify player are explicitly allowed. New external integrations require a policy review. Analytics executes in the main page, so it remains a trusted third party.

The `_headers` file supplies additional response headers for hosts that support that format. On other hosts, configure the equivalent headers in the hosting platform. In particular, `frame-ancestors`, X-Frame-Options, X-Content-Type-Options, and Permissions-Policy require actual HTTP response headers; the HTML meta policy cannot enforce those protections. Verify the live response headers after deployment. Enable HTTPS redirects and HSTS through the provider after confirming HTTPS works for the domain.

Build the static deployment directory with `python3 scripts/build.py`. This copies only the intended public assets and header file into `dist`, excluding repository metadata and configuration. Publish the resulting `dist` directory. A Git push alone does not verify deployment or hosting protections.

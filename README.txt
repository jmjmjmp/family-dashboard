POKEMON-INSPIRED FAMILY DASHBOARD — GITHUB PAGES

Upload index.html, gengar.png, sync_calendar.py, and the .github/workflows/sync-calendar.yml file to the ROOT of the same GitHub Pages repository (preserve the .github/workflows directories).

Your public Google Calendar must be set to "Make available to public" with event details visible.

In GitHub: Settings > Actions > General, enable Actions and grant "Read and write permissions" for GITHUB_TOKEN if the workflow cannot push.

Then open Actions > Sync public family calendar > Run workflow once. This generates calendar-events.json. Scheduled updates run approximately every 30 minutes (GitHub schedule can be delayed).

Calendar events show in your own illustrated dashboard instead of Google's embedded iframe. No third-party cookie prompt.

IMPORTANT: Public calendar event titles and details are public. Only add family activities you are comfortable making public.

The layout is optimized for landscape. Older iPad Safari may not support all modern CSS, and very small screens may show fewer events to avoid scrolling.

NOTE: If your GitHub Pages publishes from /docs rather than repository root, adjust the output path for calendar-events.json accordingly.

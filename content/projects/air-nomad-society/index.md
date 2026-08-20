---
date: '2024-05-20'
draft: false
title: 'Air Nomad Society'
url: 'air-nomad-society'
cover:
  image: "images/cover.png"
weight: 2
---

Air Nomad Society is a free email service that sends subscribers the best flight deals based on their travel preferences on a weekly basis as an email.

You can [signup](https://ans.timonrieger.de) and view the [source code on GitHub](https://github.com/timonrieger/air-nomad-society).

## Intention

The reason for building this email service originally came from Dr. Angela Yu's [100 Days of Code Bootcamp](https://www.udemy.com/course/100-days-of-code/), which basically started my whole journey into the world of software and programming. I think on day 35 of that course we started developing this flight service. The idea behind it was that you have a Google Sheet as a database replacement (back then we hadn't talked about/learned how to interact with databases programmatically) and you get the countries listed in the file and you search for the best flights to those places and save the price back.

In 2026 I picked the project back up, mostly because I'm travelling a lot more now and found myself wanting exactly the features it was missing. So I became my own user again. The old version was glued together from my early coding days, and every new idea was fighting the old foundation. I rebuilt the whole thing. The real point of the rework is what it enables next: more departure cities, smarter and less repetitive suggestions, and eventually planning whole trips instead of single flights.

## Timeline

Somehow I really liked this idea and I expanded the project more and more over time. I started development around April 2024 and initially hosted it directly on my website. Later, in November, I migrated the codebase (aka separated it from the website code) and have been hosting it on [ans.timonrieger.de](https://ans.timonrieger.de) ever since.
After a quiet phase, I rebuilt the service from the ground up in August 2026 — new backend, new website, new email flow — and I'm actively developing it again.

## Tech Stack

- Backend made with [FastAPI](https://fastapi.tiangolo.com/)
- Frontend made with [SvelteKit](https://svelte.dev/), [Tailwind CSS](https://tailwindcss.com/) and [bits-ui](https://bits-ui.com/)
- Data by [Kiwi Flights API](https://tequila.kiwi.com/)
- Database on [PostgreSQL](https://www.postgresql.org/)
- Hosted on [Vercel](https://vercel.com)
- Weekly emails sent via [GitHub Actions](https://github.com/features/actions)
- Email designed with [Beefree](https://beefree.io/)

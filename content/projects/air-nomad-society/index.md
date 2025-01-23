---
date: '2024-05-20'
lastmod: '2025-01-22'
draft: false
title: 'Air Nomad Society'
url: 'air-nomad-society'
summary: 'Air Nomad Society is a free email service that sends subscribers the best flight deals based on their travel preferences on a weekly basis as an email.'
cover:
  image: "cover.png"
---

Air Nomad Society is a free email service that sends subscribers the best flight deals based on their travel preferences on a weekly basis as an email.

You can signup [here](https://ans.timonrieger.de) and view the source code on [Github](https://github.com/timonrieger/air-nomad-society).

## Intention

The reason for building this email service originally came from Dr. Angela Yu's [100 Days of Code Bootcamp](https://www.udemy.com/course/100-days-of-code/), which basically started my whole journey into the world of software and programming. I think on day 35 of that course we started developing this flight service. The idea behind it was that you have a Google Sheet as a database replacement (back then we hadn't talked about/learned how to interact with databases programmatically) and you get the countries listed in the file and you search for the best flights to those places and save the price back.

## Timeline

Somehow I really liked this idea and I expanded the project more and more over time. I started development around April 2024 and initially hosted it directly on my website. Later, in November, I migrated the codebase (aka separated it from the website code) and have been hosting it on [ans.timonrieger.de](https://ans.timonrieger.de) ever since.
While this service is still running, I am no longer actively developing it.

## Tech Stack

- Backend/server made with [Flask](https://flask.palletsprojects.com/en/stable/)
- Frontend made with [Jinja](https://jinja.palletsprojects.com/en/stable/)
- Data by [Kiwi Flights API](https://tequila.kiwi.com/)
- Hosted on [Vercel](https://vercel.com)
- Cron job via [Render](https://render.com)
- Email designed with [Beefree](https://beefree.io/)

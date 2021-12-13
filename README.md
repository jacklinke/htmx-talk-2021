# Server-Side is Dead! Long Live Server-Side (+ HTMX)

This repository contains the example code and slides for the talk "Server-Side is Dead! Long Live Server-Side (+ HTMX)", given at DjangoCon US 2021 and then (modified) for Code Code Code in December of 2021.


## Contents
- [Examples](#examples)
	- [Messaging inbox functionality (read/archive)](#messaging)
	- [One-click settings](#settings)
	- [Multiple forms in multiple tabs](#tabs-with-forms)
	- [Lazy data popovers](#lazy-data-popovers)
- [Slides](#slides)
- [Video](#video)
- [Resources](#resources)

## Examples

Here are screenshots of the examples I talk through, transitioning from plain Django templates (plus a bit of ajax in the `settings` example), to Django + HTMX. The `examples` folder contains a django project with each of these examples.

Keep in mind these examples are stripped to the absolute minimum in order to make the concepts I discuss in the talk as clear as possible, so the examples do not take security best practices into account. For instance, in the `settings` example, you would want to decorate the view with `@login_required`.

The example includes fixtures for getting up-and-running quickly. After migrating, loading fixtures, and starting runserver, log into admin (http://127.0.0.1:8000/admin/) with credentials `user` `pass`, and then go to the homepage (http://127.0.0.1:8000/).

### Messaging

How do you add the ability to click on an icon to archive messages, without having to refresh the entire page to see the changes? Here's an example.

![Messages screenshot](https://raw.githubusercontent.com/jacklinke/htmx-talk-2021/master/media/messages_htmx.png)

### Settings

In this example, we allow the current user to change their settings via a set of checkboxes (which relate to BooleanField fields in the database) without refreshing the page. They also get a momentary alert of the update.

![One-click settings screenshot](https://raw.githubusercontent.com/jacklinke/htmx-talk-2021/master/media/settings_htmx.png)

### Tabs-With-Forms

This example presents a use-case where multiple forms are needed on a single webpage, each hidden within its own tab. We use HTMX to load each tab's contents only when needed and to submit each form without needing a page refresh.

![Tabbed forms screenshot](https://raw.githubusercontent.com/jacklinke/htmx-talk-2021/master/media/tabs_htmx.png)

### Maps with Lazy Data Popovers

This example presents a use-case where a data-rich map (or datatable, etc) utilized popovers with additional information. Rather than loading all of the popover content on page load, we can load the popover contents lazily when the user clicks on the map feature.

![Lazy Data Popovers screenshot](https://raw.githubusercontent.com/jacklinke/htmx-talk-2021/master/media/map_popovers_htmx.png)

## Slides

Slides are available in the media folder. You can access them directly here:

- [Download OpenDocument Presentation file](https://github.com/jacklinke/htmx-talk-2021/blob/master/media/Server-Side_is_Dead!_Long_Live_Server-Side_(+HTMX).odp?raw=true)
- [View OpenDocument Flat XML Presentation file](https://github.com/jacklinke/htmx-talk-2021/blob/master/media/Server-Side_is_Dead!_Long_Live_Server-Side_(+HTMX).fodp?raw=true)

## Video

[Video on DjangoConUS 2021 YouTube Playlist](https://www.youtube.com/watch?v=t98bKdeUHsU&list=PL2NFhrDSOxgXnYlkheXeHSE6mTXaFhaaD)
[Video on Code Code Code YouTube Playlist](https://youtu.be/MJQ9E1iap2Y)

## Resources

Resources mentioned in the talk:

- [htmx.org](https://htmx.org) - The home for HTMX examples, references, and further resources.
- [django-htmx](https://github.com/adamchainz/django-htmx) - Adam Johnson's django package with helpful utilities for making integration of Django and HTMX easier.
- [awesome-htmx](https://github.com/rajasegar/awesome-htmx) - Links to talks, blog posts, examples, and other things related to HTMX.
- [HTMX Discord](https://htmx.org/discord) - Very active community board for discussing HTMX and Django + HTMX.
- [r/htmx on Reddit](https://www.reddit.com/r/htmx/)
- [HTMX on GitHub](https://github.com/bigskysoftware/htmx)
- [_hyperscript](https://hyperscript.org/) - A speculative javascript library designed to work alongside HTMX. Simplifies writing event handlers and developing highly responsive user interfaces.
- [Alpine.js](https://alpinejs.dev/) - A lightweight javascript library for composing behavior directly in your markup which plays nicely with HTMX.

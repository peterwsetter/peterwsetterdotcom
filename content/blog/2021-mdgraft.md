title: mdgraft - Graft Markdown into HTML Template
author: Peter W Setter
description: mdgraft is a Python-based command line tool that converts markdown into HTML then merges elements into an HTML template by "grafting" elements from the markdown-to-HTML tree to the tree of the template. The application uses python-markdown2 and BeautifulSoup for the conversion and grafting, and packages for the command line using Typer.

## Goals of the Project

I recently decided to learn frontend development with the aim of building [Jamstack]() websites. As a complete beginner, I'm starting with basic HTML and CSS, using this [website](https://peterwsetter.com) as my learning project.

In the past, Peter W Setter Dot Com used [RMarkdown]() and [Pelican]() as its static site generator. In those and similar projects, much of the design of the website is given over to theme with the remaining pieces set in configuration files. For this project, I wanted an application that would convert my markdown posts and pages to HTML and apply the structure of my HTML template. Styles could be built directly into the template or, the option I elected, linked to in the template.

I wanted to use the tool as part of a build script, so I decided to use this as an opportunity to try [Typer](). I have experience using [FastAPI](), so my mind went straight to Typer for a command line application.

## Outline of the Process

1. Markdown content file is read-in and converted to HTML
1. Content HTML file is "merged" with an HTML template containing custom structure and links to styles.
1. Write final HTML to file

Additional criteria:

- For ease-of-use, application can take either a single file or a directory
  - If a single file, the final version is written to the output directory
  - If a directory, the directory is created within the output directory
- The application should allow page metadata to be set from the markdown document.

## Markdown to HTML Conversion

There are two Python libraries for converting markdown to HTML: [python-markdown](https://github.com/Python-Markdown/markdown) and [python-markdown2](https://github.com/trentm/python-markdown2). At the on-set, the choice seemed arbitary, so I decided to create versions of the application for each so performance and desired features could be compared.

Example markdown document: fill this in later

Code for converting example.md to example.html

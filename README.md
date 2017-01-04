# Oxford term dates

You need to set the `OXFORD_TERM_START` environment variable to the date of the
first Sunday of 1st week. In a UNIX environment:

```
export OXFORD_TERM_START="2017-01-15" # First Sunday of 1st week
```

You can get these dates from [this page][oxford-term-dates]

Then run either of the following:

```
> ./oxtermdate.py 2017-02-14
Tuesday of 5th week
> ./oxtermdate.py Tu5
2017-02-14
```

The day prefixes are `Su, M, Tu, W, Th, F, Sa`, date formats need to be [ISO
8601][df].

## License

Apache 2.0

[oxford-term-dates]: https://www.ox.ac.uk/about/facts-and-figures/dates-of-term
[df]: https://en.wikipedia.org/wiki/ISO_8601

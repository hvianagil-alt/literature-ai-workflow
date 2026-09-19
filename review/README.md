# `review/` — where the workflow writes your outputs

This is scratch space the agent writes to while it works through your papers. You never need to create anything here yourself.

```
review/
├── notes/     one Markdown file per paper (extracted facts, quotes, page refs)
├── table/     the running literature comparison table (literature-table.md)
└── report/    the final synthesized report (final-report.md)
```

These are your research outputs, not repo source, so they're **git-ignored by default** (see the root `.gitignore`) — the same reasoning as for `papers/`: your unpublished research direction shouldn't leak into a public repo by accident.

If you want to keep a particular note, table, or report in version control (e.g. to share with collaborators via git), just `git add -f` that specific file, or remove its pattern from `.gitignore`.

For what these files should look like, see the worked examples in [`examples/`](../examples/README.md).

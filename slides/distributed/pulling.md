#Remote repositories
###Pulling (from a remote branch)

More usually you want to get new commits from one of the remote's branches (usually `master`):

```bash
git pull origin master
```

This is more or less equivalent to a `fetch` followed by a `merge` with the remote branch

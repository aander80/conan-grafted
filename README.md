If the local commit exists in the remote but not in a current branch, then the current commit is
grafted by `conan.tools.scm.Git` when using `coordinates_to_conandata()`. This is because
`coordinates_to_conandata()` calls `git fetch --dry-run --depth=1` which grafts the commit despite
the `--dry-run` flag.

To reproduce the error, clone this repo, then run the following commands:

```shell
git fetch origin ac4e4dc3ca4cb1529f79beaed822a530d9fd500c  # This commit exists in the remote but is not referenced by any branch
git checkout ac4e4dc3ca4cb1529f79beaed822a530d9fd500c
git log  # Run git log to see the commit history
conan export .  # Export the conanfile to the cache; this will make the current commit grafted
git log  # Run git log to see that the current commit is grafted
```
